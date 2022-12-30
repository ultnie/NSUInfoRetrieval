from django import forms
from django.forms import ModelChoiceField

from . import models


class UniversityForm(forms.Form):
    fullName = forms.CharField(max_length=255)
    shortName = forms.CharField(max_length=45)
    creationDate = forms.DateField()


class StudentForm(forms.Form):
    lastName = forms.CharField(max_length=45)
    firstName = forms.CharField(max_length=45)
    patronymic = forms.CharField(max_length=45)
    birthDate = forms.DateField()
    university = ModelChoiceField(queryset=models.universities.objects.all())
    year = forms.IntegerField()