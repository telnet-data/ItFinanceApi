import json
from it_finance_api import ItFinanceApi

with open('credentials.json', 'rb') as f:
    c = json.load(f)
    USERNAME = c.get('username')
    PASSWORD = c.get('password')


def main():
    api = ItFinanceApi(fiscal_code_user='02463640306')
    api.login(USERNAME, PASSWORD)

    # ACCOUNT PARTNER
    try:
        res = api.get_account_partner()
        print(res.capabilities)
    except Exception as exc:
        print(exc)

    try:
        res = api.get_score_companies_detail('12377440156')
        print(res)
        print(res.sic_list)
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    main()
