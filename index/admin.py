from django.contrib import admin
from index.models import Article
from index.models import Email

admin.site.register(Article)
admin.site.register(Email)