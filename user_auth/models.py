from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(unique=True, max_length=150, default="")
    mobile = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    hobby = models.CharField(max_length=100, blank=True)
    education_details = models.CharField(max_length=100, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "registration"
