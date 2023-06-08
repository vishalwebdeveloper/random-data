
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from randomapp.views import *
router = DefaultRouter()
# router.register('',modelViewset)
router.register('',StudentViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
