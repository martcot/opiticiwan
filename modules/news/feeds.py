# -*- coding: UTF-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from news.models import News

class LatestEntriesFeed(Feed):
    title = _(u"Dernières nouvelles | Opiticiwan.ca")
    link = "http://opiticiwan.ca"
    description = _(u"Dernières nouvelles sur le site d'Opiticiwan.ca")

    def items(self):
        return News.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('new', args=[item.slug])
