from django.db import models
from account.models import *
from EmpJobs.models import *
# Create your models here.

class InterviewShedule(models.Model):
    choice={
        ("Upcoming","Upcoming"),
        ("Selected","Selected"),
        ("Canceled","Canceled"),
        ("Rejected","Rejected"),
        ("You missed","You missed")
    }
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE,related_name="candidate")
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE,related_name="employer")
    job = models.ForeignKey(Jobs, on_delete = models.CASCADE,related_name="job")
    date = models.DateTimeField()
    selected = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=20,choices=choice, default="Upcoming")