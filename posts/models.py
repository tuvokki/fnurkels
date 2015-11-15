import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# from posts.models import Article, Comment
# from django.utils import timezone
# a = Article(article_text="Lorem ipsum, whatever and dolor sid amet.", pub_date=timezone.now())
# a.save()
# a.id
# a.article_text
# Article.objects.all()
class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article)
    text = models.CharField(max_length=140)

    def __unicode__(self):
        return self.text
