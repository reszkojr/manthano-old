from django.db import models
from django.db.models import CASCADE

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.core.mail import send_mail

from datetime import timezone


class StudentManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, is_active, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser, is_active=is_active, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
    
        user.is_active=True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', max_length=32)
    first_name = models.CharField('First name', max_length=32)
    last_name = models.CharField('Last name', max_length=255)
    email = models.EmailField('Email address', max_length=255, unique=True)
    is_admin = models.BooleanField('Admin status', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    
    classroom = models.ForeignKey("main.Classroom", on_delete=models.CASCADE, related_name='classrooms', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = StudentManager()

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'

    def get_full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()
    
    def get_short_name(self):
        return self.first_name
    
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])