# # 这是我的第一个Python程序 
# print('hello world')
# print("这是我的第一个Python程序")
# # 输入两个数字，求和
# a = float(input('请输入第一数字： '))
# b = float(input('请输入第二数字： '))
# suma = a + b
# print(f"两个数字的和为： {float(suma)}")


# # 这是一个字典对象的练习
# phone_num = input ('请输入电话号码： ')
# phone_dict = {
#     '1':'one','2':'two','3':'three'}
# output = ''
# for ch in phone_num:
#     output += phone_dict.get(ch,"!") + " "
# print(output)

# 这是另一个字典的练习
# message = input('请输入一个短语： ')
# words = message.split(' ')
# emojis = {
#     ':)':'😊',
#     ':(':'😢'
# }
# output = ''
# for word in words:
#     output += emojis.get(word,word) + ' '
# print(output)

# # 这是第一个函数练习
# def greet_user(first_name, last_name):
#     """显示简单的问候语"""
#     print(f"Hello, {first_name.title()} {last_name.title()}!")

# greet_user(last_name='eson',first_name='chen')
# print("\n Finished!")

# 这是一个函数的练习
# def square(number):
#     """返回一个数的平方"""
#     return number ** 2
# print(square(100 ))

# def emoji_converter(message):
#     if not isinstance(message, str):
#         raise ValueError("Input must be a string")

#     try:
#         words = message.split(' ')
#         emojis = {':)': '😊', ':(': '😢'}
#         return ' '.join(emojis.get(word, word) for word in words)
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# # message = input('请输入一个短语： ')
# # print(emoji_converter(message))

# def test_emoji_converter():
#     # 正常输入测试
#     assert emoji_converter("Hello :) World") == "Hello 😊 World"
    
#     # 空字符串测试
#     assert emoji_converter("") == ""
    
#     # 特殊字符测试
#     assert emoji_converter("Hello 123 :) !@#") == "Hello 123 😊 !@#"
    
#     # 非字符串输入测试
#     try:
#         emoji_converter(123)
#     except ValueError as e:
#         assert str(e) == "Input must be a string"

# test_emoji_converter()


# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError: 
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Age can't be 0")
# except

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
 
# point = Point(1, 2)
# print(f'{point.x} , {point.y}')
# print(point.y)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is {self.age} years old")
    def talk(self):
        print(f"{self.name} says hello!")

p = Person("Eson", 30)
p.talk()