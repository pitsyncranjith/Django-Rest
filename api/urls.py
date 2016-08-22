from django.conf.urls import url
from . import views

app_name = 'api'
urlpatterns = [
	url(r'^tasks/$', views.task_list, name='task_list'),
	url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
	]