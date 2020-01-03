from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class ONEAccountManager(BaseUserManager):
    def _create_user(self, email, password, user_type, first_name, last_name):
        #Creates and saves a User with the given email and password.
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type,
                        first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, user_type, first_name, last_name):
        return self._create_user(email=email, password=password, user_type=user_type,
                                first_name=first_name, last_name=last_name)

    def create_superuser(self, email, password, user_type, first_name, last_name):
        return self._create_user(email=email, password=password, user_type=ONEUser.ADMIN,
                                first_name=first_name, last_name=last_name)


class ONEUser(AbstractBaseUser, PermissionsMixin):
    NO_ACCESS = 0
    AGENT = 1
    DIRECTOR = 2
    MANAGER = 3
    ADMIN = 4        
    USER_TYPE_CHOICES = [(NO_ACCESS,'No_access'),
                        (AGENT,'Agent'),
                        (DIRECTOR,'Director'),
                        (MANAGER,'Manager'),
                        (ADMIN,'Admin')
                        ]
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES, default = NO_ACCESS)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.TimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['user_type', 'first_name', 'last_name']

    objects = ONEAccountManager()

    def __str__(self):
        return self.email

    def get_email_field_name(self):
        return self.USERNAME_FIELD

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.user_type != self.NO_ACCESS

    @property
    def is_no_access(self):
        return self.user_type == self.NO_ACCESS

    @property
    def is_agent(self):
        return self.user_type == self.AGENT

    @property
    def is_director(self):
        return self.user_type == self.DIRECTOR

    @property
    def is_manager(self):
        return self.user_type == self.MANAGER

    @property
    def is_admin(self):
        return self.user_type == self.ADMIN
