from django.contrib import admin

from modul_bank.models import Company, Bank, Account, Operation


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass
