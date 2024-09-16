DATA = {"Iran":9,"UAE":15}
COUNTRIES = list(DATA.keys())
class User:
    pass

class Address:
    def __init__(self, country):
        self.country = country

class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.product_list = []

    def add_products(self,products_list):
        if not isinstance(products_list,list):
           products_list = [products_list] 
        self.product_list.extend(products_list)
    
    def total_price(self):
        s = 0
        for product in self.product_list:
            s+=product.price
        return s

class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
def calculate_vat(func):
    def wrapper_func(pur):
        vat = DATA[pur.address.country]
        total_price = pur.total_price()
        return total_price +total_price * vat /100
    return wrapper_func

@calculate_vat
def show_price_plus_vat(p):
    return p.total_price()

def show_price(p):
    return p.total_price()
if __name__  =="__main__":
    
    user =User()
    address_iran = Address(country=COUNTRIES[0])
    address_uae = Address(country=COUNTRIES[1])
    pr1= Product("pr1",150)
    pr2= Product("pr2",326)
    pr3= Product("pr3",178)
    purchase = Purchase(user=user,address=address_iran)
    purchase.add_products([pr1, pr2, pr3])
    print(show_price_plus_vat(purchase))
    print(show_price(purchase))