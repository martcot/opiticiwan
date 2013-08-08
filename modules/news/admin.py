# -*- coding: utf-8 -*-
from news.models import *
from app.models import *
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import admin, messages
from datetime import datetime
from django.utils import formats

def sendEmails(modeladmin, request, queryset):
	
	subscriptions = Subscription.objects.all()
	count = 0
	
	for subscription in subscriptions:
		try:
			dt = datetime.now()
			email_content = render_to_string('app/email_news_subscription.html', {'subscription': subscription,'news':queryset,"date":dt,"host":settings.HOSTNAME})
			df = formats.date_format(dt, 'DATE_FORMAT')
			email = EmailMultiAlternatives(_(u'Infolettre du ')+df, email_content, settings.SEND_EMAILS_TO, [subscription.courriel])
			email.attach_alternative(email_content, "text/html")
			email.send()
			count += 1
		except Exception as e:
			modeladmin.message_user(request, _(u"Une érreur est survenue.") + " : " + str(e), level=messages.ERROR)
	
	modeladmin.message_user(request, str(count) + "/" + str(len(list(subscriptions))) + " courriels envoyés.", level=messages.SUCCESS)
	
sendEmails.short_description = _(u"Envoyer les nouvelles sélectionnées par courriels via l'infolettre.")
	
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'lang')
	date_hierarchy = 'pub_date'
	actions = [sendEmails]
	
admin.site.register(News,NewsAdmin)