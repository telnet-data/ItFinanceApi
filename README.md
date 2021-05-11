# It Finances Api

## Official api documentation
https://api-test.itfinance.it/IT4FRest/rest/swagger-ui.html

## how to use it
``` python
    import json
    from it_finance_api import ItFinanceApi
    
    with open('credentials.json', 'rb') as f:
        c = json.load(f)
        USERNAME = c.get('username')
        PASSWORD = c.get('password')
    
    api = ItFinanceApi()
    api.login(USERNAME, PASSWORD)
    
    res:  = api.get_score_companies_detail('0246364', '02162745')
```

## Disclaimer
This wrapper is made only for those who have access to the api.
You have to directly contact It Finance to gain access to the endpoints.

The calls to this api are not free, the cost is defined with a contract with itFinance

## Contact 
http://www.itfinance.it