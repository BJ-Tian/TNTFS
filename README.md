# TNTFS

MacOS M1 开源NTFS

Python3.10 使用 py2app 打包编译

理论上 MacOS 全系列通用

#### Python3.10 环境

```shell
brew install python@3.10
brew install tcl-tk
brew install python-tk@3.10
```

#### sudo 免密

```
sudo visudo
#将 %admin          ALL = (ALL) ALL 换成下面这个
%admin          ALL = (ALL) NOPASSWD: ALL
```

#### 安装 macfuse

关闭SIP保护特性

系统中启用 macfuse

```shell
brew install ntfs-3g-mac
brew install macfuse
```

#### 运行

把软件放到应用程序里然后双击运行

#### 开机自启

<img width="343" alt="WechatIMG987" src="https://user-images.githubusercontent.com/130722656/231932672-c3c13010-8bff-46c8-917e-c61af317d709.png">

#### PS

TNTFS.zip 是打包好的程序，可直接运行。
