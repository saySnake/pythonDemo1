#导入OS模块
import os

#修改工作目录到桌面Python文件夹中
os.chdir('C:\\Users\\Administrator\\Desktop\\Python')

#输出提示当前工作路径
print('当前所在路径：',os.getcwd())


#列出文件夹中所有内容列表

lists = os.listdir(os.getcwd())
print('文件列表：',lists)

#用format函数统计有多少个文件
print('总计{p}个文件'.format(p = len(lists)))


while True:
    handle_file = input('请输入接下来的操作：m:创建文件；rm:删除文件；n:修改文件名；e:退出\n')
    if handle_file == 'm':
        mk_filename = input('请输入需要创建的文件名：\n')
        os.mkdir(mk_filename)
        mk = os.listdir(os.getcwd())
        
        #利用成员检测判断是否创建成功
        if mk_filename in mk:
            print('创建成功！恭喜您！')
            
    elif handle_file == 'rm':
        rm_filename = input('请输入需要删除的文件名：\n')
        os.rmdir(rm_filename)
        rm = os.listdir(os.getcwd())
        
        #利用成员检测判断是否删除成功
        if rm_filename not in rm:
            print('删除成功！')          
        
    elif handle_file == 'n':
        #使用while循环判断输入的名称是否存在
        while True:
            res = input('请输入需要修改的文件或文件夹名称：\n')
            if res not in lists:
                print('对不起，您输入的文件或文件夹名不存在，请确认后重新输入！')
            else:
                break
        n_filename = input('请输入修改后的名称：\n')
        os.rename(res,n_filename)
        n = os.listdir(os.getcwd())
        if n_filename in n:
            print('修改成功！')
        
    elif handle_file == 'e':
        exit()
        
    else:
        print('输入有误，请输入提示的内容，谢谢！')
    

