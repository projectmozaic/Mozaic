from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submitted|SUBMITTED$', views.submitted, name="submitted")

]
