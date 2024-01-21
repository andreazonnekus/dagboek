import datetime

from django.db import models
from taggit.managers import TaggableManager
from user.models import CustomUser

class Entry(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=True)
    content = models.TextField(blank=False)
    visibility = models.BooleanField(blank=True, default=True)
    tags = TaggableManager()
    entry_date = models.DateField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return f"{self.title} - {self.entry_date}"
    
    def get_content_preview(self):
        preview = self.content.strip().split()[0:199]

        if len(self.content) >= 200:
            preview[-1] = preview[-1][::-1].replace('.','...',1)[::-1]
        
        return ' '.join(preview)

    class Meta:
        verbose_name_plural = "Entries"
