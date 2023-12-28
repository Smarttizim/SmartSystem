from django.contrib import admin
from apps.app.models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name', 'phone']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ['group',]
    search_fields = ['name', 'phone']

@admin.register(FinanceInput)
class FinanceInputAdmin(admin.ModelAdmin):
    list_display = [ 'group', 'cost','chek_id','status','pay_day']
    list_filter = [  'group']
    search_fields = [ 'group']
    
    
@admin.register(ClassType)
class ClassTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ClassStudent)
class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']
    
@admin.register(Attendece)
class AttendeceAdmin(admin.ModelAdmin):
    list_display = ['group','status']
    search_fields = ['group']