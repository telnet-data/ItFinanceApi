# Data Finance wrapper
Developed by Telnet Data

## Scopo
Data Finance è un azienda che si occupa di schedare le anagrafiche aziendali

## Implementazione
Il wrapper è parzialmente implementato, ossia la base è completa ma non sono stati mappati tutti gli endpoint
e nemmeno tutti gli oggetti risposta.

## Funzionalità
- Controllo delle licenze all'avvio per evitare di fare chiamate ad endpoint a cui non si ha i permessi
- Eccezioni per tutti gli errori mappate
- Possibilità di cambiare utente loggato a runtime, senza dover istanziare nuovamente la classe.
- Possibilità di istanziare n classi, tutto viene salvato nelle variabili d'istanza.

## Endpoint attualmente mappati
- ACCOUNT_PARTNER:  `itf/account/v1/partner`
- ACCOUNT_SUBSCRIBER: `itf/account/v1/subscriber`
- ACCOUNT_SUBSCRIBERS: `itf/account/v1/subscribers`
- SCORE_COMPANIES_DETAIL: `itf/creditscore/v1/companies/fiscal/detail`
- SCORE_COMPANIES_OVERVIEW: `itf/creditscore/v1/companies/fiscal/overview`

## Come usarlo
``` python
    import json
    from it_finance_api import ItFinanceApi
    from it_finance_api.models import CreditScoreDetailData
    from it_finance_api.exceptions import (
        NetworkError,
        InvalidLicenseError,
        UnauthorizedError,
        InvalidParametersError,
        NotFoundError,
        MaxRequestsExceededError,
        GenericError,
        NotAvailableError,
    )
    
    # ottieni le credenziali segrete
    with open('credentials.json', 'rb') as f:
        c = json.load(f)
        USERNAME = c.get('username')
        PASSWORD = c.get('password')
    
    api = ItFinanceApi(fiscal_code_user='1234')  # fiscal_code_user: partita iva del account su cui si fa il login
    api.login(USERNAME, PASSWORD)
    
    # chiama gli endpoint
    try:
        res: CreditScoreDetailData  = api.get_score_companies_detail('02162745')
    except NetworkError:
        pass
    except InvalidLicenseError:
        pass
    except ...
        ...
```

Guardare gli esempi

## Disclaimer
Questo codice è libero ed ognuno può scaricarlo e modificarlo,
non si accettano reclami per malfunzionamenti o bug.
Se si decide di usare questo wrapper si è completamente responsabili di cio che esso fa.

Le api che si vanno a chiamare sono a pagamento.
