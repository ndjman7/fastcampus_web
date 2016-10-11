from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Studnet(Person):
    year = models.CharField(max_length=20)

class China_Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Coffee(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
