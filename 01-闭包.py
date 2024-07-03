# 闭包：定义双层嵌套函数，内层可以访问外层函数的变量，将内存函数作为外层函数的返回值，此内层函数就是闭包函数
# 优点：无需全局变量即可实现通过函数，持续的访问、修改某个值，闭包使用的变量作用于函数内，难以被错误的调用修改
# 缺点：由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存

# 简单闭包
def outer(loge):
    def inner(msg):
        print(f"<{loge}>{msg}<{loge}>")
    return inner
fn1=outer("黑马程序员")
fn1("大家好")
fn2=outer("周姐轮")
fn2("taojiji")

# 使用nonlocal关键字修改外部函数的值
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1+=num2
        print(num1)
    return inner
fn=outer(10)
fn(5)
fn(10)
fn(15)

# 使用闭包实现atm小案例
def account_creat(amount=0):
    def atm(num,choose):
        nonlocal amount
        if choose:
            amount+=num
            print(f"存款成功，余额{amount}")
        else:
            amount-=num
            print(f"取款成功，余额{amount}")
    return atm
atm=account_creat()
atm(10,True)
atm(10,False)


