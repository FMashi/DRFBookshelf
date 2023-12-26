from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from book.models import Faculty, Copy


GENDER = [
    ('M', _('Male')),
    ('F', _('Female')),
]

class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)
   
   def __str__(self):
       return self.username
   

   
class Cities(models.Model):
    city = models.CharField(max_length=80)
    city_person = models.CharField(max_length=80)


class Semesters(models.Model):
    semester = models.CharField(max_length=30)
    semester_person=models.CharField(max_length=30)

class Desposites(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    copy= models.ForeignKey(Copy, on_delete=models.CASCADE) 
    issue_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    
    def __str__(self):
        return f"{self.user} - {self.copy} - {self.issue_date}"

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"
     
class Profile(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True) 
    semester = models.ForeignKey(Semesters, on_delete=models.SET_NULL, null=True) 
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER) 
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    
    contact_no = models.CharField(max_length=14)
    identification_no = models.IntegerField(null=True)
    registration_no = models.IntegerField(null=True)
    page_no = models.IntegerField(null=True)
    original_address = models.CharField(max_length=50)
    current_address = models.CharField(max_length=50)

    signature = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
