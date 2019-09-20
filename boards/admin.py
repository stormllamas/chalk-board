from django.contrib import admin
from .models import Board, Topic, Post

# Register your models here.
# admin.site.register(Board)
# admin.site.register(Topic)
# admin.site.register(Post)

class TopicsInline(admin.TabularInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Board', {'fields': ['name', 'description']}),
    ]
    inlines = [TopicsInline]
    list_display = ('name', 'get_posts_count')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Board, BoardAdmin)


# class BoardInline(admin.TabularInline):
#     model = Board
#     extra = 1

class PostsInline(admin.TabularInline):
    model = Post
    extra = 3

class TopicsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['board', 'subject', 'starter', 'views']}),
        ('Date & Time Information', {'fields': ['last_updated'], 'classes': ['collapse']}),
    ]
    inlines = [PostsInline]
    list_display = ('board', 'subject', 'starter', 'views', 'last_updated')
    list_filter = ['board']
    search_fields = ['subject']

admin.site.register(Topic, TopicsAdmin)