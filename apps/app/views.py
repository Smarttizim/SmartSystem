from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from apps.app.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import pagination
from rest_framework.response import Response
# Create your views here.
from .models import *
from rest_framework.response import Response
from apps.app.filters import *

class GroupPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = Group.objects.all()
    filterset_class = Group
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class StudentPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = Student.objects.all()
    filterset_class = Student
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class StudentGroupPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = StudentGroup.objects.all()
    filterset_class = StudentGroup
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
    

class FinanceInputPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = FinanceInput.objects.all()
    filterset_class = FinanceInput
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class StudentViewSet(viewsets.ModelViewSet):
    objects = Student.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StudentGroupPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','phone','first_added','student_id')
    filterset_fields = ('status', )
    filterset_class = StudentFilter
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentgroupViewSet(viewsets.ModelViewSet):
    objects = StudentGroup.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','phone','first_added','student_id')
    # filterset_class = StudentGroupFilter
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
   
class GroupViewSet(viewsets.ModelViewSet):
    objects = Group.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = GroupPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    
class AllGroupViewSet(viewsets.ModelViewSet):
    objects = Group.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FinanceInputViewSet(viewsets.ModelViewSet):
    objects = FinanceInput.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = GroupPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = FinanceInputFilter
    queryset = FinanceInput.objects.all()
    serializer_class = FinanceInputSerializer
    


class ClassTypeViewSet(viewsets.ModelViewSet):
    objects = ClassType.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name')
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeSerializer
    
    
class ClassRoomViewSet(viewsets.ModelViewSet):
    objects = ClassRoom.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name')
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    
    
class ClassStudentViewSet(viewsets.ModelViewSet):
    objects = ClassStudent.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name')
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer
    

class AttendenceViewSet(viewsets.ModelViewSet):
    objects = Attendece.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = GroupPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('status','student')
    filterset_fields = ('status', )
    filterset_class = AttendenceFilter
    queryset = Attendece.objects.all()
    serializer_class = AttendenceSerializer