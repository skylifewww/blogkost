# -*- coding: utf-8 -*-  

from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
import mptt
from mptt.fields import TreeForeignKey
import random
from blogKost import settings
from easy_thumbnails.fields import ThumbnailerImageField


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    c = filename.split(".")
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + "." + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=250, verbose_name=u"Имя категории", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Родительский класс")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ('tree_id','level')

    def __unicode__(self):
        return self.name



    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Category, order_insertion_by=['name'])




class Author(MPTTModel):
    slug = models.CharField(max_length=250, blank=True, verbose_name=u"Урл")
    name = models.CharField(max_length=200, verbose_name=u"Автор статьи", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Родительский класс")

    class Meta:
        db_table = "authors"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ('tree_id', 'level')

    def __unicode__(self):
        return self.name


    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Фото эксперта'
    pic_slug.allow_tags = True       

    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Author, order_insertion_by=['name'])


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name=u"Название тега")

    class Meta:
        db_table = "tags"
        verbose_name = "теги"
        verbose_name_plural = "тег"

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    article_title = models.CharField(max_length=250, verbose_name=u"Название статьи")
    article_date = models.DateTimeField(verbose_name=u"Дата публикации статьи")
    # article_number = models.IntegerField(default=0, verbose_name="Номер статьи", blank=True, null=True)
    # article_likes = models.IntegerField(default=0, verbose_name="Лайки")
    article_tag = models.ManyToManyField(Tag, related_name="tags", related_query_name="tags", verbose_name=u"Теги")
    article_category = TreeForeignKey(Category, related_name="articles", verbose_name=u"Категории", default="", blank=True)
    article_author = TreeForeignKey(Author, related_name="autor", max_length=200, verbose_name="Автор статьи", blank=True, default="")
    short_text_ru = RichTextUploadingField(blank=True, verbose_name=u"Короткое описание RU")
    short_text_en = RichTextUploadingField(blank=True, verbose_name=u"Короткое описание EN")
    video = models.CharField(max_length=250, blank=True, verbose_name=u"Видео id в кратком описании")
    image = ThumbnailerImageField(upload_to=make_upload_path, blank=True, verbose_name=u"Изображение")
    full_text_ru = RichTextUploadingField(blank=True, verbose_name=u"Полное описание RU")
    full_text_en = RichTextUploadingField(blank=True, verbose_name=u"Полное описание EN")
    article_video = EmbedVideoField(verbose_name=u'Видео', blank=True, help_text='URL video', null=True)
    video_published = models.BooleanField( blank=True, default="")
    text_published = models.BooleanField( blank=True, default="")
    video_only = models.BooleanField( blank=True, default="")
    written_only = models.BooleanField( blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, verbose_name=u"Урл")


    class Meta:
        db_table = 'article'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['article_date']

    def __unicode__(self):
        return self.article_title

   
    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка статьи'
    pic_slug.allow_tags = True               


# class Comments(models.Model):
#     comments_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата", null=True, blank=True)
#     comments_text = models.TextField(verbose_name="Добавте Ваш комментарий")
#     comments_article = models.ForeignKey(Article, verbose_name="Статья")
#     comments_user = models.ForeignKey(User, default=True, verbose_name="Пользователь")

#     class Meta:
#         db_table = 'comments'
#         verbose_name = "Комментарий"
#         verbose_name_plural = "Комментарии"
