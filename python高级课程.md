
# 总结python中的字符串，列表，元组，字典，集合的操作方法，和内建函数
     
     
     
     

# 总结文件操作和相关模块的知识点
    倒入数学math 模块
    ceil() & floor() round pow
    num =9.0001
    1.向上取整操作
    result =math.ceil(num)
    print(result)
    打印结果是10
    
    2.向下取整操作
    result =math.floor(num)
    打印结果是9
    
    3.round 四舍五入 ps不在math模块内
    num =9.55
    result =round(num)
    print(result)
    打印结果 10
    
    4.pow 一个数的n次方 (返回的永远是浮点型)
    result =math.pow(3,4)
    print(result)
    打印结果81.0
    
    5.sqrt() 开平方
    返回值：浮点数
    num =9
    result =math.sqrt(num)
    print(result)
    打印结果是3.0
    
    6.fabs()
    对一个数值获取绝对值操作
    格式：math.fabs(数值)
    返回值：浮点数
    
    7.modf （将一个浮点拆成整数部分和小数部分组成的远组）
    num =12/138
    result =math.modf(num)
    print(result)
    输出结果：（0.1379999999，12.0）
    
    8.copysign 符号复制（将第二个书的正负号复制给第一个数）
        num1=99
        num2 =-7
        result =math.copysign(num1,num2)
        print(result)
        输出结果：-99
    
    9.fsum 将一个序列求和运算
    list =[1,35,7,21,7,24]
    result =math.fsum(list)
    print(result)
    输出结果：317.0
    
    10.sum 将一个序列求和运算（得到的是整形）
 ### 模块提供的常见值
      pi (圆周率)
      print(math.pi)
      e （自然底数）
      print(math.e)
      
 ### 随机模块 （需要倒入import random）
     查看随机模块文档 help(random)
     1.random()
     获取0~1之间的随机数（包含0不包含1）
     result =random.random()
     print(result)
     运行一次随机一次
     
     获取0～100随机数(如果取整的话需要倒入math 模块)
     import math
     
     result =math.floor(random.random()*100)
     prient(result)
     
     2.choice随机获取列表的值
     random.choice(序列)
     返回值：序列中的某个值
     one=[1,2,3,4,5,6,7,8,9,10]
     two=[1,2,3,4,5,6,7,8,9,10]
     thre=[1,2,3,4,5,6,7,8,9,10]
     four=[1,2,3,4,5,6,7,8,9,10]
     five=[1,2,3,4,5,6,7,8,9,10]
     
     result =rando,.choice(one)
     print(result)
     
     3.shuffle(随机打乱序列)
     rando,.shuffle(序列)
     one=[1,2,3,4,5,6,7,8,9,10]
     result =rando.shuffle(one)
     print(one)
     输出结果：[6,7,1,2,3,9,10,8]
    
     4.randrange()
     获取指定范围内指定间隔的随机！！！！整数！！！间隔值可以写可以不写
     格式：random.rangdrange(开始值，结束值[,间隔值])
     返回值：整数
     
     获取0到100的随机数间隔5个数
     result =random.randrange(0,100,5)
     print(result)
    
     5.uniform()
     随机获取指定范围内的所有数值包括小数
     格式：random.uniform(开始值，结束值)
     返回值：随机返回范围内的所有数值（浮点型）
     result =random.unoform(10,20)
     print(result)
 
