import json
import operator
from concurrent.futures import ThreadPoolExecutor,as_completed
from requests_toolbelt.multipart.encoder import MultipartEncoder 
import random

import time
import requests
import argparse
import os
import os.path
 

class Weibo:
	#初始化
	def __init__(self):
		with open(r'./crawler/cookie_2.txt','r',encoding= 'utf-8') as fp:
			cookie = fp.read()
		self.headers = {
		 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
		 'cookie':cookie,
		 'referer':'https://m.weibo.cn',
		 }
		self.session = requests.Session()
		self.session.headers.update(self.headers)
		self.response = self.session.get('https://m.weibo.cn/api/config').json()
		print(self.response)
		self.st = self.response['data']['st']
		self.uid = self.response['data']['uid']
	
	#获得微博里所有关注的人的id
	def Care_people_id(self):
		
		page = 1
		#关注的人的id的列表
		care_id = []
		for i in range(1,page+1):
			params = { 
				'containerid': '231093_-_selffollowed',
				'page':i
			}
			weibo_list_data = self.session.get('https://m.weibo.cn/api/container/getIndex', params=params).json()

			if i==1:
				weibo_list = weibo_list_data['data']['cards'][2]['card_group']
			elif i>1:
				try:
					weibo_list = weibo_list_data['data']['cards'][1]['card_group']
				except:
					continue
			
			for user in weibo_list:
				#k = []
				#k.append(str(user['user']['id']))
				care_id.insert(0,str(user['user']['id']))
				#care_id[user['user']['screen_name']] = user['user']['id']
		#print(care_id)
		return care_id

	#在知晓用户id下获得其最近n条微博的所有id  n=1
	def People_n_passage_ids(self,people_id,n):
		people_id = str(people_id)
		bowen_id_list = []
		params = {
			'uid':people_id,
			'luicode':'10000011',
			'lfid':'231093_-_selffollowed',
			'containerid':'107603'+people_id,
		}

		response_json_data = self.session.get( 'https://m.weibo.cn/api/container/getIndex',params=params).json()['data']['cards']
		count = 1
		for i in response_json_data:
			if 'mblog' in i and count <=n:
				bowen_id_list.append(i['mblog']['id'])
				count = count+1

		return bowen_id_list,int(people_id)
	
	#获取所有id
	def know_all_ids(self,n):
		id = self.Care_people_id()
		id_2 = id
		with ThreadPoolExecutor(2) as t:
			all_task = [t.submit(self.People_n_passage_ids,k[0],1) for k in id]
			for future in as_completed(all_task):
				h = future.result()
				for i in id_2:
					if i[0]==h[1]:
						print(h[1][0])
						
						#h[0].insert(0,str(id_dic[k]))
						#id_dic[k] = h[0]
					else:
						continue
				#print(h)
		return id_2

	#点赞
	def vote(self,people_passage_id):
		data = {
			'id':people_passage_id,
			'attitude':'heart',
			'st':self.st,
			}
		response = self.session.post('https://m.weibo.cn/api/attitudes/create',data).json()
		if response['ok']==1:
			print('微博点赞成功')
		else:
			print('微博点赞失败')
	
	#取消点赞
	def disvote(self,people_passage_id):
		data = {
			'id':people_passage_id,
			'attitude':'heart',
			'st':self.st,
			}
		response = self.session.post('https://m.weibo.cn/api/attitudes/destroy',data).json()
		if response['ok']==1:
			print('微博取消点赞成功')
		else:
			print('微博取消点赞失败')
	
	#自动发送微博
	def send(self,text):
		i = str(3)
		#i = input("请选择你所要发送的微博接受范围：1：私密，2：好友圈，3：公开\n")
		if i=='1':
			j='1'
		elif i=='2':
			j='6'
		elif i=='3':
			j='0'
		compose_data = {
			'content': text,#input("请输入发送的内容：")
			#'picId':str(picid),
			'visible':j,
			'st': self.st,
			'_spr': 'screen:1536x864'
		}
		#headers_3 = self.headers
		#headers_3['content-type'] = 'application/x-www-form-urlencoded'
		update_url = 'https://m.weibo.cn/api/statuses/update'
		response = requests.post(url=update_url,data=compose_data,headers=self.headers).json()
		#print(response)
		if response['ok']==1:
			print('微博发送成功')
		else:
			print('微博发送失败')
	
	#自动转发微博
	def repost(self,text,people_passage_id):
		i = str(3)
		#i = input("请选择你所要转发的微博接受范围：1：私密    2：好友圈    3：公开\n")
		if i=='1':
			j='1'
		elif i=='2':
			j='6'
		elif i=='3':
			j='0'
		m = str(1)
		#m = input("请选择你所要转发的微博是否同时评论：1：否    2：是\n")
		m = str(int(m)-1)
		
		repost_data = {
			'id':people_passage_id,
			'content':text,
			'dualPost': m,
			'visible':j,
			'mid':people_passage_id,
			'st':self.st
		}
		update_url = 'https://m.weibo.cn/api/statuses/repost'
		response = self.session.post(url=update_url,data=repost_data).json()
		if response['ok']==1:
			print('微博转发成功')
		else:
			print('微博转发失败')
	
	#获取西安的天气
	def weather(self):
		headers_1 = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
		}
		url_1 = 'https://weather.cma.cn/api/now/57036'

		json_data = requests.get(url=url_1,headers=headers_1).json()

		weather_data = '天气预报更新时间：'+json_data['data']['lastUpdate']+'\n\n'
		weather_data = weather_data+'位置：    '+json_data['data']['location']['path']+'\n'
		weather_data = weather_data+'温度：    '+str(json_data['data']['now']['temperature'])+'℃'+'\n'
		weather_data = weather_data+'压力：    '+str(json_data['data']['now']['pressure'])+'hPa'+'\n'
		weather_data = weather_data+'湿度：    '+str(json_data['data']['now']['humidity'])+'%'+'\n'
		weather_data = weather_data+'风向：    '+json_data['data']['now']['windDirection']+'   '+json_data['data']['now']['windScale']
	
		return weather_data

	def weibo_send(self,text_path,image_path,if_image):
		parser = argparse.ArgumentParser()
		parser.add_argument("-text_path",default=str(text_path))
		parser.add_argument("-image_path",default=str(image_path))
		parser.add_argument("-if_image",default=int(if_image),type=int)
		args = parser.parse_args()
	
		with open(args.text_path,'r',encoding='utf-8') as f_2:
			text = f_2.read()
		data = {}
		if(args.if_image == -1):
			compose_data = {
					'content': str(text),
					'st': self.st,
					'_spr': 'screen:1536x864'
			}
			data = compose_data
		elif(args.if_image == 1):
			#image_path = './input_image/'+args.text_path.split("/")[-1].split(".")[0]+'.jpeg'
			#print(image_path)
			#print(os.path.isfile(image_path))
			try:
				with open (image_path,'rb') as fp:
					fp.read()
				print('新闻有图片')
				with open(args.image_path,'rb') as f_3:
					image_data = f_3.read()
				m = MultipartEncoder(
						fields= {
								'type':(None,'json'),
								'pic':('pic',image_data,'image/jpeg'),
								'st':(None,self.st),
								'_spr':(None,'screen:1536x864'),
							},
						boundary='----WebKitFormBoundaryQyCyXzYrBB8Y2HA7'
					)
				headers_2 = self.headers
				headers_2['content-type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryQyCyXzYrBB8Y2HA7'
				#print(requests.post('https://m.weibo.cn/api/statuses/uploadPic',data=m,headers=headers_2).json())
				picid = self.session.post('https://m.weibo.cn/api/statuses/uploadPic',data=m,headers=headers_2).json()['pic_id']
				#print(picid)
				compose_data = {
						'content': str(text),
						'picId':str(picid),
						'st': self.st,
						'_spr': 'screen:1536x864'
				}
				data = compose_data
			except:
				print('新闻没图片')
				compose_data = {
					'content': str(text),
					'st': self.st,
					'_spr': 'screen:1536x864'
				}
				data = compose_data
		headers_3 = self.headers
		headers_3['content-type'] = 'application/x-www-form-urlencoded'
		update_url = 'https://m.weibo.cn/api/statuses/update'
		response = self.session.post(url=update_url,data=data,headers=headers_3).json()
		print(response)









