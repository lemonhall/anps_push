1、启一个新环境
conda create --name apns python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

2、切到新环境下去
conda activate apns

3、安装依赖
https://github.com/Fatal1ty/aioapns

pip install aioapns
pip install asyncio
pip install aiohttp

4、搞docker
docker run -i -t continuumio/anaconda3 /bin/bash
mkdir -p /opt/apns
cd /opt/apns/
git clone https://github.com/lemonhall/anps_push.git
cd anps_push/
pip install -r requirements.txt


# Dockerfile

FROM continuumio/anaconda3
RUN mkdir -p /opt/apns \
    && cd /opt/apns/ \
    && git clone https://github.com/lemonhall/anps_push.git \
    && cd anps_push/ \
    && pip install -r requirements.txt

ENTRYPOINT ["sh /opt/apns/anps_push/start.sh"] 
ENTRYPOINT ['sh','/opt/apns/anps_push/start.sh']

EXPOSE 5050

# 构建
docker build -t apns:v1 .