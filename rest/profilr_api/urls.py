from django.conf.urls import url
from profilr_api import views

urlpatterns = [
    url(r'^hello-view/',views.HelloAPIView.as_view())
]
 
