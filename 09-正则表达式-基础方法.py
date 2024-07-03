# 正则表达式是一种字符串验证的规则，通过特殊的字符串组合来确立规则
# 用规则去匹配字符串是否满足
import re

s="1python itheima python "
# match 从头匹配
result=re.match("python",s)
print(result)
# print(result.span())
# print(result.group())

# search 搜索匹配
# 搜索整个字符串，找出匹配的。从前向后，找到第一个后，就停止，不会继续向后
result=re.search("python",s)
print(result)

# findall 搜索全部匹配项
result=re.findall("python",s)
print(result)