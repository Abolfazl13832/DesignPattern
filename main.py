class DatabaseHandler:
    @classmethod
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(*args,**kwargs)
        return cls.instance
    '''سینگلتون به ما کمک میکنه که از هر کلاس فقط ی دونه آبجکت بسازیم.'''

if __name__ == "__main__":
    s1 = DatabaseHandler()
    s2 = DatabaseHandler()
    s3 = DatabaseHandler()
    print(id(s1))
    print(id(s2))
    print(id(s3))


