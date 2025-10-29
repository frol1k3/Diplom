from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    speciality = models.TextField(verbose_name="Специальность")
    work_experience = models.IntegerField(verbose_name="Стаж работы")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

class Patient(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    surename = models.CharField(max_length=20, verbose_name="Фамилия")
    login = models.TextField(verbose_name="Логин")
    password = models.TextField(verbose_name="Пароль")

    def __str__(self):
        return self.login
    
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"