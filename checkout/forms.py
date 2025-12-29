# checkout/forms.py
from django import forms
from django.db import models
from django.utils import timezone

# Simple Newsletter model for storing emails (portfolio)
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]