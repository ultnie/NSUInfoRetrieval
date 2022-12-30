from django.contrib import admin
from django import forms
from django.forms import ModelChoiceField

from .models import universities, students
# Register your models here.


class UniModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.shortName+f" ({obj.id})"


class UniversityForm(forms.ModelForm):
    class Meta:
        model = universities
        fields = ['id', 'fullName', 'shortName', 'creationDate']


class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['id', 'lastName', 'firstName', 'patronymic', 'birthDate', 'university', 'year']


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'shortName', 'creationDate')
    form = UniversityForm


admin.site.register(universities, UniversityAdmin)


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm

    @admin.display(description='university')
    def uni_short_name(obj):
        return ("%s" % (obj.university.shortName))

    list_display = ('id', 'lastName', 'firstName', 'patronymic', 'birthDate', uni_short_name, 'year')


admin.site.register(students, StudentAdmin)
