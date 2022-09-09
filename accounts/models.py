from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify



class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur") 
        email = self.normalize_email(email) 
        username = self.model.normalize_username(username)     
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, username, email=None, password=None):
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)  
        user = self.create_user(username=username, email=email,  password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
permi = [
    ('Commercial', 'Commercial'),
    ('Partenaire', 'Partenaire'),
    ('Responsable', 'Responsable'),
]

class MyUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50) 
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    email = models.EmailField(max_length=30, blank=False)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    adresse = models.CharField(max_length=200)
    CodePostal = models.IntegerField(null=True, blank=True)    
    ville = models.CharField(max_length=20)
    Groupe = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True, blank=True)
    permission = models.CharField(choices= permi, max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):       
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)            
        super().save(*args, **kwargs)   

    
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

class option(models.Model):
    slug = models.SlugField(max_length=20)
    description = models.CharField(max_length=200)
    

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.slug


class structure(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.SET_NULL,null=True, blank=True)
    actif = models.BooleanField(default=True)
    part = models.ForeignKey('accounts.partenaire', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=20)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='salle', null=True, blank=True)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 10, unique = True)
    piscine = models.BooleanField(default=False)
    haman = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)  
    membre = models.IntegerField(default=0)
    option = models.ManyToManyField(option, blank=True)
 
    def __str__(self):       
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.part)
        super().save(*args, **kwargs)
   

class partenaire(models.Model):
    salle = models.ForeignKey(structure, on_delete = models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=20)
    actif = models.BooleanField(default=True)
    ville = models.CharField(max_length=15)
    description = models.CharField(max_length=70)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 10)
    photo = models.ImageField(upload_to='ville', null=True, blank=True) 
    resp = models.OneToOneField(MyUser, on_delete = models.SET_NULL,null=True, blank=True)
    option = models.ManyToManyField(option, blank=True)

    def __str__(self):
        return self.ville
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ville)
        super().save(*args, **kwargs)
    
  

   