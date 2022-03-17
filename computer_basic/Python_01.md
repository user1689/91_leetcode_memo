

### NetworkProgramming

#### UDP

```python
'''	
		IP/端口
    1- 网络就是用来**信息共享**和**数据传递**
    2- ip就是标识收件人和发件人的地址，跟发手快递类似
    3- ip = 网络号 + 主机号， 类似于身份证号130124XXXXXX
    4- 一个字节byte = 8 bit比特位， 比特位就是存放0/1的小格子
    5- ipv4 四个字节存放ip地址，32个格子， 共2^32次方 [网络号].[网络号].[网络号].[主机号]
    6- ipv6 是ip的第六个版本，但是使用的是**8个字节**
    7- ping www.baidu.com 查看网络通不通，和查看百度的ip地址
    8- DNS域名解析系统 域名 <=> ip数字地址
    9- 一个程序运行起来就是一个进程，打开任务管理器查看各个进程
		10- ip:端口号 来标记对应程序 eg:192.168.1.2:7788 进入指定程序
		11- dest ip/ scr ip/ dest port/ src port + content
		12- 程序运行了叫做进程 没运行的叫做程序 
		13- 端口号范围是0-65535 知名端口号范围是[0,1024) 端口大于1024随便用也称为动态端口 
		
		linux command a 快速回到行首 
 		linux command e 快速回到行末 
		linux command c 退出程序
		linux exit() 退出交互模式
  	python3 / ipython3 打开交互模式
'''

'''
		编码
    1- encode编码成字节或者二进制类型, 默认参数就是encoding="utf-8"
    2- decode解码为原始数据
'''
a_str = "我是Python"
b_str = a_str.encode(encoding="utf-8")
print("数据类型：%s, 数值为：%s" % (type(b_str), b_str))

c_str = b_str.decode(encoding="utf-8")
print("数据类型：%s, 数值为：%s" % (type(c_str), c_str))

'''
		初识socket
'''
import socket
# socket.socket(AddressFamily, Type)
# 创建tcp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import socket

# 创建UDP的socket(ip协议类型ipv4 or ipv6， socket的类型) --> socket对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 将端口绑定到这个socket上, ip写""表示绑定本地所有的ip的数据
udp_socket.bind(('', 8888))

# 使用socket进行数据的发送
data = input("请输入你想要对服务器说的话：")
ip_address = "192.168.115.81"
port_num = 8080
udp_socket.sendto(data.encode(encoding="utf-8"), (ip_address, port_num))

# 进行数据的接收recvfrom --> 接收的data是一个元组类型（byte类型的data, (ip_address, port_num)）
recv_data, remote_address = udp_socket.recvfrom(1024)
recv_data = recv_data.decode("utf-8")
print("收到来自: %s 的数据：%s" % (str(remote_address),recv_data))

# 关闭socket
udp_socket.close()

'''
		UDP Socket 接受数据/客户端
		1- socket的端口需要绑定后才能接收数据 类似监听某端口
		2- 接收数据的大小可以设置
		3- 如果数据过大 会先接受一部分 再次调用receive才会返回剩余的部分
		4- udp是广播接受 所以bind的是ip写的是空 也就是本机ip 而不是具体的ip
		5- 先bind然后才能send和receive 顺序不能乱
		6- 发送端没有bind端口 系统会自动分配一个端口 但是如果程序关了又重新打开 会重新分配动态端口
		7- 同一个端口不允许被同一时间用两次
		8- socket可以同时收发数据
		9- 单工:100%只能往一个方向走 半双工:可以双向但是不能同时 全双工:同时可以收可以发 socket属于全双工
		10- echo回声服务器， 你给我发什么，我给你回什么
    11- UDP的特点： a:不保证不丢包 b:接收的data可能乱序
		
		window 数据都是gbk编码的 接受来自window的数据需要decode成gbk
		localaddr中必须绑定自己的信息
		vim control + n vim中补全代码
		linux control + c 退出当前程序
		linux tree + [dir] 列出目录树
		linux cp [local/file_location] [local/target_location]
		vim esc 进入命令模式
    vim 命令模式下 [行号] + G 直接跳转到行号
    vim 命令模式下 G 直接跳转到行末尾
    vim 命令模式下 yy 复制本行 p黏贴
    vim 命令模式下 A 跳转到本行行末 I 跳转到本行行首 并且直接变成编辑模式
    linux control + shift + t 开新窗口
		私有ip和公有ip
		192.168.1.1属于私有ip 自用 a/b/c三类ip当中都有一段范围作为私有ip
		vim 命令模式下 V 选中本行 D 剪切 P黏贴  
'''

import socket

# 创建服务器socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定接口
udp_server.bind(("", 8888))

while True:
    # 使用socket接收请求的数据
    recv_data, recv_address = udp_server.recvfrom(1024)

    # 回传数据
    udp_server.sendto(recv_data, recv_address)

# 服务器关闭socket并不重要
# udp_server.close()


'''
		UDP聊天器
'''
import socket

def send_msg(udp_socket):
    data = input("请输入你想要说的话:")
    ip_address = input("请输入目的地的ip地址:")
    port = int(input("请输入目的地的端口号:"))
    udp_socket.sendto(data.encode(encoding="utf-8"), (ip_address, port))

def recv_msg(udp_socket):
    recv_data, remote_address = udp_socket.recvfrom(1024)
    print("收到来自: %s 的数据：%s" % (str(remote_address), recv_data.decode(encoding="utf-8")))

def main():
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 8888))

    while True:
        op = input("请输入需要进行的操作: 1 发送数据 2 接收数据 3 退出")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "3":
            break
        else:
            print("你的输入有错,请重新输入...")

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
```



