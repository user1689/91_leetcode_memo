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
		
'''

```

