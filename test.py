#%%
import time
'''
1. demand execute foo function
2. calculate the time of foo running
'''
def show_time(func):
    start = time.time()
    func()
    end = time.time()
    print('spend: {}'.format(end- start))

def foo():
    print('foo...')
    time.sleep(2)

def bar():
    print('bar ...')
    time.sleep(3)

show_time(foo)
#%%
# Decorator function装饰器函数
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend: {}'.format(end- start))
    return inner

foo = show_time(foo)
foo() # execute inner function 

bar = show_time(foo)
bar
#%%
'python Syntactic sugar'
@show_time    # Equivalent to foo = show_time(foo) 
def foo():
    print('foo...')
    time.sleep(2)
foo()
#%%
@show_time
def bar():
    print('bar ...')
    time.sleep(3)
bar()
#%%
def show_time(f):
    def inner(x,y):
        start = time.time()
        f(x,y)
        end = time.time()
        print('spend: {}'.format(end- start))
    return inner

@show_time # add = show_time(add)
def add(x, y):
    print('x+y: ', x+y)
    time.sleep(2)
add(1,2)
#%%
def show_time(f):
    def inner(*x, **y):
        start = time.time()
        f(*x, **y)
        end = time.time()
        print('spend: {}'.format(end- start))
    return inner

@show_time # add = show_time(add)
def add(*x, **y):
    sum = 0
    for i in x:
        sum += i
    print('sum: ', sum)
    time.sleep(2)
add(1,2,3,4,5)
#%%
# 装饰器函数加参数
def logger(flag):






#%%
#%%
l=[]
def wrapper(fun):
    l.append(fun)#统计当前程序中有多少个函数被装饰了
    def inner(*args,**kwargs):
        # l.append(fun)#统计本次程序执行有多少个带装饰器的函数被调用了
        ret = fun(*args,**kwargs)
        return ret
    return inner

@wrapper
def f1():
    print('in f1')

@wrapper
def f2():
    print('in f2')

@wrapper
def f3():
    print('in f3')
print(l)