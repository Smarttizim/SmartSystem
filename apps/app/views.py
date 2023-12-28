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
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50000

    def get_paginated_response(self, data):
        return Response({
            "page_size": self.page_size,
            "total_objects": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "current_page_number": self.page.number,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })


class CustomPaginationMixin:
    pagination_class = BasePagination


class CourseViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RoomViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class StudentViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','phone','first_added','student_id')
    filterset_fields = ('status', )
    filterset_class = StudentFilter
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return StudentDetailSerializer  # Serializer for Student/id
    #     return StudentDetailSerializer


class StudentgroupViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = StudentGroup.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','phone','first_added','student_id')
    # filterset_class = StudentGroupFilter
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer

   
class GroupViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = Group.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    
class AllGroupViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = Group.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FinanceInputViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = FinanceInput.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name','day','cost','room','teacher','start','finish','start_lesson','finish_lesson')
    filterset_fields = ('status', )
    filterset_class = FinanceInputFilter
    queryset = FinanceInput.objects.all()
    serializer_class = FinanceInputSerializer
    


class ClassTypeViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
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
    
    
class ClassStudentViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = ClassStudent.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name')
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer
    

class AttendenceViewSet(CustomPaginationMixin, viewsets.ModelViewSet):
    objects = Attendece.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('status','student')
    filterset_fields = ('status', )
    filterset_class = AttendenceFilter
    queryset = Attendece.objects.all()
    serializer_class = AttendenceSerializer