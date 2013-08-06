from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import NewsPlugin, News
from django.utils.translation import ugettext as _

class CMSNewPlugin(CMSPluginBase):
    model = NewsPlugin
    name = _("Nouvelles")
    render_template = "news/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(CMSNewPlugin)