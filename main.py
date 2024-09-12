class DatabaseHandler:
    @classmethod
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(*args,**kwargs)
        return cls.instance
    # سینگلتون به ما کمک میکنه که از هر کلاس فقط ی دونه آبجکت بسازیم.
    #مثلا در بحث پایگاه داده اگر بدون سیمگل تون باشه برای هر ریکوست میاد یدونه ابجکت میسازه که با پایگاه داده در ارتباط باشه اگر به صورت سینگلتون بنویسیم میاد یدونه ابجکت میسازه و برای همه ی ریکوست ها از ان به طور مشرک استفاده میکنه 

if __name__ == "__main__":
    s1 = DatabaseHandler()
    s2 = DatabaseHandler()
    s3 = DatabaseHandler()
    print(id(s1))
    print(id(s2))
    print(id(s3))


#جلسه امروز در مورد factory وabstract factory هست