from django.conf.urls import url
from myapps.user import views

urlpatterns = [
    url(r'^regist/$', views.regist),

]





