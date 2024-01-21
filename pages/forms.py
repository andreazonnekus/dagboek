from django import forms

from .models import *

class Entry(forms.ModelForm):
    model = Entry

    title = models.CharField(label = "Entry Title", max_length=255, blank=False, null=True)
    content = models.TextField(label = "Entry", blank=False)
    visibility = models.BooleanField(label = "Visibility", blank=True, default=True)
    # category = models.CharField(label = "Category", max_length=50, blank=True, null=True, choices=constants.CATEGORY_CHOICES)
    # language = models.CharField(label = "Language", max_length=2, blank=True, null=True, choices=settings.LANGUAGE_CHOICES)
    tags = TaggableManager()
    entry_date = models.DateField(label = "Date", blank=True, default=datetime.datetime.now)

    class Meta:
        verbose_name_plural = "Entries"
