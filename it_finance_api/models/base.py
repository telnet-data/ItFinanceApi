
class Address:

    def __init__(self, data):
        self.cap: str = data.get('cap', '')
        self.city: str = data.get('city', '')
        self.city_code: str = data.get('cityCode', '')
        self.city_code_istat: str = data.get('cityCodeIstat')
        self.name: str = data.get('name')
        self.number: str = data.get('number')
        self.place_name: str = data.get('placeName')
        self.province: str = data.get('province')
        self.town: str = data.get('town')
