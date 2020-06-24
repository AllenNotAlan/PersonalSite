from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible,label=False)
    from_email = forms.EmailField(required = True)
    subject = forms.CharField(required = False)
    message = forms.CharField(widget=forms.Textarea, required = True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].label = "Your Email:"
