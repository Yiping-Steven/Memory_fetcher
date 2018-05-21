# Memory_fetcher
一键保存清华邮箱和网络学堂数据到本地存储.

---
## 用法
### 1. 安装
**基本环境要求：** 电脑上有python3环境就可以（python3和pip3工具的安装从略）。理论上python2也可以，不过我还没测试过。

此外还用到了另外三样：
#### 1.1 BeautifulSoup4
`pip3 install BeautifulSoup4`
#### 1.2 requests 
`pip3 install requests
`
#### 1.3 本项目
下载源码到某一本地文件夹并解压.

### 2.使用
`crawler_learn.py`脚本用于下载网络学堂数据，会在当前目录下创建一个‘learn’文件夹并分课程存放。
`crawler_mail.py`脚本用于下载清华邮箱数据，会在当前目录下创建一个‘mail’文件夹进行存放。

在本项目源码路径（建议选一个存储空间足够大的硬盘）下打开命令行（终端），运行：
`python3 crawler_learn.py`
或
`python3 crawler_mail.py`

根据提示输入用户名和密码后即开始下载。

---
## 注：
- 运行crawler_learn.py时，终端内会有大量debug信息，请不要慌张，这是程序在自动检测网络学堂上的数据编码。
- 清华邮箱下载下来的数据可能存在乱码，此bug已知，希望之后还有时间改进。
- 特别鸣谢kehao95提供的[API](https://github.com/kehao95/thu_learn)
- **祝毕业快乐！**