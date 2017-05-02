from django.conf.urls import url

from . import  views

urlpatterns =[ url(r'^$',views.index,name='index'),
               url(r'scemo',views.scemo,name='scemo'),
               url(r'^SEES\/(?P<question_id>.+)/$',views.SEES,name="SEES"),
               url(r'^recents\/(?P<quanto>.+)/$',views.recents,name="recenti"),
               url(r'^conto',views.count,name="quanto")]