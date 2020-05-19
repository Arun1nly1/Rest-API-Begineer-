from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from profilr_api import views


router = DefaultRouter()
router.register(r'hello-viewset',views.HelloViewSet,base_name="hello-viewset")


urlpatterns = [
    url(r'^hello-view/',views.HelloAPIView.as_view()),
    url(r'',include(router.urls))
]