#### TCP

```python
'''
		很稳定 有应答机制 超时重传 错误校验 流量控制与堵塞管理
		服务器端收到一个客户端的connect才会继续执行accept后面的程序
		服务器端的accept会返回一个new_socket专门供connect它的客户端服务
		服务器端的recv也会堵塞等待客户端的send
		
		vim 当建立文件忘记命名的时候 :w [文件名] 新建文件
		\ 转义符号 比如想用括号作为命名
		vim 命令模式下 O 直接在光标上插入一行  o 直接在光标下插入一行
		linux mv 重命名
		linux mkdir 新建文件夹
		
		Recap
		udp(client/server)  tcp(client)       tcp(server)
		socket							socket						socket
		bind 								connect						bind
		sendto/recvfrom			send/recv					listen
		close								close							accept
																					recv/send
																					close 
																					
		服务器不绑客户端连不上
		为了保证客户端不会因为端口有问题 客户端一般不绑端口
		tcp是面向链接的通信 connect方法 类似电话
		udp是不需要链接的通信 类似写信
		listen 后的套接字是被动套接字 用来接收客户端请求的 accept返回的新套接字是标记新来链接的客户端的
		关不同的套接字会有不同的结果
		服务器解堵塞 1收到消息 2客户端关闭 通过判断返回的消息长度来判断即可
'''

'''
    # 文件传输客户端创建
    import socket

    def main():
      # create socket
      tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # connect server
      ip_addr = input("enter the ip of the server: ")
      port_num = int(input("enter the port of the server: "))
      tcp_socket.connect((ip_addr, port_num))

      # send request of download
      file_name = input("enter the name of file: ")
      tcp_socket.send(file_name.encode(encoding = "utf-8"))

      # receive file and write on local
      recv_data = tcp_socket.recv(1024)

      if (recv_data):
        with open("new " + file_name, "wb") as f:
          f.write(recv_data)

      tcp_socket.close()

    if __name__ == "__main__":
      main()
'''

'''
		# 文件传输服务器
    import socket

    def send_file_2_client(new_client_socket, client_addr):
      '''
      receive data
      open file and read data
      send data to client
      '''
      # receive file name
      file_name = new_client_socket.recv(1024).decode("utf-8")
      print("client %s want to download %s: " % (str(client_addr), file_name))

      file_content = None
      # oepn file
      try:
        f = open(file_name, "rb")
        file_content  = f.read()
        f.close()
      except Exception as ret:
        print("did not find file %s: " % file_name)

      if (file_content):
        # send file
        # new_client_socket.send("it is a file".encode("utf-8"))
        new_client_socket.send(file_content)

    def main():
      # create tcp_socket
      tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # bind port
      tcp_socket.bind(("", 7788))

      # transfer active to passive
      tcp_socket.listen(128)

      while True:
      	print("wait client... ")	
        # wait information from client
        new_client_socket, client_addr = tcp_socket.accept()
        print("%s client connected " % str(client_addr))

				send_file_2_client(new_client_socket, client_addr)

        print("client " + str(client_addr) +  " losed connection")		
        new_client_socket.close()	

      # close socket
      tcp_socket.close()


    if __name__=="__main__":
      main()
  
'''


'''
    TCP 三次握手原理：
    1- client -> server 我可以和你吃饭吗? server收到客户端的SYN
    2- server -> client 好的 回复ACK允许建立连接
    3- client -> server 开始发送信息
    如果缺少第三部，客户端迟迟没有开始通信，称为未完成三次握手的半链接状态
    服务器一般有未完成三次握手的队列和完成三次握手的队列
    第三部完成后，系统将半连接的客户端连接从未完成队列移动到已完成的队列中
    listen(128)的参数，不同平台参数的表示含义不同
    linux中已完成三次握手的队列长度
    在其他平台一般指 未完成 + 已完成队列的中长度
    accept的含义：从已完成的队列中取出一个客户端进行服务

    Tcp四次挥手拜拜断开连接close的原理：(断开连接会有30s-2min的延迟想一会的断开时间)
    1- 一端 -> 另一端 咱们分手吧 发送FIN和ACK
    2- 另一端 -> 一端 会想一会,发送ACK
    3- 另一端 -> 一端 会想一会,发送FIN
    4- 一端 -> 另一端 好的，断开连接通知对方，发送ACK
    
    # 设置socket断开连接的选项,close的时候会立即释放，答应断开分手，1表示确定，0为取消
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    TCP/IP协议并不是单一的协议，而是一族协议
    在TCP/IP协议中简单的划分了四层：应用层，运输层，网际层，网络接口层
    而在OSI协议中有7层：应用层，表示层，会话层，传输层，网络层，数据链路层，物理层
'''
```



