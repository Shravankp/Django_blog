from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hey/$', views.index, name="index")
]