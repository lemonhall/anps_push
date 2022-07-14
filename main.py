import asyncio
from aioapns import APNs, NotificationRequest, PushType
from aiohttp import web
import datetime

#生成
#pip install pipreqs
#然后运行 pipreqs
#就生成了requirements.txt

# 1、启一个新环境
# conda create --name apns python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# 2、切到新环境下去
# conda activate apns

# 3、安装依赖
# https://github.com/Fatal1ty/aioapns

# pip install aioapns
# pip install asyncio
# pip install aiohttp
#

# 启动：python3 main.py
# 调用：curl http://localhost:5050/push?content='测试传参'

async def push(push_content):
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
				"alert" : push_content,
				"sound" : "default"
            }
        }
    )
    await apns_key_client.send_notification(request)

#curl http://localhost:5050/push?content='测试传参'
async def hello(request):
	print(request)
	push_content = request.rel_url.query['content']
	print("I am going to sending msg:" + push_content +" at "+ str(datetime.datetime.now()))
	await push(push_content)
	return web.Response(text=push_content)

async def server():
	app = web.Application()
	routes = [web.get('/push',hello)]
	app.add_routes(routes)
	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner,host='0.0.0.0',port=5050)
	print("listen on port 5050 push service waiting for call with /push get")
	await site.start()



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(server())
	#loop.run_until_complete(run())
	loop.run_forever()