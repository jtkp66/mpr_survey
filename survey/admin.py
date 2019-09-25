from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'coordinator', 'is_complete', 'student', 'date_posted', 'author')
    list_display_links = ('id', 'coordinator')
    list_filter = ('author', 'coordinator', 'is_complete')
    list_editable = ('is_complete',)
    search_fields = ('coordinator', 'student', 'hostfamily', 'is_complete', 'author')
    list_per_page = 25

admin.site.register(Post, PostAdmin)
