from it_finance_api.models.base import Address


class CreditScoreDetailData:

    def __init__(self, data):
        self.address: Address = Address(data.get('address', {}))
        self.ateco_list: [] = data.get('atecoList', [])
        self.capital: int = data.get('capital', 0)
        self.cciaa: str = data.get('cciaa', '')
        self.constitution_date: str = data.get('constitution_date', '')
        self.employees: int = data.get('employees', 0)
        self.fax: str = data.get('fax', '')
        self.fiscal_code: str = data.get('fiscal_code', '')
        self.iban: str = data.get('iban', '')
        self.id: int = data.get('id', 0)
        self.last_account_closure_date: str = data.get('lastAccountClosureDate', '')
        self.legal_nature: str = data.get('legal_nature', '')
        self.legal_nature_code: str = data.get('legalNatureCode', '')
        self.name: str = data.get('name', '')
        self.pec: str = data.get('pec', '')
        self.politically_exposed: bool = data.get('politically_exposed', False)
        self.politically_exposed_details: str = data.get('politicallyExposedDetails', '')
        self.rea_number: str = data.get('reaNumber', '')
        self.revenue: int = data.get('revenue', 0)
        self.sic_list: [] = data.get('sicList', [])
        self.status: str = data.get('status', '')
        self.technical_id: str = data.get('technicalId', '')
        self.tel_home: str = data.get('telHome', '')
        self.tel_mobile: str = data.get('telMobile', '')
        self.tel_office: str = data.get('telOffice', '')
        self.vat_code: str = data.get('vatCode', '')


class CreditScoreOverviewData:

    def __init__(self, data):
        self.address: Address = Address(data.get('address', {}))
        self.ateco_sector_code: str = data.get('atecoSectorCode', '')
        self.ateco_sector_code_description: str = data.get('atecoSectorCodeDescription', '')
        self.cciaa: str = data.get('cciaa', '')
        self.fiscal_code: str = data.get('fiscalCode', '')
        self.legal_form_type_code: str = data.get('legalFormTypeCode', '')
        self.legal_form_type_description: str = data.get('legalFormTypeDescription', '')
        self.name: str = data.get('name', '')
        self.rea_number: str = data.get('reaNumber', '')
        self.vat_code: str = data.get('vatCode', '')