### 多任务

#### 线程

```python
'''
		线程 
		vim 命令模式下 dd删一行 dw是删当前光标的单词 u是撤销
		vim 命令模式下 w 跳一个单词 d 往回跳一个单词
		单核cpu 多任务 使用时间片轮转/优先级调度 任务数多于cpu的核数 并发
		多核cpu 多任务 并行
		
		当调用thread的时候不会创建线程 只有当实例化以后的调用其start方法才会创建新的线程
		
		创建线程有两种方式 一种是直接传入方法 另一种是写一个类继承threading.Thread并且重写run方法 然后要创建线程的时候就实例化一下 调用其start方法
		class MyThread(threading.Thead):
				def run():
					...
		def main():
				t = MyThread()
        t.start()
		
		target指定将来 这个线程去哪个函数执行代码
		args指定将来调用函数的时候 传递什么数据过去
		threading.Thread(target = function_name, args = (variable,))
		
		多线程共享全局变量可能会出问题
		因为比如一个全局变量 g+=1 在执行的时候会被拆解成很多步骤 
		比如被拆为	1获取g值 2增加g的值 3存储g的值
		那么可能在第3步的时候恰好被其他线程占用了 那么可能会导致结果不正确
		
		原子性 要么不做要么做完
		互斥锁可以解决多线程共享变量出现问题的情况
		
		# 创建锁
		mutex = threading.Lock()
		
		# 锁定
		mutex.acquire()
		
		# 释放
		mutex.release()
		
		锁可能会出现死锁，比如可以添加操作时间来避免死锁
'''


```

#### 进程

```python
'''			
		进程
		它是操作系统分配资源的基本单位
		不运行的叫程序 运行的叫进程
		程序在没运行的时候没有资源 运行的程序占用资源
		进程的三种状态 运行 就绪 等待
	
		用进程实现多线程
		import multiprocessing
		p = multiprocessing.Process(target=method_name)
		p.start()
	
		进程耗费的资源大 由于把主进程的资源都拷贝过去了 (父亲有的资源孩子都有) 
		涉及到写时拷贝 (了解即可)
		
		vim 命令模式下 V选中 + : + normal + i + # 快速多行注释
		linux control + shift + t 创建新窗口
		linux ps 观察运行进程 PID标记一个进程
		linux kill + PID 杀死进程
		如果vim 编辑到一半没了 那么使用linux ls -a查看系统创建的隐藏文件 删除即可
		linux ls -a 显示隐藏文件夹
		
			线程     vs     进程
		 轻量级       一堆资源/代码的总称
在一个资源下多箭头	 多个资源的多箭头
	线程不能独立执行  进程可以独立执行
	必须存在在进程中
	
		线程之前共享全局变量进行通信
		那么进程如何通信? 
		socket/本地文件/queue
		
		进程之间通信
		form multiprocessing import Queue
		q = Queue(3) # 新建队列
		q.put("3") # 放数据
		q.get() # 取数据
		q.full() # 判断是否为满
		q.empty() # 判断是否为空
		用Queue可以解耦(耦合性)
		局限性在于只能用于一台电脑之间的进程进行通信
		
		进程池
		创建进程池
		from multiprocessing import Pool
		import os, time, random
		
		po = Pool(3)
		# 每次都会用空闲出来的子进程去调用目标
		# Pool().apply_async(需要调用的函数, 需要传递的参数)
		Pool().apply_async(worker, (i, ))
		po.close()
		# 通过threading创建的进程 主进程会等待子进程结束以后再结束
		# 通过multiprocessing创建的进程 主进程不会等待子进程结束后再结束
		po.join() # 可以使主进程等待子进程结束以后再结束
		
		vim 命令模式下 V选中 + < + . 重复上次的命令 可以多次对其
		linux gedit 用编辑器打开文件
		ipython import os + os.__file__ 直接找到python包地址
		
		os.listdir(文件路径)
		linux 删一个目录 rm 文件名 -r
'''



```

#### 协程

