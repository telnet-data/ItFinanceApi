import json
from it_finance_api import ItFinanceApi

with open('credentials.json', 'rb') as f:
    c = json.load(f)
    USERNAME = c.get('username')
    PASSWORD = c.get('password')


def main():
    api = ItFinanceApi()
    api.login(USERNAME, PASSWORD)

    try:
        res = api.get_score_companies_detail('02463640306', '02162000745')
        print(res)
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    main()
