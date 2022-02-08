import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

from aatr.api.common.utils import gen_session_token


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampedModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class UserManager(BaseUserManager):
    def create_user(self, email, name, terms, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            terms=terms,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, ProjectModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, default='no_name')
    terms = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class Session(ProjectModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='sessions',
    )

    token = models.TextField(
        default=gen_session_token,
        unique=True,
    )

    last_active = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
