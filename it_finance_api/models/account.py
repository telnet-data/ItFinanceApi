from enum import Enum
from typing import List
from datetime import datetime


class CapabilitiesType(Enum):
    CREDIT_SCORE = 'CREDIT_SCORE'
    CREDIT_SCORE_SUBSCRIPTION = 'CREDIT_SCORE_SUBSCRIPTION'
    CREDIT_SCORE_REPORT = 'CREDIT_SCORE_REPORT'
    CREDIT_SCORE_SMART = 'CREDIT_SCORE_SMART'
    CREDIT_SCORE_MAIN_INFO = 'CREDIT_SCORE_MAIN_INFO'
    CREDIT_SCORE_MAIN_INFO_OVERVIEW = 'CREDIT_SCORE_MAIN_INFO_OVERVIEW'
    COMPANY_CERTIFICATE = 'COMPANY_CERTIFICATE'
    PSD2 = 'PSD2'


class CapabilitiesData:

    def __init__(self, data):
        self.context: str = data.get('context', '')
        self.id: int = data.get('id', 0)
        self.name: CapabilitiesType = CapabilitiesType(data.get('name', ''))

    def __repr__(self):
        return f'{self.context}-{self.id}-{self.name}'


class AccountData:

    def __init__(self, data):
        self.capabilities: List[CapabilitiesData] = [CapabilitiesData(el) for el in data.get('capabilities', {})]
        self.creationDate: str = data.get('creationDate', '')
        self.id: int = data.get('id', 0)
        self.id_user: int = data.get('userId', 0)
        self.name: str = data.get('name', '')
        self.state: str = data.get('state', '')
        self.update_date: str = data.get('updateDate', '')

        # automatically updated on obj creation
        self.last_call_update: datetime = datetime.now()

    @property
    def capabilities_list(self):
        return [el.name for el in self.capabilities]

    def __repr__(self):
        return self.name

    def has_capabilities(self, capabilities):
        """
        Check if the account has the licenses to perform the action
        :param capabilities: a list of capabilities
        :return: True or False
        """
        account_capabilities = self.capabilities_list
        for capability in capabilities:
            if capability not in account_capabilities:
                return False
        return True
