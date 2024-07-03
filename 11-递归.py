# 递归:函数自己调用自己的一种特殊编程写法
# 递归需要注意:1.退出的条件,否则容易变成无线递归   2.注意返回值的传递,确保从最内层,层层传递到最外层
import os

def test_os():
    print(os.listdir("D:\test"))         # 列出路径下的内容
    print(os.path.isdir("D:\test\a"))    # 判断指定路径是不是文件夹
    print(os.path.exists("D:\test"))     # 判断指定路径是否存在

def get_file_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式,获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list,包含全部的文件,如果目录不存在或者无文件就返回一个空list
    """
    file_list=[]
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path=path+"/"+f
            if os.path.isdir(new_path):
                # 进入到这里,表明这个目录是文件夹不是文件
                file_list+=get_file_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)

    else:
        print(f"被指定的目录{path}不存在")
        return []

    return file_list

if __name__=='__main__':
    print(get_file_recursion_from_dir(...))
