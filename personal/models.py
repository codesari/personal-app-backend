from django.db import models



class Department(models.Model):
    department_name=models.CharField(max_length=15)
    how_many_person=models.IntegerField()

    def __str__(self):
        return f'{self.department_name}'


class Personal(models.Model):
    title=models.CharField(max_length=15)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    is_staffed=models.BooleanField()
    did_joined=models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


