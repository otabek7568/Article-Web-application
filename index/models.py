from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    category = models.CharField(max_length=100)
    author_full_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to="images_author/")
    author_job = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Email(models.Model):
    mail = models.EmailField()