from statistics import mode
from django.db import models

# Create your models here.

JOB_STATUS = (
    ("APPLIED", "APPLIED"),
    ("SCREENING", "SCREENING"),
    ("FIRST INTERVIEW", "FIRST INTERVIEW"),
    ("ON PROCESS", "ON PROCESS"),
    ("OFFER", "OFFER")
)


class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_site = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20, choices=JOB_STATUS, default='APPLIED')

    def __str__(self):
        return f'{self.company}-{self.job_title}'
