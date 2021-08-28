from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_3 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_4 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_5 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_6 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_7 = models.ImageField(null=True, blank=True, upload_to="images/")
    #content = models.TextField()
    content_1 = RichTextField(blank=True, null=True)
    content_2 = RichTextField(blank=True, null=True)
    content_3 = RichTextField(blank=True, null=True)
    content_4 = RichTextField(blank=True, null=True)
    content_5 = RichTextField(blank=True, null=True)
    content_6 = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('geodrapp-post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)