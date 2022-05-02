
from django.contrib import admin
import site
from app import models
from app.models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
admin.site.register(models.BlogPost,BlogPostAdmin)




