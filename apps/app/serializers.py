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
        fields = ['id','user','course','room','teacher','name','start','finish','start_lesson','finish_lesson','day','cost','status']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = instance.course.name if instance.course else None
        representation['user'] = instance.user.username if instance.user else None
        representation['room'] = instance.room.name if instance.room else None
        representation['teacher'] = instance.teacher.username if instance.teacher else None
        return representation
    

class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['id','group']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['student'] = instance.student.name if instance.student else None
        representation['group'] = instance.group.name if instance.group else None
        return representation


class StudentSerializer(serializers.ModelSerializer):
    # groups = StudentGroupSerializer(many=True, read_only=True,source='group_name',)
    groups = StudentGroupSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','phone','first_added','student_id','groups']



class FinanceInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceInput
        fields = ['id','user','student','group','cost','date','pay_day','chek_id','next_pay','status','desc']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username if instance.user else None
        representation['student'] = instance.student.name if instance.student else None
        representation['group'] = instance.group.name if instance.group else None
        return representation
        
class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id','name']
        
    

class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = ['id','classes','student']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = instance.student.name if instance.student else None
        representation['classes'] = instance.classes.name if instance.classes else None
        return representation
        

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id','type','name','desc']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type'] = ClassTypeSerializer(instance=instance.type).data
        return representation

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendece
        fields = ['id','student','group','classes','status','date','desc']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = instance.student.name if instance.student else None
        representation['group'] = instance.group.name if instance.group else None
        return representation




