# 设计模式是一种编程套路，可以方便程序的开发
# 面向对象就是最常见最经典的一个设计模式

# 单例模式：保证一个类只有一个实例，并提供一个访问他的全局访问点
from str_tools import str_tool
s1=str_tool
s2=str_tool
print(id(s1))
print(id(s2))













