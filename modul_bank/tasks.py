from celery import shared_task
from django.db import transaction
from api_module_bank import ClientApi
from api_schema import OperationSchema
from modul_bank.models import Company, Account, Operation
from modul_bank.serializers import (CompanySerializers, AccountSerializers,
                                    OperationSerializers)


@shared_task
def first_add_bank(bank_id: int):
    """First upload data include Account,
     Company and Operation"""

    client = ClientApi()

    with transaction.atomic():
        for account_info in client.get_info_accounts():
            account_info.bank = bank_id
            company_model = Company.objects.filter(
                company_id=account_info.company_id
            ).first()
            if company_model:
                company = CompanySerializers(data=account_info.model_dump())

                company.is_valid()
                company.update(company_model, company.validated_data)
            else:
                company = CompanySerializers(data=account_info.model_dump())

                company.is_valid(raise_exception=True)
                company.save()

            for account in account_info.account:
                account.company = company.data.get('id')
                account_model = Account.objects.filter(
                    id_account=account.id_account
                ).first()
                if account_model:
                    accounts = AccountSerializers(data=account.model_dump())
                    accounts.is_valid()
                    accounts.update(account_model, accounts.validated_data)
                    account_id = account_model.id
                else:
                    accounts = AccountSerializers(data=account.model_dump())
                    accounts.is_valid(raise_exception=True)
                    accounts.save()
                    account_id = accounts.data.get('id')

                operations = client.get_first_history(
                    accounts.data.get(
                        'id_account'
                    )
                )

                for operation in operations:
                    operation.account = account_id
                    operation_model = Operation.objects.filter(
                        id_payment=operation.id_payment
                    ).first()

                    create_update_operations(
                        operation_model=operation_model,
                        operation=operation
                    )


@shared_task
def regular_unloading_operations(bank_id: int):
    client = ClientApi()
    accounts = Account.objects.filter(company__bank__id=bank_id)
    for account in accounts:
        operations = client.get_first_history(account.id_account)
        for operation in operations:
            operation.account = account.id
            operation_model = Operation.objects.filter(
                id_payment=operation.id_payment
            ).first()
            create_update_operations(
                operation_model=operation_model,
                operation=operation
            )


def create_update_operations(
        operation_model: Operation | None,
        operation: OperationSchema):

    if operation_model:
        operation = OperationSerializers(data=operation.model_dump())
        operation.is_valid()
        operation.update(operation_model, operation.validated_data)
    else:
        operation = OperationSerializers(data=operation.model_dump())
        operation.is_valid(raise_exception=True)
        operation.save()
