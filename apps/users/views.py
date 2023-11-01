from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from apps.users.serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.urls.exceptions import Resolver404
from rest_framework import generics, status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

# Director Table
class DirectorViewset(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  Director.objects.all()
    serializer_class = DirectorSerializer
    # permission_classes = [ManagerandDirectorOrReadOnly]   
    def create(self, request, *args, **kwargs):
        data =  request.data
        try:
            director = Director.objects.create_user(username=data['username'],password=data['password'])
            serializer = DirectorSerializer(director,partial=True)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        except:
            return Response({'error':'Please be aware'})
    def update(self, request, *args, **kwargs):
        director  =  self.get_object()
        data = request.data
        director.username = data.get('username',director.username)
        director.password = data.get('password',director.password)
        director.save()
        serializer = DirectorSerializer(director,partial=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
# Manager Table
class ManagerViewset(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  Manager.objects.all()
    serializer_class = ManagerSerializer
    def create(self, request, *args, **kwargs):
        data =  request.data
        try:
            manager = Manager.objects.create_user(username=data['username'],password=data['password'])
            serializer = ManagerSerializer(manager,partial=True)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        except:
            return Response({'error':'Please be aware'})
    def update(self, request, *args, **kwargs):
        manager  =  self.get_object()
        data = request.data
        manager.username = data.get('username',manager.username)
        manager.password = data.get('password',manager.password)
        manager.save()
        serializer = ManagerSerializer(manager,partial=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
# Teacher Table
class TeacherViewset(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  Teacher.objects.all()
    serializer_class =TeacherSerializer
    def create(self, request, *args, **kwargs):
        data =  request.data
        try:
            teacher = Teacher.objects.create_user(username=data['username'],password=data['password'],first_name=data['first_name'],last_name=data['last_name'], )
            serializer =TeacherSerializer(teacher,partial=True)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error':'Please be aware'})
    def update(self, request, *args, **kwargs):
        teacher  =  self.get_object()
        data = request.data
        teacher.username = data.get('username',teacher.username)
        teacher.password = data.get('password',teacher.password)
        teacher.first_name = data.get('first_name',teacher.first_name)
        teacher.last_name = data.get('last_name',teacher.last_name)
        teacher.save()
        serializer = TeacherSerializer(teacher,partial=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


class UserViewset(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  User.objects.all()
    serializer_class =UserSerializer
    def create(self, request, *args, **kwargs):
        data =  request.data
        try:
            user = User.objects.create_user(username=data['username'],password=data['password'])
            serializer =UserSerializer(user,partial=True)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error':'Please be aware'})
    def update(self, request, *args, **kwargs):
        user  =  self.get_object()
        data = request.data
        user.username = data.get('username',user.username)
        user.password = data.get('password',user.password)
        user.save()
        serializer = UserSerializer(user,partial=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
class LoginAPIView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)