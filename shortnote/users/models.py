from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class AppUserManager(BaseUserManager):
    def create_user(self, email, username, role, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=Role.objects.get(pk=role)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            username,
            role=Role.get_admin_role(),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Role(models.Model):
    rolename = models.CharField(max_length=20, unique=True)

    @staticmethod
    def get_admin_role():
        return Role.objects.filter(rolename='admin')

    def __str__(self):
        return self.rolename


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, verbose_name='Username', null=False)

    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    role = models.ForeignKey(Role, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
