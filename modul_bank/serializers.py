import json
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import serializers
from ModulBankIntegration.celery import app
from modul_bank.models import Account, Company, Operation, Bank


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

    def create(self, validated_data):
        """Create Bank and start tasks
         of downloading data and updating it (adding)"""
        bank = Bank.objects.create(**validated_data)

        app.send_task(
            'modul_bank.tasks.first_add_bank',
            kwargs={'bank_id': bank.id},
        )

        schedule_first_upload, _ = CrontabSchedule.objects.get_or_create(
            minute='0',
            hour='4',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )

        PeriodicTask.objects.create(
            crontab=schedule_first_upload,
            name=f'{bank.id}-{bank.title}: Regular upload data',
            task='modul_bank.tasks.regular_unloading_operations',
            kwargs=json.dumps(
                {'bank_id': bank.id},
            ),
        )

        return bank
