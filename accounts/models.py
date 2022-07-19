from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError("Vous devez entrer un mail valide") 
        email = self.normalize_email(email)      
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, username,  email=None, password=None):
        email = self.normalize_email(email)
        user = self.create_user(username=username, email=email,  password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    entreprise = models.OneToOneField('accounts.structure', max_length=20, on_delete=models.SET_NULL,null=True)
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=False)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    adresse = models.CharField(max_length=200)
    CodePostal = models.IntegerField(default=0)
    partenaire = models.OneToOneField('accounts.partenaire', max_length=20, on_delete=models.SET_NULL,null=True)
    ville = models.CharField(max_length=20, default=0)
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

option = [('1', 'Option 1'),
          ('2', 'Option 2'),
          ('3', 'Option 3'),
          ]

ville =  [('Paris', 'Paris'),
          ('Bordeaux', 'Bordeaux'),
          ('Nice', 'Nice'),
          ('Lille', 'Lille'),
          ('Marsielle', 'Marseille'),
          ('Montpellier', 'Montpellier'),
          ('Brest', 'Brest'),
          ('Lyon', 'Lyon'),
          ('Strabourg', 'Strabourg'),
          ('Nantes', 'Nantes'),          
          ]

class structure(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.SET_NULL,null=True)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='salle', null=True, blank=True)
    option = models.CharField ( choices = option, max_length=10, default='option 1')
    numberPhone = models.IntegerField()
    piscine = models.BooleanField(default=False)
    haman = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    

class partenaire(models.Model):
    salle = models.OneToOneField(structure, on_delete = models.CASCADE)
    ville = models.CharField(choices = ville, max_length=15, default="Paris")
    email = models.EmailField ( max_length=25)
    numberPhone = models.IntegerField()
    numberThec  = models.IntegerField()

    def __str__(self):
        return self.ville

class option1(models.Model):
    bail = models.BooleanField()
    fournisseur = models.BooleanField()
    banque = models.BooleanField()
    chiffre = models.BooleanField()
    assistance = models.BooleanField()
   

class option2(models.Model):
    kine = models.BooleanField(default=False)
    Accompagne = models.BooleanField(default=False)
    coach = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)
    planing = models.BooleanField(default=False)


class option3(models.Model):
    bar = models.BooleanField(default=False)
    mailing = models.BooleanField(default=False)
    piscine = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    entretiens = models.BooleanField(default=False)
   