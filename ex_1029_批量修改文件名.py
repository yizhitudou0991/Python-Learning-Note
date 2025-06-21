import os

user_input0 = input(r'请输入文件夹所在的路径（例如：C:\abc):')
user_input1 = input('请输入要添加或删除的名字： ')
user_input2 = int(input('添加请按1，删除请按2'))
dir_list = os.listdir(user_input0)

print(dir_list)

for list_name in dir_list:
    if user_input2 == 1:
        new_name = user_input1 + list_name
        print(new_name)
    elif user_input2 == 2:
        front_add = len(user_input1)
        new_name = list_name[front_add:]
        print(new_name)
    else:
        print('输入错误，只能输入1或者2')
        break
    os.chdir(user_input0) #将程序的作用目录更改到C：\abc
    os.rename(list_name,new_name) #执行修改名字的操作