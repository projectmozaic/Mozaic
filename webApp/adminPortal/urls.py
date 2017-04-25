from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$|index$', views.index, name='index'),
    url(r'^success$|SUCCESS$', views.success, name="success"),
    url(r'^generate$|Generate$', views.generate, name="generate"),
    url(r'^process$|PROCESS$', views.process, name="generate"),
    url(r'^config$|CONFIG$', views.config, name="config"),
    url(r'^configedit$|CONFIGEDIT$', views.configedit, name="configedit"),
    url(r'^student$|STUDENT$', views.student, name="student"),
    url(r'^imagestudent$|IMAGESTUDENT', views.imagestudent, name="student")
]
