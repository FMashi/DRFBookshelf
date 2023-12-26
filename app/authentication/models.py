from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


GENDER = [
    ('M', _('Male')),
    ('F', _('Female')),
]

class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)
   
   def __str__(self):
       return self.username
   
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.Profile.save()
    
class Profile(models.Model): 
    # faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE) 
    # semester = models.ForeignKey(Semester, on_delete=models.CASCADE) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    gender = models.CharField(max_length=1, choices=GENDER) 
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    
    contact_no = models.CharField(max_length=14)
    identification_no = models.IntegerField()
    registration_no = models.IntegerField()
    page_no = models.IntegerField()
    original_address = models.CharField(max_length=50)
    current_address = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True) 
    signature = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
