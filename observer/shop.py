from decorators import notify_observers
from notification import EmailNotification, SMSNotification, PushNotification
class Product:
    pass
class Payment:
    observers = [PushNotification,SMSNotification]
    @notify_observers("Purchase paid")
    def checkout(self):
        pass
class Purchase:
    observers=[EmailNotification,SMSNotification, PushNotification]
    def __init__(self, product_list):
        self.product = product_list
        self.payment = Payment()
    @notify_observers("Purchase paid")
    def checkout(self):
        self.payment.checkout ()
    @notify_observers("purchase canceled")
    def cancel(self):
        pass