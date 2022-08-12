import requests
import argparse
import os
import os.path
from requests_toolbelt.multipart.encoder import MultipartEncoder 
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-text_path",default='../input_data/2.txt')
	parser.add_argument("-image_path",default=str( '../input_image/1.jpeg'))
	parser.add_argument("-if_image",default=1,type=int)
	args = parser.parse_args()
	with open(r'../crawler/cookie_2.txt','r',encoding= 'utf-8') as f_1:
		cookie = f_1.read()
	headers = {
		 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
		 'cookie':cookie,
		 'referer':'https://m.weibo.cn',
	}
	session = requests.Session()
	session.headers.update(headers)
	st = session.get('https://m.weibo.cn/api/config').json()['data']['st']
	with open(args.text_path,'r',encoding='utf-8') as f_2:
		text = f_2.read()
	data = {}
	if(args.if_image == -1):
		compose_data = {
				'content': str(text),
				'st': st,
				'_spr': 'screen:1536x864'
		}
		data = compose_data
	elif(args.if_image == 1):
		#image_path = './input_image/'+args.text_path.split("/")[-1].split(".")[0]+'.jpeg'
		#print(image_path)
		#print(os.path.isfile(image_path))
		if(os.path.isfile(args.image_path)):
			with open(args.image_path,'rb') as f_3:
				image_data = f_3.read()
			m = MultipartEncoder(
					fields= {
							'type':(None,'json'),
							'pic':('pic',image_data,'image/jpeg'),
							'st':(None,st),
							'_spr':(None,'screen:1536x864'),
						},
					boundary='----WebKitFormBoundaryQyCyXzYrBB8Y2HA7'
				)
			headers_2 = headers
			headers_2['content-type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryQyCyXzYrBB8Y2HA7'
			#print(requests.post('https://m.weibo.cn/api/statuses/uploadPic',data=m,headers=headers_2).json())
			picid = session.post('https://m.weibo.cn/api/statuses/uploadPic',data=m,headers=headers_2).json()['pic_id']
			compose_data = {
					'content': str(text),
					'picId':str(picid),
					'st': st,
					'_spr': 'screen:1536x864'
			}
			data = compose_data
		else:
			compose_data = {
				'content': str(text),
				'st': st,
				'_spr': 'screen:1536x864'
			}
			data = compose_data
	headers_3 = headers
	headers_3['content-type'] = 'application/x-www-form-urlencoded'
	update_url = 'https://m.weibo.cn/api/statuses/update'
	response = session.post(url=update_url,data=data,headers=headers_3).json()
	print(response)

