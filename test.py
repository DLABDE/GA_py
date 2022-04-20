class MyOuter(object):
    age = 18
    def __init__(self, name):
        self.name = name
    @classmethod
    def outer_class_method(cls):
        print('我是外部类的类方法')
    class MyInner(object):
        def __init__(self, inner_name):
            self.inner_name = inner_name
        def inner_method(self):
            print('我是内部类的对象方法')
            MyOuter.outer_class_method()


out = MyOuter('lqz')
inner = out.MyInner('lqz_inner')
inner.inner_method()
