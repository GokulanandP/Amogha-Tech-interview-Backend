# from . import views
# from django.urls import path
# from django.conf.urls import include,url
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter
# from .views import FarmerViewset
#
# router = routers.DefaultRouter(views.FarmerViewset())
#
# router.register(r'farmer/', views.FarmerViewset,basename='farmer/')
#
# urlpatterns = [
#     # path('', views.home, name='home'),
#     # path('farmer/', views.Farmer, name='farmer')
#     url(r'^farmer/',include(router.urls))
# ]
# urlpatterns += router.urls

from . import views
from django.conf.urls import include,url
from rest_framework import routers
from django.urls import path
from .views import Farmer
router = routers.DefaultRouter(views.Farmer)

router.register(r'farmer/', views.Farmer,basename='farmer')


urlpatterns = [
    # path('', views.home, name='home'),
    # path(r'farmer/', Farmer.as_view(), name='farmer')

    url(r'^farmer/',include(router.urls))
]
urlpatterns += router.urls