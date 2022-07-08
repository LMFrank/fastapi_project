## books_crud

本项目基于fastapi库构建异步RESTful风格API，主要实现了简单的crud。通过异步库——databases及SQLAlchemy库完成与mysql的连接。通过pytest进行TDD的实践。

### 依赖

```txt
python==3.8.2
fastapi==0.54.1
uvicorn==0.11.3
SQLAlchemy==1.3.16
databases==0.2.6
PyMySQL==0.9.2
pytest==5.4.1
requests==2.23.0
```



### 项目结构

![tree]( https://github.com/LMFrank/books_crud/blob/master/images/tree.bmp )

### API

![api]( https://github.com/LMFrank/books_crud/blob/master/images/api.bmp )

### 使用方法

创建虚拟环境

```shell
pip install -r requirements.txt
```

在`books_crud/app`下运行：

```
python main.py
```

### Docker部署

```shell
$ docker-compose up -d --build
```

### TODO

1. ~~使用Docker构建整体开发和测试环境，并用Docker启动项目和完成测试~~