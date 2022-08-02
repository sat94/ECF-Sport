from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.db import models
from django.core.validators import RegexValidator



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

class MyUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    entreprise = models.OneToOneField('accounts.structure', max_length=20, on_delete=models.SET_NULL,null=True, blank=True)
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=False)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    adresse = models.CharField(max_length=200)
    CodePostal = models.IntegerField(null=True, blank=True)
    partenaire = models.OneToOneField('accounts.partenaire', max_length=20, on_delete=models.SET_NULL,null=True, blank=True)
    ville = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    Groupe = models.ManyToManyField(Group)

    
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

ville =  [('Paris', 'Paris'),
          ('Bordeaux', 'Bordeaux'),
          ('Nice', 'Nice'),
          ('Lille', 'Lille'),
          ('Marseille', 'Marseille'),
          ('Montpellier', 'Montpellier'),
          ('Brest', 'Brest'),
          ('Lyon', 'Lyon'),
          ('Strasbourg', 'Strasbourg'),
          ('Nantes', 'Nantes'),  
          ('Toulouse', 'Toulouse'),
          ('Nîmes', 'Nîmes'),    
          ('Rennes', 'Renne'),
          ('Angers', 'Angers'), 
          ('Limoges', 'Limoges'), 
          ('Tours', 'Tours'), 
          ]


class structure(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.SET_NULL,null=True, blank=True)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)
    part = models.ForeignKey('accounts.partenaire', on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='salle', null=True, blank=True)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 16, unique = True)
    piscine = models.BooleanField(default=False)
    haman = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)  
    membre=models.IntegerField(default=0)
    bails = models.BooleanField(default=False)
    fourni = models.BooleanField(default=False) 
    banque = models.BooleanField(default=False) 
    compta = models.BooleanField(default=False)
    assistance = models.BooleanField(default=False) 
    kine = models.BooleanField(default=False) 
    Accompagne = models.BooleanField(default=False) 
    coach = models.BooleanField(default=False) 
    promotion = models.BooleanField(default=False) 
    bar = models.BooleanField(default=False) 
    planing = models.BooleanField(default=False) 
    mailing = models.BooleanField(default=False) 
    member = models.BooleanField(default=False) 
    entretiens = models.BooleanField(default=False) 

 
    def __str__(self):
        return self.nom


   

class partenaire(models.Model):
    salle = models.ForeignKey(structure, on_delete = models.SET_NULL, null=True, blank=True)
    actif = models.BooleanField(default=True)
    ville = models.CharField(choices = ville, max_length=15, default="Paris")
    email = models.EmailField ( max_length=25, null=False)
    description = models.CharField(max_length=70)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 16)
    photo = models.ImageField(upload_to='ville', null=True, blank=True) 

    def __str__(self):
        return self.ville


   