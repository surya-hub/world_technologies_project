from django.db import models

class DemoRegister(models.Model):
    CHOICES=(('Select Course','Select Course'),('PYTHON','PYTHON'),('JAVA','JAVA'),('.NET','.NET'),('DJANGO','DJANGO'),
    ('FLASK','Flask'),('REST API','REST API'),('DATA SCIENCE','DATA SCIENCE'),('ML','ML'),('DL','DL'),('AI','AI'))
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100,choices=CHOICES,default='Select Course')
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.course
class Courses(models.Model):
    cname=models.CharField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    duration=models.IntegerField()
    start_date=models.DateTimeField()
    content = models.FileField(upload_to='files')
    photo = models.ImageField(upload_to='images')

