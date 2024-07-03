"""
演示python正则表达式使用元字符进行匹配
"""
import re

# s="itheima1 sadd4643lajkjdspo$$#%as s;dljdk"
# result=re.findall(r'\d',s)     # 字符串前面带上r的标记，表示字符串中转义字符无效，就是普通字符的意思
# print(result)

# 匹配账号，只能由字母和数字组成，长度限制6-10位
r='^[0-9a-zA-Z]{6,10}$'
s='213187'
print(re.findall(r,s))
# 匹配qq号，要求纯数字，长度5-11，第一位不为0
r='^[1-9][0-9]{4,10}$'
s='1234563'
print(re.findall(r,s))
# 匹配邮箱地址,只允许qq 163 gmail这三种
r=r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s='a.b.d.s.d.d.d.g@163.com.a.s.d'
print(re.findall(r,s))
