import train
import news_input
import weibo_2

import run_stega_optimized
import sys
import random
import time

if __name__ == '__main__':
    print("请关注新浪微博，微博昵称：端庄的厄耳")

    for k in open('./read.txt','r',encoding='utf-8').readlines():
        print('@'*5,end = '')
        print(k.split('\n')[0],end = '')
        print('@'*5)
    i = input("继续运行请输入1，否则请输入0")
    
    if (i == '0'):
        sys.exit()
        
    elif (i=='1'):
        #模块初始化
        w = weibo_2.Weibo()
        care_id = w.Care_people_id()
        print(care_id)
	    #点赞所有关注的人中随机三个人的第一条微博
        l = len(care_id)
        r = random.randint(0,l-4)
        time.sleep(2)
        for i in care_id[r:r+3]:
            k = w.People_n_passage_ids(i,1)
            print(k)
            time.sleep(2)
            w.vote(k[0][0])
        #发送微博
        time.sleep(2)
        text = w.weather()
        w.send(text)
	    #随机转发评论一位关注的博主的文章
        time.sleep(2)
        r_1 = random.randint(0,l-1)
        hh = w.People_n_passage_ids(care_id[r_1],1)
        w.repost('信安大赛',hh[0][0])

        news_input.get_news()
        path = ['./input_data/1.txt','./input_data/2.txt','./input_data/3.txt','./input_data/4.txt','./input_data/5.txt']

        for p in path:
            with open(p,'r',encoding='utf-8') as fp:
                if (fp.read()==''):
                    print('内容为空')
                    continue
            train.train(p)

        for k in range(1,6):
            with open('./results/cnndm/'+str(k)+'.txt','r',encoding='utf-8') as fp:
                if (fp.read()==''):
                    print('内容为空')
                    continue
            w.weibo_send(text_path='./results/cnndm/'+str(k)+'.txt',image_path='./input_image/'+str(k)+'.jpeg',if_image=1)

        run_stega_optimized.run()
        w.weibo_send(text_path='./c_text/1.txt',image_path='./images/1.jpeg',if_image=1)

