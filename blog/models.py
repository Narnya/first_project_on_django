from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    post_number = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


