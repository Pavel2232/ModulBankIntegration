import datetime
import requests
from dateutil.relativedelta import relativedelta
from ModulBankIntegration.settings import env
from api_schema import AccountInfoSchema, OperationSchema


class ClientApi:

    def __init__(self):
        self._api = 'https://api.modulbank.ru/v1'
        self._authorization_bearer = {
            'Authorization': f"Bearer {env('TOKEN_MODUL_BANK')}",
        }

    def get_info_accounts(self) -> list[AccountInfoSchema]:
        """Get accounts by API ModuleBank"""
        response = requests.post(
            url=f'{self._api}/account-info',
            headers=self._authorization_bearer
        )
        response.raise_for_status()

        my_accounts = response.json()
        model_list = [AccountInfoSchema(**account) for account in my_accounts]

        return model_list

    def get_operation_history(self, account_id: str) -> list[OperationSchema]:
        """
        Get operation_history by API ModuleBank
        :param account_id: Syste identifier account.
        :return: history operations
        """
        response = requests.post(
            url=f'{self._api}/operation-history/{account_id}',
            headers=self._authorization_bearer,
            json={
                "from": str(datetime.date.today()),
                "till": str(datetime.date.today()),
            }
        )
        response.raise_for_status()
        operations = response.json()
        model_list = [OperationSchema(**operation) for operation in operations]

        return model_list

    def get_first_history(self, account_id: str) -> list[OperationSchema]:
        """
        Get operation_history by API ModuleBank by from a year ago to now
        :param account_id: System identifier account.
        :return: history operations
        """
        response = requests.post(
            url=f'{self._api}/operation-history/{account_id}',
            headers=self._authorization_bearer,
            json={
                "from": str(datetime.date.today() - relativedelta(years=1)),
                "till": str(datetime.date.today()),
            }
        )
        response.raise_for_status()
        operations = response.json()
        model_list = [OperationSchema(**operation) for operation in operations]

        return model_list
