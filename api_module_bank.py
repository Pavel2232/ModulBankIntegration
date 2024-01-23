import requests
from ModulBankIntegration.settings import env


class ClientApi:

    def __init__(self):
        self._api = 'https://api.modulbank.ru/v1'
        self._authorization_bearer = {
            'Authorization': f"Bearer {env('TOKEN_MODUL_BANK')}"
        }


    def get_info_accounts(self) -> list[dict]:
        """Get accounts by API ModuleBank"""
        response = requests.post(
                url=f'{self._api}/account-info',
                headers=self._authorization_bearer
        )

        my_accounts = response.json()

        return my_accounts

    def get_operation_history(self, account_id: str) -> list[dict]:
        """
        Get operation_history by API ModuleBank
        :param account_id: Системный идентификатор счета.
        :return: history operations
        """
        response = requests.post(
                url=f'{self._api}/operation-history/{account_id}',
                headers=self._authorization_bearer
        )
        result = response.json()
        return result
