from django import forms
from taggit.managers import TagField
import datetime
from .models import *

class EntryForm(forms.ModelForm):
    
    title=forms.CharField(label="Entry Title", max_length=255, required=True)
    content=forms.CharField(label="Entry", widget=forms.Textarea, required=True)
    # category=models.CharField(label="Category", max_length=50, blank=True, null=True, choices=constants.CATEGORY_CHOICES)
    # language=models.CharField(label="Language", max_length=2, blank=True, null=True, choices=settings.LANGUAGE_CHOICES)
    tags=TagField(required=False)

    class Meta:
        model=Entry
        verbose_name_plural="Entries"
        fields=['title', 'content', 'tags']
