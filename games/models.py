from django.db import models

class RetroGame(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.URLField(blank=True, null=True)
    youtube_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.platform})"
