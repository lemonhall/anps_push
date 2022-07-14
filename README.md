# README
依赖了这个库 https://github.com/Fatal1ty/aioapns

这个项目其实很简单，就是用一个http的server把apns的调用封装起来，并且docker化

然后EXPOSE 5050端口给集群，方便使用，就这么简单


## 启一个新环境
conda create --name apns python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

## 切到新环境下去
conda activate apns

## 安装依赖
https://github.com/Fatal1ty/aioapns

pip install aioapns
pip install asyncio
pip install aiohttp

## 搞docker
docker run -i -t continuumio/anaconda3 /bin/bash
mkdir -p /opt/apns
cd /opt/apns/
git clone https://github.com/lemonhall/anps_push.git
cd anps_push/
pip install -r requirements.txt


## Dockerfile

FROM continuumio/anaconda3
RUN mkdir -p /opt/apns \
    && cd /opt/apns/ \
    && git clone https://github.com/lemonhall/anps_push.git \
    && cd anps_push/ \
    && pip install -r requirements.txt

ENTRYPOINT ["sh /opt/apns/anps_push/start.sh"] 
ENTRYPOINT ['sh','/opt/apns/anps_push/start.sh']

EXPOSE 5050

## 构建
docker build -t lemonhall/apns:v1 .

## push的小技巧

首先需要在自己的空间下build
docker build -t lemonhall/apns:v1 .
docker login
docker push lemonhall/apns:v1

这样就能成功的push了

