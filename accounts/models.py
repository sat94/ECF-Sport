from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur") 
        email = self.normalize_email(email)      
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, username, email=None, password=None):
        email = self.normalize_email(email)
        user = self.create_user(username=username, email=email,  password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

option = [('1', 'Option 1'),
          ('2', 'Option 2'),
          ('3', 'Option 3'),
          ]

class MyUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=20)
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=False)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    adresse = models.CharField(max_length=200)
    abonnement = models.CharField(max_length=8, choices=option, default="option 1")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
   
    
    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
