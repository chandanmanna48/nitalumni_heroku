from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CLUserManager
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
   # user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    #cuser = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    regdno = models.CharField(max_length=70,null =False,blank =False)
    passout_year = models.CharField(max_length=70,null = False,blank = False)
    branch = models.CharField(max_length=70,blank=False)
    profession = models.CharField(max_length=70,blank=True)
    company = models.CharField(max_length=70,blank=True)
    work_location = models.CharField(max_length=70,blank=True)
    designation = models.CharField(max_length=70,blank=True)
    work_country = models.CharField(max_length=70,blank=True)
    contactno = models.CharField(max_length=70,blank =True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',default="user.socialaccount_set.all.0.get_avatar_url")

    street_name = models.CharField(max_length=70,blank=True)
    street_number = models.CharField(max_length=70,blank=True)
    city = models.CharField(max_length=70,blank=True)
    state = models.CharField(max_length=70,blank=True)
    district = models.CharField(max_length=70,blank=True)
    country = models.CharField(max_length=70,blank=True)
    date_created = models.DateTimeField(default = timezone.now)
    facebook_username = models.CharField(max_length=50,null=True,blank=True)
    linkedin_resource_id = models.CharField(max_length=50,null=True,blank=True)
    twitter_username = models.CharField(max_length=50,null=True,blank=True)
    
    '''
    @receiver(post_save, sender = User)
    def create_user_profile(sender ,instance,created,**kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save() '''

    def __str__(self):

        return self.regdno

class Gallery(models.Model):
    email = models.EmailField(null=True,blank=True)
    title = models.CharField(max_length = 100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    images = models.FileField(upload_to='gallery')
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    profile_image_url = models.URLField(null=True,blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    first_visit = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_master = models.BooleanField(default = False)
    is_approved = models.BooleanField(default = False)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    gallery = models.ForeignKey(Gallery,on_delete=models.SET_NULL,null=True,blank=True)

    def first_visited(self):
        self.first_visit = False
        self.save()

    def make_master(self):
        self.is_master = True
        self.save()

    def make_approve(self):
        self.is_approved = True
        self.save()


    objects = CLUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def get_email(self):
        return self.email

    def get_full_name(self):
        fullname = '%s %s' %(self.first_name,self.last_name)
        return fullname.strip()

    def get_short_name(self):
        return self.first_name








# Create your models here.









