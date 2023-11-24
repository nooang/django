from django.contrib import admin
from .models import Post, Reply

class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'subject', 'create_date', 'modify_date']
  list_display_links = ['id', 'subject']
  search_fields = ['subject', 'content']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Reply)