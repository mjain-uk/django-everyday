from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from basiccrud.models import Todo
from basiccrud.serliazers import TodoSerializer, TodoModelSerializer


# Create your views here.

# using API view class
class TaskList(APIView):

    def get(self, request, *args, **kwargs):
        serialized_data = TodoSerializer(Todo.objects.all(), many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.validated_data, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'Error'}, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        try:
            id = kwargs['id']
            Todo.objects.get(pk=id).delete()
            return Response({'message': 'Success'}, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({'message': 'Error'}, status=HTTP_400_BAD_REQUEST)
        
    def put(self, request, **kwargs):
        try:
            id = kwargs['id']
            instance = Todo.objects.get(id=id)
            serializer = TodoSerializer(instance, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            
            return Response({"message":"Something wrong"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message":'something wrong'}, status=HTTP_400_BAD_REQUEST)
        
    def patch(self, request, **kwargs):
        try:
            id = kwargs['id']
            instance = Todo.objects.get(id=id)
            serializer = TodoSerializer(instance, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            
            return Response({"message":"Something wrong"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message":'something wrong'}, status=HTTP_400_BAD_REQUEST)


# Using Generic Views
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

        
        


