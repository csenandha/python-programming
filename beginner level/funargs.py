def main():
    pass
list = ['GUVI', 'learning', 'is', 'awesome', 'always']
def foo(x):
     print x * 3


def map(fun, list):
     for a in list:
         fun(a)


map(foo, list)
if __name__ == '__main__':
    main()
