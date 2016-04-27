from django.conf.urls import url
import article.views

urlpatterns = [

    # url(r'^commentspage/(?P<page_number>\d+)/$', article.views.article),
    url(r'^videos/get/(?P<article_id>\d+)/(?P<art_page_number>\d+)/$', article.views.article),
    url(r'^page/article/addlike/(?P<article_id>\d+)/$', article.views.addlike),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
    url(r'^videos/page/(\d+)/$', article.views.articles),
    url(r'^writtens/page/(\d+)/$', article.views.articles),
    url(r'^$', article.views.articles),
]