```python
'''
		协程
		
		迭代器
		from collections import Iterable
		True = isinstance(a, A) # 表示为A创建出来的a
		isinstance([11,22,33], Iterable)
		
		vim 文件名 + 空格+行号 直接跳转到目标行号
		
		实现 __iter__方法 返回一个迭代器(含有__iter__方法和__next__方法供增强for循环调用)
		一个东西可以迭代不一定是迭代器 一个迭代器一定可以迭代
		迭代器可以节省内存空间 什么时候用什么时候调用
		
		python2中
		range和xrange有什么区别
		range:存储生成的值
		xrange:存储生成值的方式 返回一个迭代器对象
		returns an object that generates the numbers in the range

		python3中
		range和xrange已经相同了
		
		linux ps -aux 查看linux进程
    vim :%s/要改的变量名/改成的变量名/g
    
'''
import time

class ClassMate:
    def __init__(self):
        self.names = []
        self.idx = 0
 
    def __iter__(self):
      return self
 
    def __next__(self):
        if (self.idx < len(self.names)):
            res = self.names[self.idx]
            self.idx += 1
            return res
        else:
            raise StopIteration
 
classmate = ClassMate()
classmate.names.append("jack")
classmate.names.append("sam")
classmate.names.append("tom")

for name in classmate:
    print(name)
    time.sleep(1)

'''
		fibonacci iterator
'''

class Fibonacci:
  	def __init__(self, total):
				self.total = total 
        self.curNum = 0
        self.a = 0
        self.b = 1 
    
    def __iter__(self):
      	return self 
    
    def __next__(self):
      	if (self.curNum < self.total): 
          	res = self.a 
          	self.a, self.b = self.b, self.a + self.b
          	self.curNum += 1
          	return res
       	else:
         		raise StopIteration
      
fib = Fibonacci(10)
for num in fib:
  	print(num)
    
'''	
		生成器 
		可以暂停函数的执行 什么时候想执行随时执行
		创建生成器的两种方式
		1- list comprehension -> 中括号换成小括号 -> 生成器
		2- yield 会暂停函数的执行 并返回数值 后继续执行剩下的部分
		可以使用next()方法来调用迭代器的__next__方法
		两个生成器之间没有影响
		出现异常后停止 此时如果想访问return回来的值 可以通过捕获异常后通过ret.value来访问

		通过send启动生成器 
		生成器.send(参数 可以当做yield的结果)
			
'''
def create_num(all_num):
  	a, b = 0, 1
    current_num = 0
    while (current_num < all_num):
      	ret = yield a
        print(">>>>>ret>>>>>", ret)
        a, b = b, a + b
        current_num += 1

obj = create_num(10)
ret = next(obj)
print(ret)

# 最好不要放在第一次调用 否则会崩 除非传递None作为参数
ret = obj.send("haha")
print(ret)

'''
		协程
		使用yield实现多线程
		协程使用的资源最少
		
		greenlet
		对yield进行了封装
		gr.switch()
		
		gevent
		是一个网络异步并发库
		g1 = gevent.spawn(想要执行的方法, 想要传递的参数)
		g1.join() # 延时操作 + gevent.sleep(时间)
		gevent遇到延时操作就会切换任务 从而实现多任务
		程序运行资源分配 线程执行代码 协程依赖于线程
		可以用gevent.monkey 中 monkey.patch_all()来打补丁使得可以直接使用原来的time.sleep()方法
		gevent.joinall([g1,g2,g3...])	
		
'''

'''
		使用协程实现udp图片下载器
		import urllib.request
		req = urllib.request.urlopen("http://www.baidu.com")
		req.read()

'''
import gevent
from gevent import monkey
monkey.patch_all()

def download(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
      	f.write(img_content)
        
def main():
		gevent.joinall([
      gevent.spawn(download, "1.jpg", "url")
      gevent.spawn(download, "2.jpg", "url")
    ])
    
if __name__ == "__main__":
  	main()
```



### Web Server

#### 正则表达式

```python
'''
		正则表达式
		
		import re
		result = re.match(r"正则表达式", "要匹配的字符串")
		result.group() # 可以获取匹配的数据
		
		\d 表示一个数字
		[1-8] or [12345678] or [1-36-8] 闭区间匹配 可以精确匹配也可以范围匹配 可以匹配一个数字
    \w 匹配小写字母大写字母数字和下划线 bug:范围有点广少用 中文可能也可以
		\s 匹配一个空白字符
		
		匹配单个字符，小写为正，大写为非正
    1- \d 匹配数字，即0-9
    2- \D 匹配非数字，即不是数字
    3- \w 小写，大写，数字，下划线，中文也行 (word)
    4- \W 匹配非(小写，大ß写，数字，下划线，中文)
    5- [] 匹配中括号中制定的一个字符
    6- \s 匹配空格(tab,space)
    7- \S 匹配非空格(tab,space)
    8- .  匹配任意一个字符，除了\n(换行) 传入re.S可以匹配上\n
    9- $  匹配结尾[a-zA-Z_][a-zA-Z_0-9]*$
   10- ^  匹配开头^[a-zA-Z_][a-zA-Z_0-9]*，默认就是^，可以略写
		
    匹配多个字符
    1- 单个字符后+大括号：\d{3} == \d\d\d  \d{3,4} = \d\d\d or \d\d\d\d
    2- 大括号只表示其前面的**单个字符**，而不是一坨
    3- 大括号中没有分隔符表示其中之一，有逗号的是或的关系
    
    1- {m}   匹配一个字符出现m次
    2- {m,n} 匹配一个字符出现m到n次
    3- ?     匹配一个字符出现1次或者0次都行，一次或者0次 -?
    4- *     匹配一个字符出现0次或者无限次都行，可有可无 -*
    5- +     匹配一个字符出现1次或者无限次都行，至少有一次 -+	
    6- ()    匹配一个group
    7- |     匹配group里的选择
    8- \1    匹配前面第一个gourp里的内容
    9- (?P<name>regx) 分组起变量名
    10- (?P=name)	分组通过变量名取变量
'''

import re
def main():
    names = ["age", "_age", "age!", "^a$#123"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if (ret):
            print("变量名:%s 符合要求" % name)
        else:
            print("变量名:%s 不符合要求" % name)
            
if __name__ == "__main__":
        main()

import re
def main():
  	email = input("enter email: ")
    # 如果在正则表达式中需要用到普通字符比如点,问号等需要在它们前面添加一个反斜杠
  	ret = re.match(r"[a-zA-Z_0-9]{4,20}@(163|126|gmail)\.com$", email)
    if (ret):
     		print("email:%s 符合要求" % email)
    else:
      	print("email:%s 不符合要求" % email)
        
if __name__ == "__main__":
  			main()
    
''' 
		 
		re模块高级用法
		search()	不会从头匹配 只要有就会返回
		findall()		直接返回数据 不用group
		sub(正则, 内容 or 函数引用, 被替换的内容) 替换已经匹配到的数据 支持多个替换
		split(正则, 要切割的内容) 切割后返回数组
		
'''
```

