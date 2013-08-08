# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from django.core.validators import validate_email
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class EmailForm(forms.Form):
    nom = forms.CharField(
        label = _("Votre nom:"),
        max_length = 255,
        required = True,
    )

    courriel = forms.CharField(
        label = _("Votre courriel:"),
        max_length = 255,
        required = True,
    )
    
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_id = 'emailSubscriptionForm'
        self.helper.form_class = 'grid-100'
        self.helper.form_method = 'post'
        self.helper.form_action = '#emailSubscription_open'

        self.helper.add_input(Submit(_('Envoyer'), _('Envoyer'),css_class='btn-orange btn-large'))
        
    def clean_courriel(self):
        data = self.cleaned_data['courriel']
        try :
            validate_email(data)
        except:
            raise forms.ValidationError("Courriel invalide !")
 
class ContactForm(forms.Form):
    message = ""

    nom = forms.CharField(
        label = _("Votre nom:"),
        max_length = 255,
        required = True,
    )

    courriel = forms.CharField(
        label = _("Votre courriel:"),
        max_length = 255,
        required = True,
    )
    
    sujet = forms.CharField(
        label = _("Sujet:"),
        max_length = 255,
        required = True,
    )

    textarea = forms.CharField(
        label = _("Message:"),
        widget = forms.Textarea(),
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_id = 'contactForm'
        self.helper.form_class = 'grid-100'
        self.helper.form_method = 'post'
        self.helper.form_action = '#contactForm'

        self.helper.add_input(Submit(_('Envoyer'), _('Envoyer'),css_class='btn-orange btn-large'))

    def clean_courriel(self):
        data = self.cleaned_data['courriel']
        try :
            validate_email(data)
        except:
            raise forms.ValidationError("Courriel invalide !")