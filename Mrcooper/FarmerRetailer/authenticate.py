from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .base_view1 import BaseView


class AuthenticatedView(BaseView):
    """ Base class for the views which needs to be authenticated from auth service. """

    def __init__(self, *args, **kwargs):
        super(AuthenticatedView, self).__init__(*args, **kwargs)


class AuthenticatedViewSet(AuthenticatedView, viewsets.ViewSet):
    """Base class for the views which needs to be authenticated in application"""
    pass


class AuthenticatedAPIView(AuthenticatedView, APIView):
    """Base class for the views which needs to be authenticated in application"""
    pass
