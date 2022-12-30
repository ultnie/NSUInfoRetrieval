from django.db import models


# Create your models here.
class universities(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255)
    shortName = models.CharField(max_length=45)
    creationDate = models.DateField()
    def __str__(self):return self.shortName + f" (id: {self.id})"


class students(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    birthDate = models.DateField()
    university = models.ForeignKey(universities, on_delete=models.CASCADE, null=True)
    year = models.IntegerField()