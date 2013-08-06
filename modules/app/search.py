import haystack
import datetime
from haystack import indexes
from haystack import site
#from cms.plugin_pool import plugin_pool
from cms.models import Page
from news.models import News
from galeries.models import Gallery
from documents.models import Document, Category

#plugin_pool.get_plugin('TextPlugin').search_fulltext = True

class PageIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True, model_attr='text')
    title = indexes.CharField(model_attr='get_page_title')
    get_slug = indexes.CharField(model_attr='get_slug')

    def prepare_text(self,obj):
        renderedplugins = ""
        for i in obj.cmsplugin_set.all():
            renderedplugins += i.render_plugin(context={})
        return renderedplugins

    def get_queryset(self):
        qs = Page.objects.published().filter(publisher_is_draft=False).values('get_slug').distinct()
        result_qs |= qs
        return qs


site.register(Page, PageIndex)

############################################################################################################################

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
    
class GalleriesIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Gallery

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
    
class DocumentsIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    short_content = indexes.CharField(model_attr='short_content')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
    
class CategoriesIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    
site.register(News, NewsIndex)
site.register(Gallery, GalleriesIndex)
site.register(Document, DocumentsIndex)
site.register(Category, CategoriesIndex)
  
haystack.autodiscover()