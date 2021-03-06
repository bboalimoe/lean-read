精益阅读
========

功能列表
--------

1. 电子书分享与下载
2. 按章节标注阅读信息

开发环境
--------

# 依赖

1. python 2.7
2. mysql
3. git(recommended)
4. pip(recommended)
5. Chrome(recommended)

# 搭建

1. 安装 python 类库

    ```$ sudo pip install -r requirement.txt```
2. 数据库配置

    settings.py 中修改数据库链接信息. 推荐另存为 local_settings.py
3. 创建数据库 schema

    登录数据库执行```create database lean_read;```
3. 更新 submodule, 加载资源文件和数据库数据

    ```$ ./install.sh```

主要页面
--------

1. 电子书列表
    - 电子书列表及其下载链接 -- done
    - 可以上传电子书，并填写书名(链接到新页面进行)
2. 图书阅读信息
    - 展示目录、章节摘要、阅读状态和笔记
    - 章节摘要可以根据阅读状态折叠
    - 目录顺序可选: 顺序/阅读次序
    - 图书阅读进度百分比
    - 可以批量标注章节的阅读信息，添加读书笔记(弹出新页面进行)
