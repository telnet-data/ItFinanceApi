import requests
from requests.auth import HTTPBasicAuth
from it_finance_api.response import ItFinanceResponse
from it_finance_api.endpoints import *
from it_finance_api.models.credit_score import (
    CreditScoreDetailData,
    CreditScoreOverviewData,
)


class ItFinanceApi:

    def __init__(
            self,
            base_uri='https://api-test.itfinance.it/IT4FRest/rest/',
            return_raw=False,
            raise_exception=True,
    ):
        """
        :param base_uri: the url of the api
        :param return_raw: return the data as json do not wrap into class
        :param raise_exception: return data without error handling
        """
        self.fiscal_code_user = None
        self.base_uri = base_uri
        self.return_raw = return_raw
        self.raise_exception = raise_exception
        self.auth = ''

    def login(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def get_score_companies_detail(self, fiscal_code_user, fiscal_id, search_type='fiscalCode'):
        """
        :param fiscal_code_user: The fiscal code of the user sending the request (company)
        :param fiscal_id: The Fiscal ID of the company, can be a VAT CODE or a FISCAL CODE depending on the search type
        :param search_type: The kind of search between:
                - fiscalCode
                - vatNumber
        :return:
        """
        uri_params = f'?fiscalCodeUser={fiscal_code_user}&fiscalId={fiscal_id}&searchType={search_type}'

        res = requests.get(
            self.base_uri+SCORE_COMPANIES_DETAIL+uri_params,
            auth=self.auth
        )

        if self.return_raw:
            return res.content

        data = ItFinanceResponse(res)()
        return CreditScoreDetailData(data)

    def get_score_companies_overview(self, fiscal_code_user, fiscal_id, search_type='fiscalCode'):
        """
        :param fiscal_code_user: The fiscal code of the user sending the request (company)
        :param fiscal_id: The Fiscal ID of the company, can be a VAT CODE or a FISCAL CODE depending on the search type
        :param search_type: The kind of search between:
                - fiscalCode
                - vatNumber
        :return:
        """
        uri_params = f'?fiscalCodeUser={fiscal_code_user}&fiscalId={fiscal_id}&searchType={search_type}'

        res = requests.get(
            self.base_uri+SCORE_COMPANIES_DETAIL+uri_params,
            auth=self.auth
        )

        if self.return_raw:
            return res.content

        data = ItFinanceResponse(res)()
        return CreditScoreOverviewData(data)
