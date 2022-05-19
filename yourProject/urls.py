from django.conf.urls import url
from yourProject import views



urlpatterns = [
    url(r'^projectDetails$', views.ProjectDetailsApi),
    url(r'^projectDetails/([0-9]+)$', views.ProjectDetailsApi)
]
