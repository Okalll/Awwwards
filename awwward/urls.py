from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^$", views.signup, name="signup"),
    url(r"^home/", views.home, name="home"),
    url(r"^upload/", views.upload, name="upload"),
    url(r"^profile/", views.profile, name="profile"),
    url(r"^project/(?P<project_id>[0-9])$", views.project, name="project"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