#### HTTP协议

```python
'''
		超文本传输协议
		基于Tcp
		
		...
		
		Tcp 三次握手
		syn 请求
		ack 应答
		
		网页链接的tcp建立需要三次握手，四次挥手拜拜，中大型网站都是长连接
		
		全双工 需要四次挥手拜拜 
		1- client 调用 close 客户端告诉服务器不会再给服务器发任何数据  
		2- new_socket close 服务器告诉客户端不会再给客户端发数据了 
		3- server 调用 close (2,3不能合并的 原因是有可能server迟迟不关闭 那么new_socket的close就一直不会被发送给client)
		4- client 关闭收通道 server 关闭发通道
		谁先调用close 谁的数据会先保留2分钟 那么当服务器先关闭 由于端口是绑定的 再次运行时候除非修改端口否则 会报错 此时可以使用
		tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
		
'''

import re
import socket

def service_client(new_socket):

	# receive request from chrome
	# GET / HTTTP/1.1	
	request = new_socket.recv(1024).decode("utf-8")
		

	request_lines = request.splitlines()
	# GET /index.html HTTP/1.1
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	
	file_name = ""

	if (ret):
		file_name = ret.group(1)
		if (file_name == "/"):
			file_name = "/index.html"
		
	try:
		f = open("./html" + file_name, "rb")

	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "-------------flie not found-------------"
		new_socket.send(response.decode("utf-8"))
	else:
		html_content = f.read()
		f.close()
	
		# return http package
		# header
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# send response header
		new_socket.send(response.encode("utf-8"))
		# send response body
		new_socket.send(html_content)
	
	
	new_socket.close()
		

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	tcp_server_socket.bind(("", 8888))
	
	tcp_server_socket.listen(128)
	
	while True:
		new_socket, client_addr = tcp_server_socket.accept()
		service_client(new_socket)
		
	
	tcp_server_socket.close()

if __name__ == "__main__":
	main()


'''	
		通过多进程实现http服务器
		linux 拷贝文件 cp 文件路径 ./ -r  (文件路径到当前路径)
		linux 全文更换 :%/想要换的/换成什么/g
		
		linux下一切都为文件 通过fd文件描述符来标记 就是一个数字 对应一个特殊的文件 例如网络接口
		创建子进程也拷贝了主进程的文件 此时主进程和子进程指向包含同一个fd的文件 如果只关闭子进程而不关闭主进程的文件 因为还有另外一个进程指向此fd文件 此文件不会被关闭 所以四次挥手就不会开始 浏览器会一直等待服务器来发消息
'''
import re
import socket
import multiprocessing

def service_client(new_socket):

	# receive request from chrome
	# GET / HTTTP/1.1	
	request = new_socket.recv(1024).decode("utf-8")
		

	request_lines = request.splitlines()
	# GET /index.html HTTP/1.1
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	
	file_name = ""

	if (ret):
		file_name = ret.group(1)
		if (file_name == "/"):
			file_name = "/index.html"
		
	try:
		f = open("./html" + file_name, "rb")

	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "-------------flie not found-------------"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
	
		# return http package
		# header
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# send response header
		new_socket.send(response.encode("utf-8"))
		# send response body
		new_socket.send(html_content)
	
	
	new_socket.close()
		

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	tcp_server_socket.bind(("", 8888))
	
	tcp_server_socket.listen(128)
	
	while True:
		new_socket, client_addr = tcp_server_socket.accept()
		
		p = multiprocessing.Process(target = service_client, args = (new_socket,))		
		p.start()
		
		new_socket.close()
	
		
	
	tcp_server_socket.close()

if __name__ == "__main__":
	main()

'''	
		使用多线程实现http服务器
		但由于用线程创建的多任务不会复制文件 多线程里共享文件 所以主线程不需要立刻调用close方法 
'''
import re
import socket
import threading

def service_client(new_socket):

	# receive request from chrome
	# GET / HTTTP/1.1	
	request = new_socket.recv(1024).decode("utf-8")
		

	request_lines = request.splitlines()
	# GET /index.html HTTP/1.1
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	
	file_name = ""

	if (ret):
		file_name = ret.group(1)
		if (file_name == "/"):
			file_name = "/index.html"
		
	try:
		f = open("./html" + file_name, "rb")

	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "-------------flie not found-------------"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
	
		# return http package
		# header
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# send response header
		new_socket.send(response.encode("utf-8"))
		# send response body
		new_socket.send(html_content)
	
	
	new_socket.close()
		

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	tcp_server_socket.bind(("", 8888))
	
	tcp_server_socket.listen(128)
	
	while True:
		new_socket, client_addr = tcp_server_socket.accept()
		
		p = threading.Thread(target = service_client, args = (new_socket,))		
		p.start()
			
	
	tcp_server_socket.close()

if __name__ == "__main__":
	main()


'''
		使用gevent实现http服务器
'''
import re
import socket
import threading
import gevent
from gevent import monkey

monkey.patch_all()

def service_client(new_socket):

	# receive request from chrome
	# GET / HTTTP/1.1	
	request = new_socket.recv(1024).decode("utf-8")
		

	request_lines = request.splitlines()
	# GET /index.html HTTP/1.1
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	
	file_name = ""

	if (ret):
		file_name = ret.group(1)
		if (file_name == "/"):
			file_name = "/index.html"
		
	try:
		f = open("./html" + file_name, "rb")

	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "-------------flie not found-------------"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
	
		# return http package
		# header
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# send response header
		new_socket.send(response.encode("utf-8"))
		# send response body
		new_socket.send(html_content)
	
	
	new_socket.close()
		

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	tcp_server_socket.bind(("", 8888))
	
	tcp_server_socket.listen(128)
	
	while True:
		new_socket, client_addr = tcp_server_socket.accept()
		
		gevent.spawn(service_client, new_socket)
		
	
	tcp_server_socket.close()

if __name__ == "__main__":
	main()


'''		
		使用单进程单线程的程序 实现为多用户服务的http服务器
'''
import socket
import time 

client_socket_list = list()
 
def main():

	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.bind(("", 8888))
	tcp_socket.listen(128)
	tcp_socket.setblocking(False)
	
	while True:
		# time.sleep(0.5)
		try:
			new_socket, socket_addr = tcp_socket.accept()
		except Exception as ret:
			print("---there is not new client---")
		else:	
			print("---if there is not expcetion, which means there is a new client is coming---")
			new_socket.setblocking(False)
			client_socket_list.append(new_socket)
	
		
		for client_socket in client_socket_list:
			try:
				recv_data = client_socket.recv(1024)
			except Exception as ret:
				print("---this client did not send any information---")
			else:
				print("---there is not exception---")
				if recv_data:
					print("---the client send a information---")
				else:
					client_socket.close()
					client_socket_list.remove(client_socket)
					print("---the client is closed---")

if __name__ == "__main__":
	main()


'''	
    响应头的connection：keep-alive长连接类似于公交卡，短链接类似于一次性的单程票
    1- 长连接：再次连接，不需要排队买票，节约时间
    2- 短链接：发起链接，建立连接，发送消息，server回应，链接关闭，实现简单，不需要保存socket，省内存，但是不能快速响应用户请求
    3- 一般客户端连接代理，代理连接数据库，代理不需要断开数据库，客户端不需要重复的断开数据库，客户端直接和代理进行连接/等待链接
    4- 一个百度首页，需要请求多次服务器获取多个资源，长连接不需要频繁建立，效率高
    
    长链接服务器
    
'''



```



