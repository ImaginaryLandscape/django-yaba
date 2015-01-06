from django import forms
from django_comments.forms import CommentForm
from nocaptcha_recaptcha.fields import NoReCaptchaField

class CommentFormNoEmail(CommentForm):
    email = forms.EmailField(label="Email Address", required=False)
    captcha = NoReCaptchaField()
