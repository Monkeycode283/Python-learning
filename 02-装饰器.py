# 装饰器：使用创建一个闭包函数，在闭包函数内调用目标函数
# 也是一种闭包，在不破坏目标函数原有代码和功能前提下，为目标函数增加新功能
# 比如想给sleep函数增加两个输出语句
def outer(fun):        #外部函数接收想改造的函数
    def inner():       #内部函数增加功能
        print("起床")
        fun()
        print("睡觉")
    return inner       #返回内部函数
@ outer                #给sleep增加了一个outer的装饰器
def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1,5))
sleep()

# 10-16行代码相当于如下：
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1,5))
# fn=outer(sleep)
# fn()