#### web静态服务器

```python
'''
		epoll简单模型 单进程单线程  
		1- 有一个特殊内存 是应用程序和kernel共享的
		2- 检测的时候不是轮循 采用事件通知

'''
import re
import socket
import select


def service_client(new_socket, request):
	# request = new_socket.recv(1024).decode("utf-8")

	request_lines = request.splitlines()
	
	file_name = ""
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	if ret:
		file_name = ret.group(1)
		if file_name == "/":
			file_name = "/index.html"

	try:
		f = open("./html" + file_name, "rb" )
	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "------file not found------"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
		response_body = html_content

		response_header = "HTTP/1.1 200 OK\r\n"
		response_header += "Content-Length:%d\r\n" % len(response_body)
		response_header += "\r\n"
			
		response = response_header.encode("utf-8") + response_body

		new_socket.send(response)
	
	# new_socket.close()	


fd_event_dict = dict()

def main():
	
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	tcp_server_socket.bind(("", 8888))
	tcp_server_socket.listen(128)
	tcp_server_socket.setblocking(False)
	

	epl = select.epoll()
	epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
	
	while True:
		
		fd_event_list = epl.poll()
		
		for fd, event in fd_event_list:
			if fd == tcp_server_socket.fileno():
				new_socket, client_addr = tcp_server_socket.accept()
				epl.register(new_socket.fileno(), select.EPOLLIN)
				fd_event_dict[new_socket.fileno()] = new_socket
			elif event == select.EPOLLIN:
				client_socket = fd_event_dict[fd]
				recv_data = client_socket.recv(1024).decode("utf-8")
				if recv_data:
					service_client(client_socket, recv_data)
				else:
					client_socket.close()
					epl.unregister(fd)
					del fd_event_dict[fd]


	tcp_server_socket.close()


main()
```



