from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import date
from django_extensions.db.fields import AutoSlugField
from PIL import Image
# from autoslug import AutoSlugField

gender = {
    ('Male','Male'),
    ('Female', 'Female'),
    ('Others','Others')
}
class User(AbstractUser):
    # username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(max_length=200)
    # password = models.CharField(max_length=200)
    # confirm_password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=gender, default='Male')
    # image = models.ImageField(upload_to="post_images/images")

    def __str__(self):
        return self.email
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name',unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name





class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tags)
    title = models.CharField(max_length=200)
    text = models.TextField()
    featured = models.ImageField(upload_to='featured/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    parent=models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    
    class Meta:
        ordering=('-created_date',)
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name

    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


    # image = models.ImageField(upload_to="post_images/images")
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # def __str__(self):
    #   return "{}".format(self.email)