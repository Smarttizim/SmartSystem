from django_filters import rest_framework as filters
from apps.app.models import *
from django.db.models import  fields
from apps.app.models import *
import django_filters
from django.db.models import F, Q, Sum, ExpressionWrapper



class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = ['id','name','phone']


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = ['id','day','name','course','cost','room','teacher','start','finish','finish_lesson','user']

class FinanceInputFilter(django_filters.FilterSet):
    STATUS_CHOICES = (
        ("To'langan", "To'langan"),
        ('Qarzdorlik', 'Qarzdorlik'),
        ("To'langan","To'langan"),
    )
    student = django_filters.CharFilter(field_name='student', lookup_expr='icontains')
    date = django_filters.CharFilter(field_name='date', lookup_expr='icontains')
    status = django_filters.CharFilter(method='filter_status')

    # def filter_status(self, queryset, name, value):
    #     today = timezone.localdate()
    #     queryset = queryset.annotate(
    #         total2=ExpressionWrapper(
    #             (F('cost') - F('ad_payment')) + (F('surcharge') * F('dedline')),
    #             output_field=fields.FloatField()
    #         ),
    #         total_payments=Sum('payments__summa'),
    #         debt_f=F('total2') - F('total_payments')
    #     )
    #     if value == "To'langan":
    #         return queryset.filter(debt_f=0)
    #     elif value == "Qarzdorlik":
    #         return queryset.filter(Q(Q(debt_f__gt=0) | Q(debt_f=None)) & Q(next_pay__lt=today))
    #     elif value == "To'langan":
    #         return queryset.filter(Q(Q(debt_f__gt=0) | Q(debt_f=None)) & Q(next_pay__gte=today))
    #     return queryset
    class Meta:
        model = FinanceInput
        fields = ['student','group','cost','date']
        
        

class AttendenceFilter(filters.FilterSet):
    class Meta:
        model = Attendece
        fields = ['id','status']