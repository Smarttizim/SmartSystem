from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.app.views import *
from apps.users.views import *
from apps.app.views import *
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('director', DirectorViewset, basename='director')
router.register('teacher', TeacherViewset, basename='teacher')
router.register('manager', ManagerViewset, basename='manager')
router.register('user', UserViewset, basename='user')


router.register('course', CourseViewSet, basename='course')
router.register('room', RoomViewSet, basename='room')
router.register('student', StudentViewSet, basename='student')
router.register('studentgroup', StudentgroupViewSet, basename='student_group')
router.register('groups', GroupViewSet, basename='groups')
router.register('financeinput', FinanceInputViewSet, basename='financeinput')
router.register('attendence', AttendenceViewSet, basename='attendence')

router.register('classtype', ClassTypeViewSet, basename='classtype')
router.register('classroom', ClassRoomViewSet, basename='classroom')
router.register('classtudent', ClassStudentViewSet, basename='classtudent')



# router.register('statistic-group', StatisticPostViewset, basename='statistic-group')

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    
]