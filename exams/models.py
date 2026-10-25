from django.db import models
from accounts.models import User

from datetime import datetime,time,timedelta
# Create your models here.

class Assessment(models.Model):

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=200)

    LANGUAGE_CHOICES = [
        ('PYTHON', 'Python'),
        ('JAVA', 'Java'),
        ('JAVASCRIPT', 'JavaScript'),
        ('C','c'),
        ('CPP','C++'),
        ('SQL','SQL')
    ]

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    exam_date = models.DateField()

    duration = models.PositiveIntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField(null = True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
    ]

    status = models.CharField(max_length=20,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        end_date_time = datetime.combine(self.exam_date,self.start_time)+timedelta(hours = self.duration)
        self.end_time = end_date_time.time()
        return super().save(*args,**kwargs)