# 内键函数、
### 已经学过的内键函数
      int()  创建或者将其他数据转化为整形
      float() 创建或者将其他数据转化为浮点型
      bool()  布尔型
      complex() 复数
      list()   列表
      str()   字符串
      tuple()  元组
      set()  集合
      dict()  字典
      以上函数可以用于创建或者进行类型转换
    
  ### 变量相关：
  id() 获取变量id标志
  type() 获取变量的类型字符串
  print() 打印变量的值
  locals() 打印当前环境中的所有的变量
  
  ## 数学相关：
      abs（）获取一个数值的绝对值
      sum ()计算数列的数值合
  #### max() 获取最大值
          lists =[1,3,10,5,6,7]
          result =max(lists)
          print(result)
          打印结果：10
  
          result =max(1,3,5,7,10,12)
          print(result)
          打印结果：12

  ####  min() 获取最小值
          lists =[1,3,10,5,6,7]
          result =min(lists)
          print(result)
          打印结果：1
  
          result =min(1,3,5,7,10,12)
          print(result)
          打印结果：1
          
          pow()获取一个数值的n次方
          round()对一个数值进行四舍五入操作
          
          range()产生连续数据的序列
          range(结束值)1个参数
          range(开始，结束) 直接的序列
          range(5,50,5) 5-50学咧 5的整数倍（间隔值）
          
  ### 进制相关
          hex() 将十进制转换为16进制
                    print(hex(255))

          oct() 将十进制转换为8进制
                    print(oct(64))
                    
          bin() 将十进制转换为2进制
                    print(bin(10)
  ### 与字符串相关
          chr()将ascii编码转化为字符
          ord()将字符转化为ascii编码
          repr()获取任意数据的原始格式字符串（书写格式带引号）
                  str1 ='你好啊'
                  result=repr(str1)
                  print(result)
                  打印结果：'你好啊'
          eval()将一个字符串当作python代码执行,字符串需要符合代规范和repr配合
                  
                  result=eval(repr(str1))
          

# 创建列表的方法
* 创建方法1
* lists =[]
        print(type(lists))
        print(lists)
* 创建方法2
        lists =list()
        print(type(lists))
        print(lists)
        
### 创建具有一个数据的列表
          * lists =['sss']
          * print(type(lists))
          * print(lists)
           
### 创建具有多个数据的列表
            lists =['ss','sss','ssss']
            print(type(lists))
            print(lists)
            
            
     列表的基本操作
     * 1.访问列表的元素（值）
         lists =['鲁智深','花和尚','及时雨']
         print(lists[2])
      2.修改列表的元素
          lists =['鲁智深','花和尚','及时雨']
          lists[2]="呼保义"
          print(lists)
          输出结果：['鲁智深','花和尚','呼保义']
      3.添加元素（正常操作无法添加元素，需要借助函数）
      4.删除元素 
         del lists[2]
         print(lists)
         输出结果:['鲁智深','花和尚]
     5.删除任意变量
         del lists
         print(lists)
         打印：报错，找不到这个lists定义
     6.列表相加
         lists1 =['张全']
         lists2 =['2']
         result =lists1+lists2
         print(result)
         输出结果：['张全','2']
         
     7.列表相乘
         lists =["2"]
         result =lists*5
         print(result)
         输出结果：["2","2","2","2","2"]
         
     8.索引操作
         lists =['守护在她身边,'帮她盖上被子','亲吻她一下','把她xxx了']
         print(lists[2])
         print(lists[3])
         print(lists[3])
         print(lists[1]) 
         print(lists[0])
     9.取片操作
         lists =['1','2','3','4','5']
         print(lists[1:4])从1到4不包括5
         print(lists[2:]) 从3到结尾
         print(lists[:2]) 从开始到到3
         print(lists[::2]) 第三个参数 间隔
         print(lists[::]) 复制整个lists
         
     10. 成员检测操作
        result ="1" in lists
        print(result)
        输出结果：True
        
        result ='10' not in lists
        print(result)
        输出结果：True
        
      11. 序列相关的函数操作
         len 获取列表的长度操作
             result = len（lists）
             print(result)
             输出结果：5
         max & min     获取列表的最大值/最小值 （如果是汉子的话 是按照编码来计算的）
             lists =['1','2','3','4','5']
             result =max(lists)
             print(result)
             输出结果：5
         
      列表推导式
         lists =['张玮','你好']
         最简单列表推导式
            result =[i for i in lists]
            print(result)
            打印结果：['张玮','你好']
         带有运算的列表推导式
            result =[girl +"a" for girl in lists]
            print(result)
            打印结果：['张玮a','你好a']
         带有条件判断的列表推导式
            nums =[1,2,3,5,6,8]
            只要偶数
            result =[i for i in nums if i%2 ==0]
            print(result)
            打印结果：[2,6,8]
    
       多循环推导式
          boys =['吴升宇'，‘用剪开’，‘徐达’，‘张宏喜’]
          girls =['徐颖'，'有颗心',‘万凌云’,'周光里']
          result =[b+'<->'+g for b in boys for g in girls]
          print(result)           打印结果：['吴升宇<->徐颖'，'吴升宇<->有颗心','吴升宇<->万凌云',‘吴升宇<->周光里’,'用剪开<->徐颖'，'用剪开<->有颗心','用剪开<->万凌云',‘用剪开<->周光里’,'徐达<->徐颖'，'徐达<->有颗心','徐达<->万凌云',‘徐达<->周光里’,'张宏喜<->徐颖'，'张宏喜<->有颗心','张宏喜<->万凌云',‘张宏喜<->周光里’]
          
       多循环推导式带有判断条件的格式
          boys =['吴升宇'，‘用剪开’，‘徐达’，‘张宏喜’]
          girls =['徐颖'，'有颗心',‘万凌云’,'周光里']
          result =[b+‘--’+g for b in boys for g in girls if boys.index(b)== grils.index(g)]
          print(result)
          打印结果：['吴升宇<->徐颖','用剪开<->徐颖','徐达<->徐颖','张宏喜<->徐颖']
          
        列表的函数操作
* append()  在列表的末尾添加值
            lists =[1,3,5]
            lists.append(6)
            print(lists)
            输出结果：[1, 3, 5, 6]
            
* clear() 清空列表
           lists.clear()
           print(lists)
           输出结果：[]
           
* copy()
            lists =[1,3,5]
            result =lists.copy()
            print(result)
            输出结果：[1,3,5]
            检测是不是在内存中是否是同一个列表
            print(result is lists)
            输出结果：False
            
* count()计算某个值在列表中出现的次数
             lists =[1,2,3,5,6,2,4,2,5]
             result =lists.couont(2)
             print(result)
             输出结果：3
           
* extend()将一个列表继承另外一个列表,类似列表相加操作
               lists1 =["我",'你','她']
               lists2 =[‘hha’,‘你好’,‘他好‘]
               lists1.extend(lists2)
               print(lists1)
               输出结果：['我', '你', '她', 'hha', '你好', '他好']
               
* index 获取某个值在列表中第一次数出现的索引值
                lists1 =["我",'你','她']
                result =lists1(“我”)
                print(result)
                输出结果：0
                
* insert()  在列表中指定位置之前插入一个数据和append是一套 无返回值
                lists1 =['我','我','你','你','她']
                lists1.insert(0,‘she’)
                print(lists1)
                输出结果：['she', '我', '我', '你', '你', '她']
                
* pop（）移除列表中的指定索引元素 不写参数默认最后一个值
               lists =['我','我','你','你','她']
               result =lists.pop(2)
               print(result)
               输出结果：你
               print(lists)
               输出结果：['我','我','你','她']
               
* remoe()移除列表中的某个值
               lists =['我','我','你','你','她']           
               lists.remove(“我”)
               print(lists)
               输出结果：['我', '你', '你', '她']
               
* reverse()列表反转操作
                lists =['我1','我2','你1','你2','她']           
                lists.reverse()
                print(lists)
                输出结果：['她', '你2', '你1', '我2', '我1']
                
* sort()列表的排序
               nums =[12,123,133,1241412,53231,122]
               1.数字正序排列
               nums.sort()
               print(nums)
               输出结果：[12, 122, 123, 133, 53231, 1241412]
               
* 数字的倒序排列
              num.sort(reverse =True)
              print(nums)
              输出结果：[1241412, 53231, 133, 123, 122, 12]





# 元组的操作
* 创建元组
 * 创建空元组
     变量=（）或者变量 =turple()
    * 创建单个元素的元组
        turple =(值，) 或者变量 =值，
        print(type(turple))
        print（turple）
    * tuple1 =tuple()
    注意tuple1 =(“这不是元组”)
        print（type(tuple1)）
        输出结果：str
        
        * 要想变成元素tuple1 =(“这是元组加了一个,号”,)
    
    
    * 创建多个元素的元组
        turple =(“11”，‘22’，‘33’)
        turple =(值，值。。。。) 或者变量 =值，值。。。。
* 基本操作
 * 1.访问元素  变量（索引值）
        turple =(“11”，‘22’，‘33’)
        print(turple("1"))
        输出结果：22
        
        
 * 2.修改元素
      不可以  turple[3]=“不能修改”
 
 * 3.删除元素
      不可以 del turple[2] 不可以
      删除整个元组
          turple =（“w”,“f”,“m”）
          del turple
 
 * 4.添加元素
      不可以
* 序列操作
 * 元组相加操作
     turple1 =("1","2","3","4")
     turple2 =("5","6","7","8")
     result =turple1+turpl2
     print(result)
     输出结果：("1","2","3","4","5","6","7","8")
     
  * 元组相乘操作
      turple1 =('1','2')
      result =rurple1 *5
      print(result)
      输出结果：('1','2','1','2','1','2','1','2','1','2')
      
  * 分片操作
      turple1 =('a','b','c','d','e','f')
      print([2:5])
      输出结果:('c','d','e')
      
      print([2:])
      print([:5])
      print([:])
      print([::2])

  * 成员检测
      turple1 =('a','b','c','d','e','f')
      result ='g' in turple1
      print(result)
      输出结果：False
      
      result ='g' not in turple1
      输出结果：True

      
* 列表函数
 * 序列函数
     turple1 =('a','b','c','d','e','f')
     result =len(turple1)
     print(result)
     输出结果：6
 * max & min 获取元组中的最大值 最小值
     turple1=('1','4','232')
     maxresult =max(turple1)
     minresult =min(turple1)
     输出结果：232 ,1
 * tuple 创建空元组或者将其他序列转化为元组
     tuple1=()
     print(tuple1)
     输出结果：()
     
     tuple2 =tuple("今天天气不错，风和日丽")
     print(tuple2)
     输出结果：('今', '天', '天', '气', '不', '错', '，', '风', '和', '日', '丽')

 * 元组的遍历
  * while循环
     turple1 =('a','b','c','d','e','f')
     获取长度
     cd =len(tuple1)
     i =0
     while i<cd:
         print(tuple1[i])
         i+=1
  * for.. in
      for one in tuple1:
          print(one)
       
  * 多级元组的遍历
   *长度相等的二级元组
      tuple1 =(
      ('张玮1','178','220今天'),
      ('张玮2','178','220今天'),
      ('张玮3','178','220今天'),
      ('张玮4','178','220今天'),
      ('张玮5','178','220今天'),
      )
      for name,height,weight in tuple1:
          print(name,height,weight)
      输出结果：  张玮1 178 220今天
                张玮2 178 220今天
                张玮3 178 220今天
                张玮4 178 220今天
                张玮5 178 220今天
                
    *长度不等的二级元组                     
          tuple1 =(
      ('张玮1','178','220今天','你好啊','dada'),
      ('张玮2','178','220今天'),
      ('张玮3','178','220今天'),
      ('张玮4','178','220今天'),
      ('张玮5','178','220今天'),
      )
      for one in tuple1:
          for infor in one:
              print(infor)
              
     输出结果：张玮1
              178
              220今天
              fas
              张玮2
              178
              张玮3
              178
              220今天
              张玮4
              178
              220今天
              张玮5
              178
              220今天
         
         
* 元组内涵/元组推导式
 * 简单的元组推导式
     tuple1 =('1','2','3','4')
     result =(i for i in tuple1)
     print(result)
     输出结果：生成器(惰性求值)
     
     要想取出来：next(result)
     for..in  循环 可以去读生成器
     for i in result
          print(i)
     输出结果: 1
              2
              3
              4
              
  * 带有运算的元组推导式
       tuple1 =(1,2,3,4,5,10)
       result =(i+100 for i in tuple1)
       print(result)
       
   *   获取数据
        for x in result:
           print(x)
           
  * 带有判断的元组推导式
      tuple1 =(2,2,4,5,8,9,11)
      获取所有偶数
      result =(i for i in tuple1 if 1%2 ==0)
      print(result)
      
      获取数据：
      for x in result:
       print(x)
      打印结果：2，2，4，8
      
   * 多个循环的元组推导式
       girls =("a",'b','c')
       boys =('d','s','d')
       result =(g +'--'+b for g in girls for b in boys)
       print(result)
       打印结果：
       
       for x in result:
           print(x)
       打印结果：a--d
                a--s
                a--d
                b--d
                b--s
                b--d
                c--d
                c--s
                c--d
                
   * 带有条件的多个循环推导式
       girls =("a",'b','c')
       boys =('d','s','d')
       result =(g+'--'b for g in girls for b in boys if girls.index(g)== boys.index(b))
       for x in result:
          print(x)
       打印结果： a--d
                a--d
                b--s

     
* 元组函数

# 字典的操作
* 创建字典
 * 创建空字典
     dict1 ={}
     dict1 =dict()
     
 * 创建具有多个元素的字典
     1.dict1={"a":"f","s":"f"}
     2.dict2 =dict({"a":"f","s":"f)
     3.dict3 =dict(a ="f",s="f")
     
     4.lists =[
      ["a","f"],
      ["s","f"]
     ]
     dict4 =dict(lists)
     5.tuple1 =(
      ("a","f"),
      ("s","f")
     )
     dict5 =dict(tuple1)
     
     6.第六种创建
     key =(a,s)
     value =(s,f)
     dict6 =dict(zip(key,value))
 * 访问操作（通过key访问）
  * dict1={"a":"f","s":"f"}
    print(dict1["a"])
    
 * 直接添加元素（键值对）
   dict1["lzs"]=“鲁智深”
   print(dict1)
   输出结果：{'a': 'f', 's': 'f', 'lzs': '鲁智深'}
 * 修改
    dict1["a"]='你好'
    print(dict1)
    输出结果：{'a': '你好', 's': 'f', 'lzs': '鲁智深'}
    
 * 删除元素
      del dict1["a"]
      print(dict1)
      输出结果：{'s': 'f', 'lzs': '鲁智深'}
 * 删除整个字典
     del dict1
     
* 序列操作
    dict1 ={"yz":"圆通","zt":"中通"}
    result ="zt" in dict1
    print(result)
    输出结果：True
    result ="zt" not in dict1
    输出结果：Falese
 * 序列操作的四个函数
     len()获取字典的元素个数
         result=len(dict1)
         print(result)
         输出结果：2
         
         dict1={24:"a",25:'2',123:"2"}
     max()
         maxresult =max(dict1)
         输出结果：123
     
     min()
         maxresult =min(dict1)
         输出结果：24
         
     dict()
    
 * 遍历操作
     dict1={24:"a",25:'2',123:"2"}
     for..in 循环
      for i in dict1:
        print(i)
        print(dic1[i])
    输出key结果：24，25，123   
    输出value结果:a,2,2
   
   直接遍历键值对
   for key,value in dict1.items():
       print(key,   vaule)
    输出结果：
       24 a
       25 2
       123 2
  * 字典推导式
     dict1={24:"a",25:'2',123:"2"}
     result ={key:value for key,value in dict1.items()}
     输出结果：{24: 'a', 25: '2', 123: '2'}
   * 带有运算的推导式
       result ={key:"--"+value for key,value in dict1.items()}
    输出结果：{24: '--a--', 25: '--2--', 123: '--2--'}
    
   * 带有判断的推导式
       result ={key:value for key,value in dict1.items() if key !="24"}
    输出结果：{25: '2', 123: '2'}
   
   * 多循环的推导式
     dict1 ={'a':'1','b':'2','c':'3'}
     dict2 ={'aa':'11','bb':'22','cc':'33'}
     result ={k11 +k2 :v1+v2 for k1,v1 in dict1.items() for k2,v2 in dict2.items()}
     print(result)
     打印结果：{'aaa': '111', 'abb': '122', 'acc': '133', 'baa': '211', 'bbb': '222', 'bcc': '233', 'caa': '311', 'cbb': '322', 'ccc': '333'}
     
   * 带有判断条件的多循环推导式
       result ={k1+k2:v1+v2 for k1,v1 in dict1.items() for k2,v2 in dict2.items() if k1=='a' and k2 =='cc'}
       print(result)
       打印结果：{'acc': '133'}

 * 字典函数
  * clear()清空字典
    dict1 ={'a':'1','b':'2','c':'3'}
    dict1.clear()
    print(dict1)
    打印结果:{}
    
  * copy()复制字典
    dict2 =dict1.copy()
    print(dict2)
    打印结果：{}
    
  * fromkeys()使用指定的序列和固定的值组成字典
    lists =['手机','充电宝','充电线','插座']
    result ={}.fromkeys(lists,"手机配件")
    print(result)
    打印结果：{'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}

  * get()获取字典的值
    dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}
    result=dict1.get("手机")
    print(result)
    打印结果：手机配件
    如果dict1['momo']
    直接报错
    可以
    result=dict1.get('momo','aa')
    打印结果：aa
    
  * items()获取键值组成的二级列表
    dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}    
    result =dict1.items()
    print(result)
    打印结果：dict_items([('手机', '手机配件'), ('充电宝', '手机配件'), ('充电线', '手机配件'), ('插座', '手机配件')])

  * keys()将字典的所有键组成的列表
     打印结果：dict_keys(['手机', '充电宝', '充电线', '插座'])

  * values()将字典的所有值组成的列表
     打印结果：dict_values(['手机配件', '手机配件', '手机配件', '手机配件'])

  * pop()移除字典中的指定的元素
     dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}    
     
     删除已经存在的键
     dict1.pop('手机')
     print(dict1)
     打印结果：{'充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}
     
     删除不存在的键
     dict1.pop('momo')
     打印结果：报错
     设置默认值
     dict1.pop('momo','馒头')
     result =dict1.pop('momo','馒头')
     print(result)
     打印结果：馒头

   * popitem() 移除字典中的键值对 注意：字典为空会报错
     dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}    
     dict1.popitem()
     print(dict1)
     打印结果：{'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件'}
     
   * setdefault()添加字典的值
     dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}  
     dict1['手机']='aa'
     print(dict1)
     打印结果：{'手机': 'aa', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}
     dict1.setdefault('leg','你好')
     打印结果：{'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件', 'leg': '你好'}
     
   * update()更新字典的值
     dict1= {'手机': '手机配件', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}  
     dict1.update(手机='哈哈哈')
     print(dict1)
     打印结果：{'手机': '哈哈哈', '充电宝': '手机配件', '充电线': '手机配件', '插座': '手机配件'}

     dict1.update({'手机':'buubu','充电宝':"dadasdas"})
     打印结果：{'手机': 'buubu', '充电宝': 'dadasdas', '充电线': '手机配件', '插座': '手机配件'}
 
 

# 集合操作
* 创建空集合
 sets =set{}
 * 创建具有多个数据的集合
     sets ={1,2,2,3,5,6,7}
     print(sets)
     打印结果：{1, 2, 3, 5, 6, 7}
 * 集合可以使用的数据
     sets ={'大',123,True,1+2j}
     不能放列表,不能放集合
     
 * 集合的基本操作
  没有任何的基本操作
 
 * 序列操作
  * 成员检测
   sets ={'刘文','张玮','刘海','王者','或者','你好'}
   result ='刘文' in sets
   result ='刘文' not in sets
   print(result)
   打印结果：True Falese
   
 * 序列函数
  * len 检测集合长度
       result =len(sets)
       print(result)
       打印结果：6
  * max & min 获取最大值 最小值
       sets={1,5,3,123,12}
       maxVaule =max(sets)
       minVaule =min(sets)
       打印结果：123 1

  * 集合的遍历
     sets ={'刘文','张玮','刘海','王者','或者','你好'}
     for i in sets:
       print(i)
  * 二级集合
    sets ={
    {
    ('刘文','dad'),
    ('张玮','刘海'),
    ('王者','或者'')
    }
    }
 打印结果：
    刘文 dad
    张玮 刘海
    王者 或者
    
  * 长度不等的二级集合
  sets ={
    ('刘文','dad','eqeqw'),
    ('张玮','刘海'),
    ('王者','或者')}
    for v1 in sets:
        for i in v1:
            print(i)
     打印结果：
     刘文
     dad
     eqeqw
     王者
     或者
     张玮
     刘海
 * 集合的推导式操作
     sets ={1,2,351,123,123}
  * 推导式
      result ={i for i in sets}
      print(result)
      打印结果：{1, 2, 123, 351}
  * 带运算的推导式
      result ={i*3 for i in sets}
      打印结果：{369, 3, 1053, 6}
  * 带有判断调节的推导式
      result ={i for i in sets if i%3 ==0}
      print(result)
      打印结果：{123, 351}
  * 多循环推导式
      sets1={2,4,6,8}
      sets2={1,3,5,7}
      result ={i+j for i in sets1 for j in sets2}
      print(result)
      打印结果：{3, 5, 7, 9, 11, 13, 15}
  * 带有判断的多循环推导式
      sets1={2,4,6,8}
      sets2={1,3,5,7}
      result ={i+j for i in sets1 for j in sets2 if len(i) ==len(j) and len(i) ==2}
      打印结果：{'8877', '1177'}

 * 集合函数
     sets={'张玮','说的','大神'}
  * add()向集合中添加值（只能一次添加一个）
     sets.add('we')
     print(sets)
     打印结果：{'we', '说的', '大神', '张玮'}
  * pop()随机删除集合中的值
     sets.pop()
  * remove()移除集合中的指定的值（数据不存在会报错）
     sets.remove('we')
     print(sets)
     打印结果：{'说的', '大神', '张玮'}
  * discard()移除集合中的指定的值（数据不存在则不移除）
      sets.discard('说的')
      print(sets)
      打印结果：{'we', '大神', '张玮'}
  * clear()清空集合
      sets.clear()
      打印结果：set()
  * copy()复制集合
     result = sets.copy()
     print(result)
     打印结果：{'we', '说的', '大神', '张玮'}
     
  * difference()差集
     set1={'张玮','说的','大神','we'}
     set2={'咋办','式','安徽'}
     result =set1.difference(set2)
     
  * difference_update()差集更新操作
    set1={'张玮','说的','大神','we'}
    set2={'咋办','式','安徽','说的'}
    set1.difference_update(set2)
    print(set1)
     
  * intersection() 交集
      set1={'张玮','说的','大神','we'}
      set2={'咋办','式','安徽','说的'}
      result= set1.intersection(set2)
      print(result)
  打印结果：{'说的'}
  * intersection_update() 交集
      set1.intersection_update(set2)
      print(set1)
      打印结果：{'说的'}

  * union()并集
      set1={'张玮','说的','大神','we'}
      set2={'咋办','式','安徽','说的'}
      result =set1.union(set2)
      print(result)
      打印结果：{'咋办', '安徽', 'we', '大神', '张玮', '说的', '式'}
  * update()并集更新
      set1.update(set2)
      print(set1)
      打印结果：{'咋办', '安徽', 'we', '大神', '张玮', '说的', '式'}
      
  * 超集子集运算
   * issuperset()检测一个集合是不是另外一个集合的超集
      set1={'蓝天','白云','农妇','山泉','田'}
      set2={'农妇','山泉'}
      result =set1.issuperset(set2) 集合1是集合2的超集
      打印结果：True
   * issubset()检测一个集合是不是另外一个集合的子集   
      result =set2.issubset(set1) #set2是不是set1的子集
      print(result)
      打印结果：True
      
  *  isdisjoint  检测俩个集合是否相交
     set1 ={1,2,3,4,5}
     set2 ={'a','b','c','d','f'}
     result =set1.isdisjoint(set2)
     print(result)
     打印结果：True
     
  * symmetric_difference()对称差集操作
       格式：集合1.symmetric_difference(集合2)
       返回值：集合
       操作过程：将集合1和集合2不相交的部分组成新的集合
   
  * symmetric_difference_update 对称差集更新操作

  ps:创建空的冰冻集合
    fset =frozenset()
    print(type(fset))
    print(fset)
    打印结果：
    <class 'frozenset'>  frozenset()     
    
  创建具有元素的冰冻集合
  fset =frozenset(['老大','老二','老三','老五'])
    print(type(fset))
    print(fset)
    打印结果：<class 'frozenset'>
        frozenset({'老大', '老三', '老五', '老二'})
 * 遍历冰冻集合
   for i in fset:
       print(i)
       
 * 尝试修改无从下手
 
 冰冻集合推导式 代表结果是个列表
 result ={i for i in fset}
 print(result)
 打印结果：{'老大', '老2二', '老三', '老五'}
 
 * 冰冻集合的函数
 copy()复制集合
 difference()计算俩个集合的差集
 intersetion()计算俩个集合的交集
 union()计算俩个集合的并集
 symmetric_difference()对称差集
 isdisjoint()检测是否具有交集
 is

 

 

# 文件操作
 *  (w模式)文件写入操作
  * 1.打开或者创建文件(不存在创建文件，存在则打开文件，清空文件内容，再写入内容)
    fb =open('1.txt','w')
    print(fb)
    
  * 2.向文件中写入信息
    fb.write('一生一世')
    
  * 3.关闭文件
    fb.close()
    
 * a模式 打开文件或者创建文件
    append/add(文件已存在咋打开文件,在文件末尾追加内容)
    fp =open('21.txt','a')
    fp.write('aaaaaa')
    fp.close()
   
 * x模式 xor模式(文件存在则报错，文件不存在则新建文件，再写入内容。每次都是新文件)
    fp =open('22.txt','x')
    
 * r模式 read模式 打开文件 文件存在咋打开，文件不存在咋报错
  * 打开文件
    fp.open('22.txt','r')
  * 读取文件
    txt =fp.read()
    print(txt)
  * 关闭文件
    fp.close()
    
 * b模式 binary模式(二进制文件，辅助模式不能单独使用，必须配合w,a,x,r +b模式实用)
  * 打开文件
    fp =open('24.txt','rb')
    
  * 读取操作
    txt =fp.read()
  * 关闭文件
    fp.close()
    输出结果：b'aaaa'
  
* +模式 plus模式
 * 打开或者新建文件
    fp =open('25.txt','w+')
 * 移动文件指针（光标）返回文件开始的位置
    fp.seek(0)  
 * 写入文件
    fp.write('你啊下达大大大神大')

 * 读取文件
     txt =fp.read()
     print(txt)
 * 关闭文件
     fp.close()
 * read() 读取文件信息
 * 读取指定长度的信（字符个数）
     txt =fp.read(5)
 * write 写入文件操作
    fp =open('31.txt','a')
    fp.write('斜日呢啊')
    fp.close()
    
 * readline() 一次读取一行文件
    fp =open('33.txt','r')
    txt =fp.readline()
    print(txt)
    fp.close()
    
    循环读取所有行数
    while True:
     line =fp.readline()
     #判断是否为空字符串
     if len(line)==0
       break
     else:
       print(line)
  fp.close
 * readlines 将所有行读取到一个列表当中取
    fp =open('33.txt','r')
    lines =fp.lines()
    print(lines)
    fp.close
 * writelines()将一个序列中的信息写入文件
    fp=open('33.txt','w')
    lists =[
         '2313131',
         '大大说的',
         'dad'
    ]
    fp.writelines(lists)
    fp.close()
 
 * truncate() 文件截取操作
    fp.open('34.txt','r+')
    result=fp.truncate(5)
    print(result)
    fp.close
 * tell() 获取当前指针的位置
    fp.open('34.txt','r+')
    pos =fp.tell()
    print(pos)
    fp.close()
   
 * seek()便宜指针位置
    fp =open('4.txt','r')
    改变指针文职
    fp.seek(4)
    txt =fp.read(4)
    fp.close 
    
      
  
    

# OS模块文件及目录操作
* OS操作系统的简称 OS模块就是对操作系统进行操作
 * 使用该模块必须先导入模块：
     import os
## OS模块中的函数
 * getcwd()获取当前的工作目录
   格式：os.getcwd()
   返回值：路径字符串
 * chdir()修改当前工作目录  
   格式：os.chdir()
   返回值：None
 * listdir()获取指定文件夹中的所有文件和文件夹组成的列表
   格式:os.listdir('目录路径')
   返回值：目录中内容名称的列表
 * mkdir()创建一个目录/文件夹
   格式：os.mkdir(目录路径)
   返回值:None
 * rmdir()移除一个目录（必须是空目录）
   格式：os.rmdir(目录路径)
   返回值：None 
 * makedirs()递归创建文件夹
   格式：os.makedirs(路径)
   返回值：
 * removedirs()递归删除文件夹
   格式：os.makedirs(路径)
   返回值：None
   注意：例如：删除D:/a/b/c 如果abc文件夹中除了路径显示的文件夹之外没有任何其他文件或者文件夹，removedirs会移除掉所有文件夹a,b,c如果a,b,c任意文件夹中包含其他文件和文件夹，则该文件夹不会被删除。如果是最底层c文件夹则会爆出非空错误
 * rename()修改文件和文件夹的名称
   格式：os.rename('源文件或文件夹','目标文件或文件夹')
   返回值：None
 * stat()获取文件的相关信息
   格式：os.stat(文件)
   返回值：os.stat_result(st_mode=33188, st_ino=8592227827, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=0, st_atime=1516606657, st_mtime=1516605051, st_ctime=1516606649)
   注意：st_atime 访问时间 st_mtime修改时间  st_ctime创建时间
 
 * system()执行系统shell命令
   格式：os.system()
   返回值：整形
 * getenv()获取系统环境变量
   格式：os.getenv(获取的环境变量名称)
   注意：putenv确实可以添加成功，但是无法使用正常的getenv检测到
 * putenv()设置系统环境变量
   格式：os.putenv('环境变量名称',值)
 * exit()退出当前执行命令,直接关闭当前操作
   格式：exit()
   
## os.environ模块
 * os.environ 可以直接获取所有环境变量的信息组成的字典。如果希望更改环境变量，并且可以查询得到。就需要os.environ进行操作
   该模块的所有方法均是字典的方法。可以通过字典的os.environ的结果进行操作。
 * 无论使用os.getenv putenv 还是使用os.environ进行环境变量的操作，都是只对当前脚本，临时设置，无法直接更新或者操作系统的环境变量设置。
   
 * os.path 代表一个子模块
 * os.curdir 当前目录(相对路径) 返回值:.
 * os.pardir 上一层文件夹 返回值:..
 * 创建文件
  #fp.open('./my.txt','w') .可以省略 相对路径
   fp =open('/Users/zhangwei/Desktop/测试/111.txt','w')绝对路径
   fp.close()
   fp.open('../die.txt','w') ..不可以省略
   fp.close()
 * os.name  当前系统的内核名称 windows nt  linux/unix(苹果系统)  posix
 * os.sep 获取当前系统的路径分隔符号 windows是\  unix是/
 * os.extsep 获取当前系统中文件名和后缀名之间的分隔符  都是.
 * os.altsep 
 * os.linesep  获取系统换行符合  windows是:\r\n  linux/unix是:\n

## os.path模块
 * os.path是os模块中的子模块，包含很多和路径相关的操作
### 函数部分
* 获取当前路径并且转化为绝对路径
* abspath() 将一个相对路径转化为绝对路径
 * path =os.curdir
   abspath =os.path.abspath(path)
   print(abspath)
* basename()获取路径中的文件夹或者文件名称（只要路径的最后一部分）
* dirname() 获取路径中的路径部分（除去最后一部分）
 * path ='/Users/zhangwei/Desktop/测试/aaa.txt'
   result1 =os.path.basename(path)
   print(result1)
   result2 =os.path.dirname(path)
   print(result2)
   打印结果：aaa.txt   /Users/zhangwei/Desktop/测试
 * join()将俩个路径合成一个路径
   格式：os.path.join(路径1，路径2)
   返回值：合并后的路径
   result =os.path.join(result2,result1)
 * split() 将一个路径切割成文件夹和文件名部分
  * path ='/Users/zhangwei/Desktop/测试/aaa.txt'
    result =os.path.split(path)
    print(result)
    打印结果：('/Users/zhangwei/Desktop', '测试')
    


# tarfile模块 文件打包模块
# 压缩文件方法
 * 打开或者创建压缩方法（要压缩的地址）
    '''
    tp =tarfile.open('/Users/zhangwei/Desktop/333.tar','w:bz2')
* 添加文件(要压缩文件的地址 ，存进去后的名称)
    tp.add('/Users/zhangwei/Desktop/测试/aaa.txt','33.txt')
    tp.add('/Users/zhangwei/Desktop/测试/aa.pdf','fm.pdf')
    tp.add('/Users/zhangwei/Desktop/测试/01.py','calc/jsq.py')
* 关闭压缩文件
    tp.close()
    '''
* 解压软件
* 打开压缩软件
    tp =tarfile.open('/Users/zhangwei/Desktop/333.zip','r:bz2')

* 解压操作

* 解压所有文件操作
* tp.extractall('/Users/zhangwei/Desktop/jieya')

* 解压指定文件
 tp.extractall('/Users/zhangwei/Desktop/jieya',['fm.pdf','33.txt'])

* 解压单个文件
    tp.extract('fm.pdf','/Users/zhangwei/Desktop')
* 关闭解压软件
    tp.close()

# zipfile模块	文件压缩模块
  * 引入import zipfile
  * 打开或者创建zip文件
     #打开或者创建zip文件 文件路径。打开文件模式，压缩编码（压缩还是不压缩）  超过64G（64位） zipfile.ZIP_STORED 只归档不压缩。
     #zipfile.ZIP_DEFLATED 文件压缩
# zp =zipfile.ZipFile(file,,p)
  * zp =zipfile.ZipFile('/Users/zhangwei/Desktop/pyaa.zip','w',zipfile.ZIP_DEFLATED)
    print(zp)

  * 文件添加操作
  * 向压缩文件添加内容（文件或者目录）哪个文件  叫什么名
    zp.write('/Users/zhangwei/Desktop/01.py','01.xx')
    zp.write('/Users/zhangwei/Desktop/04.py','04.xx')
  * 关闭文件
    zp.close()
    '''
    解压操作
    打开压缩ZIP文件
    zp =zipfile.ZipFile('/Users/zhangwei/Desktop/py00.zip','r')

    #解压文件
    #解压所有文件 解压到哪
 * zp.extractall('/Users/zhangwei/Desktop/测试',['01.xx'])

 * 解压所有文件 解压指定文件列表
 * zp.extractall('/Users/zhangwei/Desktop/测试')

 * 解压一个文件
 * zp.extract('01.xx','/Users/zhangwei/Desktop/测试/test')

 * 关闭压缩文件
  zp.close()
 *   

# shutil模块	高级文件和目录处理
 * copy()复制文件
 result =shutil.copy('./1.txt','./test/hhah.txt')
 print(result)
 打印结果：./test/hhah.txt

 * copy2()复制文件，保留元数据
 
 * copyfileobj 将一个文件内容拷贝到另一个文件当中(打开当前文件夹下的01.py)
    result =shutil.copyfileobj(open('./01.py','r'),open('./test/05.py','w'))
    print(result)
    
 * copyfile()将一个文件内容拷贝到另一个文件当中
   result =shutil.copyfile('./01.py','./test/7.py')
   print(result)
 * copytree()  复制整个文件目录
   result =shutil.copytree('/Users/zhangwei/Desktop/插件','/Users/zhangwei/Desktop/测试1')
   print(result)
 * copymode()拷贝权限
 * copystat()拷贝数据（状态）
 * rmtree()移除整个目录，无论是否空
 * move()移动文件或者目录
   格式：move(来源地址，目标地址)
   result =shutil.move('./1.txt','./test/11new.txt')
   print(result)
 * which()检测命令对应的文件路径
   result =shutil.which('ping')
   print(result)
   打印结果：/sbin/ping
 * disk_usage()检测磁盘实用信息
   result =shutil.disk_usage('/Users/zhangwei')
   print(result)

 

# 时间和日期相关的模块
* 日历模块
 import calendar
 
* calendar()获取一年 份的完整日历
* result =calendar.calendar(2017,w=2,l=2,c=7,m =4)
* print(result)

* month() 获取一个月的日历
* result =calendar.month(2017,10,w=3,l=2)
* print(result)

* monthcalendar()获取一个月的矩阵列表
* result =calendar.monthcalendar(2017,8)
* print(result)
'''
'''
[
  [ 0,  1,  2,  3,  4,  5,  6],
  [ 7,  8,  9, 10, 11, 12, 13],
  [14, 15, 16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25, 26, 27], 
  [28, 29, 30, 31,  0,  0,  0]
]
'''
'''
* isleap()检测是否是闰年(如果不是100的整数倍，被4整除就是闰年，如果是100的整数倍，需要被400整除)
* result =calendar.isleap(2017)
* print(result)

* leapdays()检测指定年份之间的闰年个数
* 格式：calendar.leadays(开始年份，结束年份)
* result =calendar.leapdays(2000,2008)
* print(result)

* monthrange()获取一个月的周几开始及当月天数
* 格式：calendar.monthrange(年，月)
* result =calendar.monthrange(2017,8)
* print(result)
* 打印结果：(1, 31) 从周二开始 31天

*weekyday() 根据年月日计算周几
* 格式：calendar.weekday(年，月，日)
* result =calendar.weekday(1997,7,1)
* print(result)
* 返回结果：0-6 周一到周天

* timegm()将时间元转化为时间戳
* 格式：calendar.timegm(时间元组)
* 返回值：时间戳 1997年7月1号12点30分45秒
* timetuple =(1997,7,1,12,30,45,0,0)
* result =calendar.timegm(timetuple)
* print(result)
* 返回值：867760245


# time模块

* 时间戳
 * 从（1970年1月1日开始计算）
 * 能够使用到2018年的某一天
 * 如果使用太远的未来或者1970年以前的时间可能出现异常
 
* UTC时间
 * 世界协调时间（格林尼治时间）
 
* 夏令时（就是通过夏季时间调快一个小时，来提醒大家早睡早起身体好，节省蜡烛）每天的始终变   成了25小时，注意本质还是24小时
#时间元组就是一个用来表示时间的元组
'''
 （年，月，日，时，分，秒，周几，一年中的第几天，夏令时）
 
'''
* 导入时间模块 time
* timezone
* print(time.timezone) #得到一个秒数 和格林尼治标准时区差的秒数

* altzone 获取当前时区与格林尼治所在时区的相差秒数，再有夏令时的情况下
* print(time.altzone)

* daylight 检测是否是夏令时的状态， 0是 1不是
* print(time.daylight)

* 时间模块的函数
* asctime()返回一个正常的可读的时间字符串(英文)
* 格式：time.asctime(时间元组)*获取当前时间字符串
* result =time.asctime()
* 获取指定时间字符串
* result =time.asctime((1997,7,1,0,0,0,0,0,0))
* print(result)
* 打印结果：Mon Jul  1 00:00:00 1997

* localtime.localtime()获取指定时间得时间元组格式
* 获取当前时间得时间元组
* result =time.localtime()
* 获取指定时间戳的时间元组
* result =time.localtime(0)
* print(result)
* 打印结果：time.struct_time(tm_year=2018, tm_mon=1, tm_mday=23, tm_hour=15, tm_min=48, tm_sec=51, tm_wday=1, tm_yday=23, tm_isdst=0)

* gmtime()获取指定时间的时间元组格式（UTC）
* 获取当前时间的时间元组
* result =time.gmtime()
* 获取指定时间的时间元组
* result =time.gmtime(0)
* print(result)
* 打印结果：time.struct_time(tm_year=2018, tm_mon=1, tm_mday=23, tm_hour=7, tm_min=52, tm_sec=52, tm_wday=1, tm_yday=23, tm_isdst=0)

*  ctime()获取本地时间的字符串格式
*  获取当前时间的刻度字符串格式（英文）
*  result =time.ctime()
*  获取指定时间戳的可读字符串格式
*  result =time.ctime(0)
*  print(result)
*  打印结果：Tue Jan 23 15:55:15 2018

* mktime() 根据时间元组制作时间戳
* tt =(1999,12,12,0,0,0,0,0,0)
* result =time.mktime(tt)
* print(result)

'''
* clock()获取CPU执行的时间 适合Python3.3以下版本
'''
* result =time.clock()
* print(result)
'''
* 开始执行程序
* 第一次执行程序
  start =time.clock()

* 程序执行中
  time.sleep(5)
* 程序执行完毕
  end =time.clock()
  result =end- start
  print('程序执行时间为：{0}秒'.format(result))
'''


'''
* pref_counter()获取CPU执行的时间 适合Python3.3以上版本
* 第一次执行
* 第一次执行程序
  start =time.perf_counter()

* 程序执行中
* time.sleep(5)
  end =time.perf_counter()
* 程序执行完毕
  result =end- start
  print('程序执行时间为：{0}秒'.format(result))

* sleep() 程序睡眠，使得程序在此处等待指定的时间
* 格式：time.sleep(时间秒数)

'''
* time()获取本地时间戳
* result =time.time()
* print(result)

'''
* strftime() 把一个时间元组格式化一个字符串
  tt =(2017,8,1,11,52,0,0,0,0)
* 将当前时间转化为指定的字符串格式
* result =time.strftime('%Y-%m-%d %H:%M:%S')
* 将指定的时间转化为指定的字符串格式
  result =time.strftime('%Y-%m-%d %H:%M:%S',tt)
  print(result)
'''
* strptime() 把一个字符串中的时间提取到时间元组当中去
  strtime ='7/1/1997 12:38:15'
  result =time.strptime(strtime,'%m/%d/%Y %H:%M:%S')
  print(result)
* 打印结果：time.struct_time(tm_year=1997, tm_mon=7, tm_mday=1, tm_hour=12, tm_min=38, tm_sec=15, tm_wday=1, tm_yday=182, tm_isdst=-1)