#### TCP/IP协议

```python
'''
		TCP/IP 协议族
		应用层    		应用1   应用2
		传输层    		TCP 	 	 UDP 
		网络际层  ICMP IP IGMP RARP ARP
		网络接口层 		 网络接口	
'''

'''
		电脑通信 
		使用 网络掩码 来验证ip是否存在于同一个网络号下
		通过 默认网关 代理 
		当一台电脑发送的目标ip地址和本机ip地址所在的网络号不在同一个网络号的时候 会默认的把数据转发给默认网关 默认网关可以代理发送 默认网关一般情况下是路由器
		ip地址在发送过程中不发生变化 mac地址会在发送过程中发生变化 因为mac地址只标记当前的接受方为谁
		
		路由发现协议
		...
		
'''
```



TCP/IP传输协议示意图 ![TCP/IP传输协议示意图](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/OSI%E5%8D%8F%E8%AE%AE%E5%92%8CTCP:IP%E5%8D%8F%E8%AE%AE%E7%9A%84%E5%8C%BA%E5%88%AB.png)

OSI协议和TCP/IP协议的区别 ![OSI协议和TCP/IP协议的区别](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/OSI%E5%8D%8F%E8%AE%AE%E5%92%8CTCP:IP%E5%8D%8F%E8%AE%AE%E7%9A%84%E5%8C%BA%E5%88%AB.png)

简单网络通信 ![简单网络通信](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1.png)

复杂网络通信 ![复杂网络通信](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1.png)



### Python高级

#### GIL

```python
	'''
			linux pwd 查看当前路径
			linux shift + control + t 开双窗口
			linux shift + control + 加号 调大窗口
			linux top or h top 显示当前的操作系统当前运行的情况  
			
			即使有GIL, 多线程的爬取还是比单线程爬取的要快 
			
			计算密集型程序: 没有延时 进程 
			IO密集型程序: 有延时 线程 协程
			
			如何解决GIL
			1- 用其他解释器
			2- 用其他的语言来替代将来线程所做的事情
			
	'''
  
```

GIL简介  ![GIL简介](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/GIL%E7%AE%80%E4%BB%8B.png)



#### 深拷贝与浅拷贝

```python
	'''
			浅拷贝 copy.copy 只拷贝可变对象的最上面一层 对于不可变对象连最上面一层也不拷贝
			深拷贝 copy.deepycopy 拷贝所有的对象 如果拷贝对象都是不可变类型(包含内部元素) 那么此时也只是单纯的指向 但是如果拷贝对象中包含一个可变类型则会递归的拷贝整个对象 
			列表的切片 属于浅拷贝
			
			
			
	'''
```

