from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=100)
    salary = models.IntegerField()
    address = models.CharField(max_length=200)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" %(self.fname, self.salary, self.city_name)