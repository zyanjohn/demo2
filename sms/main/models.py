from django.db import models

# Create your models here.



class Batch(models.Model):

    Batch_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Batch_name

class Department(models.Model):
    Dept_name=models.CharField(max_length=100)

    def __str__(self) :
        return self.Dept_name


class Semester(models.Model):
    sem=models.CharField(max_length=100)
    
    def __str__(self):
        return self.sem

class Student(models.Model):
    student_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,default=1,on_delete=models.CASCADE)
    sem=models.ForeignKey(Semester,default=1,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,default=1,on_delete=models.CASCADE)
