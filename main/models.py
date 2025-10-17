from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    speciality = models.TextField(verbose_name="Специальность")
    work_experience = models.IntegerField(verbose_name="Стаж работы")

