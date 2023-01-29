from django.urls import path, include
from Api import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views


router = DefaultRouter()

router.register('api', views.AssetViewSet, basename='assetapi')

router.register('checkin', views.CheckInViewSet, basename='checkinaip')

router.register('checkout', views.CheckOutViewSet, basename='checkoutapi')

router.register('checkoutandreturn', views.CheckOutAndReturnSerializerViewSet, basename='checkocutandreturn')

router.register('devicelog', views.DeviceLogViewSet, basename='devicelog')

router.register('company', views.CompanyCViewSet, basename='company')


urlpatterns = [
    path('', include(router.urls)),

    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]