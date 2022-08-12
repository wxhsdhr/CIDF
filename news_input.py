import requests
from lxml import etree

#用于爬取中国日报网的英文新闻
def get_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        }
    url_1 = 'http://www.chinadailyglobal.com/'
    home_text = requests.get(url=url_1,headers=headers).text
    tree = etree.HTML(home_text)
    news_list = tree.xpath('/html/body/div[@class="pc"]/div[@class="cont-two"]/div[@class="b-left"]/div[@class="b-con"]/ul/li//@href')

    num = 1
    file = open("./news_url.txt","w",encoding='utf-8')

    for i in news_list:
        url_2 = 'http://www.chinadailyglobal.com'+i
        k = url_2+'\n'
        file.write(k)
        news_text = requests.get(url=url_2,headers=headers).text
        tree_2 = etree.HTML(news_text)
        real_news_list = tree_2.xpath('/html/body/div[@class="content"]/div[@class="content-left left"]/div[@id="Content"]/p/text()')
    
    
        path = "./input_data/"+str(num)+".txt"
        with open(path,'w',encoding='utf-8') as fp:
            for k in real_news_list:
                fp.write(k)
            print("news'text is ready!")
        try:
            image_src = tree_2.xpath('//*[@id="Content"]/figure/img/@src')
            image_src = 'https:'+image_src[0]
            image = requests.get(url=image_src,headers=headers).content
            p = "./input_image/"+str(num)+".jpeg"
            with open(p,'wb') as f:
                f.write(image)
            num = num+1
            print("news'image is ready!")
        except:
            print("news'image is not ready!")
            num = num+1
            continue
    

    file.close()
    print("news all ready!")
