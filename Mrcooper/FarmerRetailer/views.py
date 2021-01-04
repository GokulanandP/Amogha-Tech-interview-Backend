from rest_framework import status
from rest_framework import viewsets
import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .authenticate import AuthenticatedViewSet
from .models import Customer
from .base_view1 import BaseView
from .serializers import CustomerSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

#Viewset is used
class Farmer(viewsets.ViewSet):
    def list(self, request):
        queryset = Customer.objects.filter(user_type=2, crop_type=1)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)


    # queryset = Customer.objects.filter(user_type=2, crop_type=1)
    # serializer_class = CustomerSerializer
    #
    # def list(self, request):
    #     response = Customer.objects.filter(user_type=2, crop_type=1).values('user_name', 'address', 'contact')
    #     response = dict(response)
    #     serializer = self.get_serializer(response,many = True)
    #     return Response(serializer.data)





    #     this_user_cultivates = Customer.objects.filter(user_key =1000).values('user_type')
    #     serializer = CustomerSerializer()
    #     response =Customer.objects.filter(user_type=2,crop_type = 1).values('user_name','address','contact')
    #     response =self.response(is_success=True,
    #              status=status.HTTP_200_OK,
    #              data=response, message="Success")
    #     return response



        # return Response()
        # respone = list(respone)
        # print(respone)
        # respone = BaseView.response(is_success=False,
        #          status=status.HTTP_200_OK,
        #          data=respone, message="Success")
        # return respone

