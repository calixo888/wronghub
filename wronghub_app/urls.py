from . import views
from django.conf.urls import url

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^ask/$", views.ask, name="ask"),
    url("^answer/$", views.answer, name="answer"),
]
