from django.db import models

# Create your models here.

class Hh_vacancy(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    salary_from = models.CharField(max_length=20,blank=True,null=True)
    salary_to = models.CharField(max_length=20,blank=True,null=True)
    currency = models.CharField(max_length=20,blank=True,null=True)
    gross = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    area_name = models.CharField(max_length=20,blank=True,null=True)
    responsibility = models.TextField(blank=True,null=True)
    requirement = models.TextField(blank=True,null=True)
    vacancy_id = models.IntegerField(blank=True,null=True)
    employer_name = models.CharField(max_length=20,blank=True,null=True)
    employer_id = models.CharField(max_length=20,blank=True,null=True)

class Vacancy(models.Model):
    vacancy_id = models.IntegerField(blank=True,null=True)
    salary_from = models.CharField(max_length=20,blank=True,null=True)
    salary_to = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    responsibility = models.TextField(blank=True,null=True)
    requirement = models.TextField(blank=True,null=True)
    experience = models.CharField(max_length=20,blank=True,null=True)


class Responsibility(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Requirement(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Сompanies(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
