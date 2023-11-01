from rest_framework import serializers

from apps.users.serializers import TeacherSerializer, UserSerializer
from apps.app.models import *
from rest_framework import fields


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']
        read_only_fields = ['id']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']
        


class GroupSerializer(serializers.ModelSerializer):
    day = serializers.JSONField()
    class Meta:
        model = Group
        fields = ['id','user','course','room','teacher','name','course_name','room_name','teacher_name','user_name','status','start','finish','start_lesson','finish_lesson','day','cost']
    

class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['id','student','group','group_name','student_name','group_name','student_name']


class StudentSerializer(serializers.ModelSerializer):
    # groups = StudentGroupSerializer(many=True, read_only=True,source='group_name',)
    groups = StudentGroupSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','phone','first_added','student_id','groups']



class FinanceInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceInput
        fields = ['id','student','group','cost','date','pay_day','chek_id','next_pay','status','student_name','student_group','desc']
        
class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id','name']
        
    

class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = ['id','classes','student']
        

class ClassRoomSerializer(serializers.ModelSerializer):
    classes = ClassStudentSerializer(many=True, read_only=True)
    class Meta:
        model = ClassRoom
        fields = ['id','type','name','desc','students','classes']

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendece
        fields = ['id','student','student_name','student_group','group','classes','status','date','desc']






