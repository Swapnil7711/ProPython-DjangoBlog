from django.contrib import admin
from blog.models import Contact, Post

# Register your models here.

# Post Model
admin.site.register(Post)

# Conatct model
admin.site.register(Contact)
