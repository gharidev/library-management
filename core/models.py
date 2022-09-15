from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    """
    Custom auth user model.
    """
    class Types(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        STUDENT = 'STUDENT', 'Student'
    
    type = models.CharField('Type', max_length=50, choices=Types.choices, default=Types.STUDENT)


# PROXY MODEL MANAGERS

class AdminManager(UserManager):
    """
    User manager for `Admin` user.
    """
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)

class StudentManager(UserManager):
    """
    User manager for `Student` user.
    """
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

# PROXY MODELS
class Admin(User):
    """
    Proxy user model for admin.
    """

    class Meta:
        proxy = True

    objects = AdminManager()

class Student(User):
    """
    Proxy user model for student.
    """

    class Meta:
        proxy = True

    objects = StudentManager()

class Book(models.Model):
    """
    Book model.
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    total_count = models.IntegerField(default=1)
    
    @property
    def available_count(self):
        history_set = self.checkouthistory_set.filter(returned_at__isnull=True).all()
        total = self.total_count
        for history in history_set:
            total -= history.quantity
        return total
    
    def __str__(self) -> str:
        return self.title

class CheckOutHistory(models.Model):
    """
    Checkout history model.
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    returned_at = models.DateTimeField(blank=True, null=True)
