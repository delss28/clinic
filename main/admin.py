from django.contrib import admin
from .models import Doctor, Service, Sick_list, User, Reception

admin.site.register(Doctor)
# admin.site.register(Service)
admin.site.register(Sick_list)
admin.site.register(User)
admin.site.register(Reception)

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


