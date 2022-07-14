FROM continuumio/anaconda3
RUN mkdir -p /opt/apns \
    && cd /opt/apns/ \
    && git clone https://github.com/lemonhall/anps_push.git \
    && cd anps_push/ \
    && pip install -r requirements.txt
