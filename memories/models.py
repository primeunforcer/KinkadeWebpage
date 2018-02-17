from django.db import models
from django.utils import timezone

class Memory(models.Model):
    class Meta:
        verbose_name_plural = "Memories"
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    attendees = models.CharField(max_length=200)
    story = models.TextField(max_length=7000)
    story_is_true = models.BooleanField(default=False)
    whos_fault  = models.CharField(max_length=200, default='Ian Townsend')
    memory_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
