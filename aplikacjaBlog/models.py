from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    STATUS_COICES = {
        ("draft", "draft"),
        ("published", "Published")
    }

    status = models.CharField(max_length=10, choices=STATUS_COICES, default="draft")

    def get_absolute_url(self):
        return reverse('aplikacjaBlog:post_detail', args=[self.publish.year,
                                                                    self.publish.month,
                                                                    self.publish.day,
                                                                    self.slug]
                                                                )

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title