from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = DefaultRouter()
router.register('berita', views.BeritaCrudCBV)

urlpatterns = [
	path('', include(router.urls)),
    path('get_jwt_token/', obtain_jwt_token), # GET JET TOKEN
    path('refresh_jwt_token/', refresh_jwt_token), # REFRESH JET TOKEN
    path('verify_jwt_token/', verify_jwt_token), # VERIFY JET TOKEN
]
