from django.db import models
from apps.users.models import Teacher, User
# Create your models here.
from datetime import time, date
from django.utils import timezone

# Courses 

class Course(models.Model):
    name = models.CharField(max_length=100, help_text="Enter course name", verbose_name="Course name")
    # @property 
    # def group_count(self):
    #     results = self.groups.all()
    #     return len(results)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Courses"
        verbose_name_plural = "Courses"

# Rooms

class Room(models.Model):
    name = models.CharField(max_length=500, verbose_name="Room name")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Rooms"
        verbose_name = " Room "
        verbose_name_plural = " Rooms "

# Students class

class Student(models.Model):
    name = models.CharField(max_length=500, verbose_name="Student name")
    phone = models.CharField(max_length=9, verbose_name="Student phone", null=True, blank=True)
    first_added = models.DateField(null=True, blank=True)
    student_id = models.IntegerField(unique=True, null=True, blank=True)
    @property
    def student_id(self):
        return self.id + 10000

    
    def __str__(self):
        return f"{self.name} {self.student_id}"
    class Meta:
        db_table = "Student"
        verbose_name = " Student "
        verbose_name_plural = " Students "
        
# Group class

class Group(models.Model):
    DAY = [
        ('Du', 'Du'),
        ('Se', 'Se'),
        ('Chor', 'Chor'),
        ('Pay', 'Pay'),
        ('Ju', 'Ju'),
        ('Shan', 'Shan'),
        ('Yak', 'Yak')
    ]
    name = models.CharField(max_length=100, verbose_name="Group name")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='group_course')
    day = models.CharField(max_length=100, choices=DAY, null=True, blank=True)
    cost = models.FloatField(verbose_name="Cost", help_text="Enter cost", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='groups_rooms')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True, related_name='teacher')
    start = models.DateField(null=True, blank=True)
    finish = models.DateField(null=True, blank=True)
    start_lesson = models.TimeField(null=True, blank=True)
    finish_lesson = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='post_users')
    def save(self, *args, **kwargs):
        self.start_lesson = time(hour=self.start_lesson.hour, minute=self.start_lesson.minute)
        self.finish_lesson = time(hour=self.finish_lesson.hour, minute=self.finish_lesson.minute)
        return super().save(*args, **kwargs)
    @property
    def status(self):
        today = timezone.localdate()
        if today < self.start:
            return "waiting"
        elif self.start <= today <= self.finish:
            return "active"
        else:
            return "ended"
        
    def course_name(self):
        return self.course.name
    def room_name(self):
        return self.room.name
    def teacher_name(self):
        return self.teacher.username
    def user_name(self):
        return self.user.username
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Group"  # noqa
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ['-id']
        
        
class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')
    @property
    def group_name(self):
        return self.group.name
    @property
    def student_name(self):
        return self.student.name
    def __str__(self):
        return self.student.name
    class Meta:
        db_table = "StudentGroup"  # noqa
        verbose_name = "Student Group"
        verbose_name_plural = "Student Groups"
        ordering = ['-id']
        
        

class FinanceInput(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, blank=True)
    cost = models.FloatField( null=True, blank=True)
    date = models.DateField()
    next_pay = models.DateField()
    chek_id = models.FloatField(null=True, blank=True, unique=True)
    desc = models.TextField(null=True, blank=True)
    

    @property
    def status(self):
        today = timezone.localdate()
        if self.next_pay < today:
            return f"❌ Qarzdorlik"
        else:
            return "✔ To'langan"
    @property
    def pay_day(self):
        today = timezone.localdate()
        if (self.next_pay - today).days < 0:
            return f"{0 - (self.next_pay - today).days}"
        else:
            return f"{(self.next_pay - today).days}"
    
    @property
    def chek_id(self):
        return 100000 + self.id
    
    @property
    def student_name(self):
        return self.student.name
    
    @property
    def student_group(self):
        return self.group.group.name
    
    def __str__(self):
        return f"Aziz"
    
    
    
    class Meta:
        db_table = "FinanceInput"  # noqa
        verbose_name = "Finance Input"
        verbose_name_plural = "Finance Inputs"
        ordering = ['-id']
        

        
        
# ClassRoom table

class ClassType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"  

class ClassRoom(models.Model):
    type = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"  
    
class ClassStudent(models.Model):
    classes = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')
    @property
    def class_name(self):
        return self.classes.name
    @property
    def student_name(self):
        return self.student.name
    def __str__(self):
        return self.student.name
    class Meta:
        db_table = "ClassStudent"  # noqa
        verbose_name = "Class Student"
        verbose_name_plural = "Class Student"
        ordering = ['-id'] 
        
        
        
# Attendence table


class Attendece(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, blank=True)
    classes = models.ForeignKey(ClassStudent, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    status = models.BooleanField()
    desc = models.TextField(null=True, blank=True, help_text='Sababsiz')
    
    @property
    def student_name(self):
        return self.student.name
    
    @property
    def student_group(self):
        return self.group.group.name
    
    def __str__(self):
        return f"Aziz"  
    class Meta:
        db_table = "Attendece"  # noqa
        verbose_name = "Attendece"
        verbose_name_plural = "Attendece"
        ordering = ['-id']