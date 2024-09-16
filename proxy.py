COUNTRIES = ["Iran","UAE"]
VAT={"Iran":9,"UAE":15}
def check_permition(func):
    def wrapped_func(obj,user):
       if obj.user == user:
           return func(obj)
       return "You are not allowed to checkout"
    return wrapped_func

class User :
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
        self.address = address
        self.product_list =[]

    def add_products(self,products_list):
        if not isinstance(products_list,list):
           products_list = [products_list] 
        self.product_list.extend(products_list)

    def total_price(self):
        s=0
        for product in self.product_list:
            s+=product.price
        return s
    @check_permition
    def checkout(self):
        return "checkout done!"

def calculate_vat(func):
    def wrapped_func(pur):
        vat = VAT[pur.address.country]
        total_price = pur.total_price()
        return total_price +total_price * 9 / 100
    return wrapped_func

def show_total_price(p):
    return p.total_price()
@calculate_vat
def show_vat_pluse_price(p):
    return p.total_price()
if __name__ == "__main__":
    user = User()
    user1 = User()
    address1 =Address(country=COUNTRIES[0])
    address2 =Address(country=COUNTRIES[1])
    p1= Product("rug",150)
    p2= Product("television",300)
    p3= Product("seshvar",300)
    purchase = Purchase(user=user,address=address1)
    purchase.add_products([p1,p2])
    print(purchase.checkout(user))
    print(purchase.checkout(user1))

    