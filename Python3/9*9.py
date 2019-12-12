# encoding: utf-8

m = 1
while m <= 9:
    i = 1
    while i <= m:
        print(f'{i} X {m} = {i*m}', end=' ')
        i += 1
    print()
    m += 1


for m in range(1, 10):
    for i in range(1, m+1):
        print(f'{i} X {m} = {i * m}', end=' ')
    print()



nums = [5, 8, 7, 10, 20, 2, 6, 9]

max_num = max(nums)
min_num = min(nums)
max_index = nums.index(max_num)
min_index = nums.index(min_num)
print(max_num, max_index)
print(min_num, min_index)



nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [34, 12, 3, 5, 5, 4, 1, 3, 2, 1]

num_set = set(nums_1) & set(nums_2)
print(num_set)
print(list(num_set))

'''
# 相对路径：相对「脚本」执行的目录路径
# 绝对路径：从跟路径起的目录


# 打开&关闭文件
f = open('test.txt')
while True:
    f_read = f.read(3)   # 一次读取所有到内存中，防止文件过大，导致内存溢出，建议加“size”参数读取
    # print(f_read)      # print在此会多打印一行空行
    # 判断是否读取完毕
    if f_read == '':    
        break
    print(f_read)
    
    # if f_read:
    #     print(f_read)
    
f.close()       # 操作完毕，切忌要关闭文件

# 读取操作
print(f.read(3)）        # 一次读取所有「文本内容」到内存中，为防止文件过大，导致内存溢出，建议加“size”参数读取
print(f.readline())      # 每次读取一行
print(f.readlines())     # 一次读取所有「文本内容」，返回的是list类型，每个元素为文件的一行

# 文本读取建议
.read(size)     # size为每次读取的字节数，可通过while循环获取全部内容
.readline()

# 非文本文件，读取为「二进制」的建议
.read()或.read(size)     # 用其他方式读取时，如是乱码可能区分不出是在哪换行


'''



f = open('test.txt', 'r')   # +参数'b'：把文本读取为二进制

print(help(f.tell))

# print(f.read())
while True:
    f_read = f.read(3)
    # print(f_read)
    if f_read == '':    # '' != b''（空格不等于二进制空格）
        break
    print(f_read)

f.close()


print('中国'.encode())                           # 字符(编码)转为二进制
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode())     # 二进制(解码)转为字符


with open('test1.txt', 'a') as f:
    f.write('北京')
    f.write('昌平')

with open('test1.txt', 'r') as f:
    r = f.read()
    print(r)


'''
函数
    定义
    调用
    返回值
    参数
    匿名函数
    sorted&list.sort
模块与包
其他：三目表达式、列表推倒时
'''


a = 1
b = [1]
c = [1]

def test():
    global a, b
    a = 2
    b = [1, 2]
    c.append(2)     # 修改了全局变量c
    print(a)
    print(b)
    print(c)

test()
print(a)
print(b)
print(c)

l1 = [1, 2, 3]
l2 = l1
l2.append(4)       # 对l1有影响 > 基本类型
print(l1)       # [1, 2, 3, 4]
print(l2)       # [1, 2, 3, 4]


l3 = [4, 5, 6]
l4 = l3
l4 = [7, 8, 9]       # 对l3无影响 > 引用类型
print(l3)
print(l4)

print('>>>>>>>')
g_a = 1
g_b = [1]
g_c = [1]

def change(a, b, c):
    a = 2
    b = [1, 2]
    c.append(2)
    print(a, b, c)

change(g_a, g_b, g_c)
print('<<<<<<<<')
print(g_a, g_b, g_c)



key = lambda x : x
print(key(5))   # 5


print(True + False)  # 1
print(True + True)   # 2


# Django

# 前端：html，css，bs

