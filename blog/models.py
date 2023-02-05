from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ManyToOne
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='image/articles')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
    class Meta:
        pass