from django.contrib import admin
from website.models import Employees, LegalServices, Clients


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass


@admin.register(LegalServices)
class Services(admin.ModelAdmin):
    pass


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    pass