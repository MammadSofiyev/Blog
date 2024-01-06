from django.contrib import admin
from .models import Post,Contact,Comment,About
# Register your models here.


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(About)

