from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets

from profilr_api import serializers

class HelloAPIView(APIView):
    """Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format =None):
        an_apiview = [
         'Uses HTTP methods as function(get,post,patch,put,delete)',
         'Is similar to a traditional Django View',
         'Gives you the most control over your application logic',
         'Is mapped manually to URLs',

         ]
        return Response({'message':'Hello','an_apiview':an_apiview})


    def post(self,request):
        serializer  = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'message':'PUT'})

    def patch(self,request,pk=None):
        '''handle partial update of object'''
        return Response({'message':'PATCH'})

    def delete(self,request,pk = None):
        'Deletes an object'
        return Response({'message':'DELETE'})


class   HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset = [
          'uses actions (list,create,retrieve,update,partial_update)',
          'Automatically maps to URLs using Routers',
          'Provides more functionality with less code',
          ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        'Create a new hello message'
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status =status.HTTP_400_BAD_REQUEST
            )


    def  retrieve(self,request,pk = None):

        return Response({'http_method':'GET'})

    def update(self,request,pk =None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk =None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk =None):
        return Response({'http_method':'DELETE'})
