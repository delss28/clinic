from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=50)
    work_experience = models.IntegerField()
    phone = models.CharField(max_length=30)
    mail = models.CharField(max_length=50)
    room_number = models.IntegerField()
    salary = models.DecimalField(max_digits=10,
                                 decimal_places=2)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.full_name


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    id_doctor = models.ForeignKey(Doctor,
                                  related_name='id_doctors',
                                  on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200,unique=True, blank=True, null=True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ("id",)

    def __str__(self):
        return self.title

class Sick_list(models.Model):
    complaints = models.CharField(max_length=150)
    end_date_of_treatment = models.DateField()

    class Meta:
        verbose_name = 'Больничный лист'
        verbose_name_plural = 'Больничные листы'

    def __str__(self):
        return self.complaints


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    dateOfBirth = models.DateField()
    number = models.CharField(max_length=30)
    mail = models.CharField(max_length=50)
    id_sick_list = models.ForeignKey(Sick_list,
                                     related_name='id_sick_lists',
                                     on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    confirm = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Reception(models.Model):
    id_service = models.ForeignKey(Service,
                                   related_name='id_services',
                                   on_delete=models.CASCADE, null=True)
    id_client = models.ForeignKey(User,
                                  related_name='id_users',
                                  on_delete=models.CASCADE, null=False)
    reception_date = models.DateTimeField(blank=True, null=True)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'

    def __str__(self):
        return self.id_client