深浅拷贝  ![深浅拷贝](https://github.com/user1689/91_leetcode_memo/blob/main/computer_basic/img/%E6%B7%B1%E6%B5%85%E6%8B%B7%E8%B4%9D.png)



#### 私有化

```python
'''
		xx 公有变量
		_x 私有化属性或方法 静止导入 类对象和子类可以访问
		__xx 双前置下换线 避免与子类中的属性命名冲突 无法在外部直接访问(名字重整所以访问不到)
		__xx__ 双前后下划线 用户名字空间的魔法对象或属性 例如 __init__ 
		xx_ 单后置下换线 用于避免与python关键词的冲突
		
'''
```



#### 导入模块

```python
'''
		from xxx import yyy
		import xxx
		from xxx import *
		import xxx, zzz
		from xxx import yyy, mmm
		import xxx as zzz
'''
```



#### 路径搜索

```python
'''
		import sys
		sys.path 返回一个list 系统会按list先后顺序 进行搜索是否存在导入的包
		
		导入模块的时候 在使用该模块的代码没有结束的时候 确修改了导入模块的值 此时import为了防止多次导入相同包的情况会避免重新加载模块 若想在程序运行的时候更新导入模块 那么需要调用 from imp import reload, reload(导入模块的名称) 才能使用修改后的模块
		
		多个模块之间有共享的数据放到另外一个模块中 
		如果是 不可变变量 不要使用 from xxx import yyy 此语句会在新建一个本地变量yyy
		如果是 可变变量 如果是append那么可以修改此时不会新建本地变量 如果是=赋值那么也会新建一个本地变量

'''
```



封装 继承 多态

```python
'''
		封装
		比面向过程更加简洁
		__dict__ 对象里有什么属性
		__class__ 表示谁创建了这个类
		
		继承
		对类功能功能进行扩展 提高代码的重复利用率
		
		多态
		
'''
```



#### 多继承中的MRO顺序

```python
'''
		调用父类有两种方法 
		1- 使用父类名称调用 Parent.__init__(self, 参数1， 参数2)
		2- 使用super().__init__(参数1, 参数2)
		
		print(class.__mro__)
		返回一个super方法调用父类的顺序 (, , , , )   基于c3算法
		
		多继承中的super和传统类型java有点不同
    1- Python中的C(A,B)是根据传入的父类顺序来规定的，所以A,B是有顺序的
    2- 具体的顺序是根据python使用C3算法，Grandson.mro() 方法返回的(<class '__main__.GrandSon'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
    3- Grandson()构造时候，super()调用的是mro返回元组的本身位置的下一个，即Grandon的下一个是Son1
    4- 然后去找Son1的构造方法，发现Son1的也调用了super()，所以还去**Grandson的mro**元组中招son1的下一个是son2
    5- son2的构造方法中super，去找son2在元组中的下一个是parent
    可以看出Son1的super方法竟然调用的是**Son2**的，所以很奇怪，一切根据C3算法的mro列表
    super(Parent, self).__init__()，是可以根据具体的类去调用某个父类的super
    super().init没有参数的super默认就是本事的类，类似super(自身的类, self).__init__()
    1- 单继承的情况下，并没有这样的**错误**，所以super()无参，比较方便
    2- 多继承的情况下，还是推荐写有参数的super，来制定具体的父类是谁，该去mro列表中找谁
'''
class Parent(object):

    def __init__(self, name, *args, **kwargs):
        print("Parent的init方法开始调用")
        self.name = name
        print("Parent的init方法结束被调用")


class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):
        print("Son1的init方法开始调用")
        self.age = age
        super().__init__(name, args, kwargs)
        print("Son1的init方法结束被调用")


class Son2(Parent):

    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init方法开始调用")
        self.gender = gender
        super().__init__(name, args, kwargs)
        print("Son2的init方法结束被调用")


class GrandSon(Son1, Son2):

    def __init__(self, name, age, gender):
        print("GrandSon的init方法开始调用")

        super().__init__(name, age, gender)

        print("GrandSon的init方法结束被调用")


def test01():
    print(GrandSon.__mro__)     # --> 返回的是元组
    # print(GrandSon.mro())     # --> 返回的是列表

    gs = GrandSon("grandson", 11, "男")

    print("姓名: ", gs.name)
    print("年龄: ", gs.age)
    print("性别: ", gs.gender)

 
'''  
    继承并不是子类**复制**父类的属性，而是子类中**访问**父类的属性
    实例对象中的x属性现在自身寻找，然后才去父类寻找，父类没有，就去父类的父类寻找
    继承不是复制，而是引用
'''
class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


def test02():
    print(A.x, B.x, C.x)

    # python一看B中并没有自己的x，就自己添加了一个属性x=2
    B.x = 2
    print(A.x, B.x, C.x)

    # 父类中x进行了修改，C并不是复制的1，而是C可以使用A的x
    # C.x 一看自身并没有，就去引用父类
    A.x = 3
    print(A.x, B.x, C.x)        # 返回的是3 2 3 并不是3 2 1
    

```



#### 类方法

```python
'''
		1- 实例方法(self)指向的是调用的实例对象引用，所以需要self，可以读写**实例对象**的属性
    2- 类方法(cls)指向的是类对象引用，可以读写共享的数据**类属性**
    3- 所需要的既不是self实例对象引用也不需要cls类对象引用，就使用静态方法
'''
class D(object):

    def a(self):
        print("实例方法")


    @classmethod
    def b(cls):
        print("类方法")


    @staticmethod
    def c():
        print("静态方法")
 
```



#### 装饰器

```python
# 创建property的第一种方式
class Goods(object):
    def __init__(self):
        self.__price = 0
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, val):
        self.__price = val
    @price.deleter
    def price(self):
				del self.__price
        
apple = Goods()
apple.price = 10 # 设置商品价格
del apple.price

# 创建property的第二种方式
class Foo:
  	def get_bar(slef):
      	return "hi"
      
    BAR = property(get_bar)

obj = Foo()
result = obj.BAR
print(result)


'''
		定义类的时候
		不能直接用私有属性 被类改了名字 用class.__dict__能看到 xxx.__dict__检查属性
		但是可以设置一个__xxx 但是就是普通属性 和__init__方法里的__xxx不同
	
'''
```



#### With 与上下文管理器

```python
'''
		文件读写
		普通版
'''
def m1():
  	f = open("...", "w")
		f.write("")
    f.close()

'''
		进阶版
'''
def m1():
  	f = open("...", "w")
    try:
      f.write("python")
    except IOError:
     	print("oops error")
    except Exception as e:
    
    else:
      
    finally:
      f.close()
      
'''
		高级版
'''
def m3():
  	with open("...", "r") as f:
      f.write("haha")
      
'''
		上下文管理器
		1- 只要在类里面实现了 __enter__ 和 __exit__ 方法
		2- 使用contextmanager的装饰器 通过yield将函数分成两部分 yield之前的语句在__enter__方法中执行 yield之后的语句在__exit__方法中执行 紧跟在yield之后的值是函数的返回值
'''
```



### 问题列表

```python
'''
		Problems
		urllib 和 gevent 无法安装成功 成功
		使用re.split 过滤数组？
'''
```

