#!coding: utf-8
from flask import *
from json import *
import requests
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

bot_server = Flask(__name__)

@bot_server.route('/api/message',methods=['POST'])
## coolq-http-api设定的路径
def server():
    api_url2 = 'http://IP：端口/send_msg'
    data_1 = request.get_data().decode('utf-8')
    print data_1
    data_2 = json.loads(data_1)
    #print(data)
    message = data_2['raw_message']
    print message
    qq_id = data_2['user_id']
    print qq_id
    manager_id = "管理员QQ"
    if message == 'ok':
       asd_dist = []
       with open("./dx.json",'r') as p:
         dict = json.load(p)
         for load_dict in dict:
            if load_dict['user_id'] == qq_id:
               load_dict['status_id'] = '1'
            asd_dist.append(load_dict)
       with open('./dx.json','w') as g:
          json.dump(asd_dist,g)
    if message == 'list' and str(qq_id) == str(manager_id):
       with open("./dx.json",'r') as k:
         awd = json.load(k)
       for asd_list in awd:
         if asd_list['status_id'] == '0':
           msg1 = {
                   "message_type":'private',
                   "user_id":manager_id,
                   "message":"QQ: " + str(asd_list['user_id']) + "     昵称：" + str(asd_list['user_name']).decode('utf-8'),
                   "auto_escape":False
                  }
           xbg = requests.post(api_url2,data=msg1)
           print(xbg)
    if message == 'ccc' and str(qq_id) == str(manager_id):
       with open("./dx.json",'r') as k:
         awd = json.load(k)
       for asd_list in awd:
         if asd_list['status_id'] == '0':
           msg2 = {
                   "message_type":'private',
                   "user_id":asd_list['user_id'],
                   "message":"请大佬尽快将截图发给我这个机器人，并且给他回复一个ok（大小写注意）,如果已经发过截图还受骚扰的，请再次给本机器人发一次截图，并且回复一个ok，最后请暴打本机器人制作者————limu。",
                   "auto_escape":False
                  }
           aaa = requests.post(api_url2,data=msg2)
           print(aaa)
    if message == 'build' and str(qq_id) == str(manager_id):
          os.system('python2 ./build.py')
          msg3 = {
                 "message_type":'private',
                 "user_id":manager_id,
                 "message":"重置成功！\n 机器人制作者————limu。",
                 "auto_escape":False
                  }
          bbb = requests.post(api_url2,data=msg3)
    return ''



if __name__ == '__main__':
  bot_server.run(host='0.0.0.0' , port=40002)
##coolq-http-api设定的端口

