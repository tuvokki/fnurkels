from django.contrib import admin

# Register your models here.
from .models import Article, Comment


# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    # fields = ['article_title', 'pub_date', 'article_text']
    fieldsets = [
        (None,      {'fields': ['article_title', 'pub_date']}),
        # ('Text',    {'fields': ['article_text'], 'classes': ['collapse']})
        ('Text',    {'fields': ['article_text']})
    ]
    inlines = [CommentInline]
    # list_display = ('was_published_recently')
    list_display = ('article_title', 'pub_date', 'was_published_recently')
    search_fields = ['article_text', 'article_title']

admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment)
