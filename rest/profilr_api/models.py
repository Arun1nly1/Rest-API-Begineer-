from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for User Profiles'''
    def create_user(self,email,name,password=None):
        '''Create a new user Profile'''
        if not email:
            raise ValueError("user must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name )

        user.set_password(password)
        '''To tell django use thus database'''

        user.save(using = self._db)

        return user

    def create_superuser(self,email,name,password):
        '''Create and save a new superuser with given details'''
        user = self.create_user(email,name,password)
        '''Automatically created by PermissionMixin'''
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 255,unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default =True )
    is_staff = models.BooleanField(default =False )

    objects = UserProfileManager ()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email



class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status_text
