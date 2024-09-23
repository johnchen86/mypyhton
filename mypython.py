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

def greet_user(first_name, last_name):
    """显示简单的问候语"""
    print(f"Hello, {first_name.title()} {last_name.title()}!")

greet_user(last_name='eson',first_name='chen')
print("\n Finished!")