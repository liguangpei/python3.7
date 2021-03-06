# -*- coding: UTF-8 -*-

print "hello"
"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
函数内容以冒号起始，并且缩进
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
"""
#1--定义自己的打印函数
def printme(str):
    print "printme:",str
    return

printme("hello world")

"""
参数传递

在 python 中，类型属于对象，变量是没有类型的
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象

可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
"""
#python 传不可变对象实例
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print b # 结果是 2

#传可变对象实例
# 修改传入的列表
def changeme(mylist):
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

"""
参数

以下是调用函数时可使用的正式参数类型：

    必备参数 : 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
    
    关键字参数 : 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
    使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
    
    默认参数 ： 调用函数时，缺省参数的值如果没有传入，则被认为是默认值
    
    不定长参数：
    你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：

def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
   匿名函数：python 使用 lambda 来创建匿名函数
   lambda函数的语法只包含一个语句，如下：

    lambda [arg1 [,arg2,.....argn]]:expression

"""

#关键字参数 例子
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");

#默认参数 参数有缺省值
def printinfo2(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo2(age=50, name="miki");
printinfo2(name="miki");

#不定长参数  加了星号（*）的变量名会存放所有未命名的变量参数
def myMoreArgs(*var):
    print "不定长参数例子"
    for a in var:
        print a
    return

myMoreArgs(3)

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)

#return 语句
def sum(arg1, arg2):
    total = arg1+arg2
    return total
# 调用sum函数
mytotal = sum(10, 20)
printme(mytotal)

"""
全局变量想作用于函数内，需加 global
1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。

2、一个global语句可以同时定义多个变量，如 global x, y, z。

globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1
"""