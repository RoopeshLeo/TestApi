from django.conf.urls import url
from .views import FileViewSet,CollegeViewSet,CollegeListViewSet

urlpatterns = [
    url(r'^upload/$', FileViewSet.as_view(), name='file-upload'),
    url(r'^reg/$', CollegeViewSet.as_view(), name='college-reg'),
    url(r'^list/$', CollegeListViewSet.as_view(), name='college-list'),
]