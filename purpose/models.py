from django.db import models
from django.contrib.auth.models import User

project_type=(
    (0,'mini project'),
    (1,'main project'),
    (2,'live project')
)
class Master(models.Model):
    created_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    class Meta:
        abstract=True
class Course(Master):
    Course=models.CharField(max_length=220)
    def __str__(self):
        return self.Course
class Technology(Master):
    technology=models.CharField(max_length=200)
    def __str__(self):
        return self.technology
class Project_Ideas(Master):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    project_type=models.IntegerField(choices=project_type,null=False,blank=False)
    Description=models.TextField()
    technology=models.ManyToManyField(Technology,blank=True)
    project_title=models.CharField(max_length=300)
    def __str__(self):
        return self.project_title






