from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

    


class User(AbstractUser):
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    number = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars_images', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.username
    

#class Reception(models.Model):
#    id_service = models.ForeignKey(Service,
#                                   related_name='id_services',
#                                   on_delete=models.CASCADE, null=True)
#    id_client = models.ForeignKey(User,
#                                  related_name='id_users',
#                                  on_delete=models.CASCADE, null=False)
#    reception_date = models.DateTimeField(blank=True, null=True)
#    confirm = models.BooleanField(default=False)
#
#    class Meta:
#        verbose_name = 'Прием'
#        verbose_name_plural = 'Приемы'
#
#    def __str__(self):
#        return self.id_client