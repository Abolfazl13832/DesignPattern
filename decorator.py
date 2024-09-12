COUNTRYS = ['Iran', 'UAE']
VAT = {'iran':9,'UAE':15}
def show_total_price(purchase):
    pass
def show_vat_pluse_price(purchase) :
    pass

class User:
    pass

class Address:
    def __init__(self, country):
        self.country = country

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Purchase:
    def __init__(self, user, address):
        self.user = user 
        self.product_list = []
        self.address = address

    def add_products(self,product_list):
        if not isinstance(product_list,list):
            product_list = [product_list]
        self.product_list.extend(product_list)

    def total_price(self):
        s = 0
        for product in self.product_list:
            s += product.price

        return s
    

if __name__ == "__main__":
    user = User()
    addr_iran = Address(country=COUNTRYS[0])
    addr_UAE = Address(country=COUNTRYS[1])
    p1 = Product("persian rugs",150)
    p2 = Product("nain rugs", 160)
    product = [p1, p2]

    ph = Purchase(user=user , address=addr_UAE )
    ph.add_products(p1)
    ph.add_products([p2,p1])
    print(ph.total_price())

