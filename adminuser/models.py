from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser,PermissionsMixin
)
class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,type,username, password=None,):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name=last_name,
            username=username,
            type=type
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password,username):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.type = "staff"
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,username):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.staff = True
        user.username = username
        user.is_admin=True
        user.is_superuser = True
        user.type = "admin"
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    # required
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(verbose_name='E-Mail-Adresse', max_length=255, unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name='aktives Konto', default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='Vorname', max_length=55)
    last_name = models.CharField(verbose_name='Nachname', max_length=55)

    # additional
    password = models.CharField(verbose_name='Password', max_length=500)
    profilepic = models.ImageField(verbose_name='Profilpic', upload_to='profilepics/', max_length=100, null=True,
                                   blank=True)
    type = models.CharField(max_length=20,choices=(('admin','Admin'),('student','Student'),('teacher','Teacher'),('staff','Staff')),default='Teacher')
    school = models.CharField(max_length=200)
    section=models.CharField(max_length=20)
    subject = models.CharField(max_length=40)
    designation = models.CharField(max_length=30)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password','email','first_name','last_name','type']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return self.username


