
from django.db import models

class Student(models.Model):
    Add = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        
    )

    admission_no = models.CharField(max_length=10,blank=True)
    full_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(blank=False,max_length=100)
    age = models.IntegerField()
    class_level = models.CharField(max_length=50, choices=Add)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    marklist = models.FileField(upload_to='marklists/',null=True,blank=True)

    def __str__(self):
        return self.full_name
