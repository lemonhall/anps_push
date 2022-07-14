1、启一个新环境
conda create --name apns python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

2、切到新环境下去
conda activate apns

3、安装依赖
https://github.com/Fatal1ty/aioapns

pip install aioapns
pip install asyncio

4、编码
import asyncio
from aioapns import APNs, NotificationRequest, PushType

async def run():
    apns_key_client = APNs(
        key='./push.p8',
        key_id='A533U9KJ66',
        team_id='84Z2AMFMF3',
        topic='com.mr-noone.apns-tool',  # Bundle ID
        use_sandbox=False,
    )
    request = NotificationRequest(
        device_token='CBDEC837C450FAD4F9578E8482158DBE207BDC5F18EEC9A3EB3E4171F2B56B6B',
        message = {
            "aps": {
				"alert" : "温度超过60度",
				"sound" : "default"
            }
        }
    )
    await apns_key_client.send_notification(request)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
