from django.db import models

# Create your models here.
class teachers(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,null=False)
    subject=models.CharField(max_length=32,null=False)
class classes(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,null=False)
    student_quantity=models.IntegerField(null=False)
class lessons(models.Model):
    id =models.IntegerField(primary_key=True)
    week=models.IntegerField(null=False)
    section=models.IntegerField(null=False)
    teacher=models.ForeignKey(teachers,to_field='id',on_delete=models.CASCADE)
    Class=models.ForeignKey(classes,to_field='id',on_delete=models.CASCADE)
