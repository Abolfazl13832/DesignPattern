from abc import ABC ,abstractmethod

class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass
    @abstractmethod
    def price(self):
        pass
    # @abstractmethod
    # def shipping(self):
    #     pass

    #برای این که بتونیم همه محصول ها رو به ی شکل صدابزنیم باید یدونه پروداکت بیسی داشته باشیم 

class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass
class RugsDetail(DetailBase):
    def __init__(self,rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs detail: {self.rugs._name}"
class RugsPrice(DetailBase):
    def __init__(self,rugs):
        self.rugs = rugs
    def show(self):
        return f"rugs price: {self.rugs._price}"
class GiftCardDetail(DetailBase):
    def __init__(self,card):
        self.card = card
    def show (self):
        return f"company: {self.card.company}"

class GiftCardPrice():
    def __init__(self,card):
        self.card = card
    def show (self):
        return f"gitcard min: {self.card.min_price}\t gitcard min: {self.card.max_price}"

#فرض کنید که ی فروشگاه داریم که کالاهای مختلفی میفروشیم

class Rugs(ProductBase):
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def detail(self):
        return RugsDetail(self)
    @property
    def price(self):
        return RugsPrice(self)
class Mobile:
    pass

class GiftCard(ProductBase):
    def __init__(self, company , min_price , max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
    @property
    def detail(self):
        return GiftCardDetail(self)
    @property
    def price(self):
        return GiftCardPrice(self)

#میبینید همه اینا باهم دیگه فرق میکنن 


if __name__ == "__main__":
    r1 = Rugs("persian rugs",135)
    r2 = Rugs("nain rugs",150)

    g1 = GiftCard('google',20,60)
    g2 = GiftCard('apple',20,60)
    products = [r1,r2,g1,g2]

    for product in products:
        print(product.detail.show())
        print(product.price.show())

#دقیقا فکتوری میاد پیچیدگی ساخت ابجکت و استفاده ازش رو پنهان میکه توسط کد هایی که زدیم تا اتین که رسیدیم که خیلی ساده با ی حلقه فور همه دیتیل و پرایس رو نشون بدیم