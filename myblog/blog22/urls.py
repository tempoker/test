from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index), #尤其注意路径最后加上/和$
]