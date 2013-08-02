import haystack
import datetime
from haystack import indexes
from haystack import site
from cms.plugin_pool import plugin_pool
from news.models import News

plugin_pool.get_plugin('TextPlugin').search_fulltext = True

class NewsIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    short_content = indexes.CharField(model_attr='short_content')
    content = indexes.CharField(model_attr='content')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
    
site.register(News, NewsIndex)
  
haystack.autodiscover()