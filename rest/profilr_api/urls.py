from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'hello-viewset',views.HelloViewSet,base_name="hello-viewset")
router.register(r'profile',views.UserProfileViewSet )
router.register(r'feed',views.UserProfileFeedViewSet )

urlpatterns = [
    url(r'^hello-view/',views.HelloAPIView.as_view()),
    url(r'^login/',views.UserLoginApiView.as_view()),
    url(r'',include(router.urls)),
]
