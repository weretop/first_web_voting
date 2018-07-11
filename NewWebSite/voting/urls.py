from django.urls import path, re_path
from voting import views

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^(?P<question_id>[0-9]+)/$',views.detail, name = 'detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$',views.results,name = 'results'),
    re_path(r'^(?P<question_id>[0-9]+)/voting/$',views.vote,name='vote'),
]

