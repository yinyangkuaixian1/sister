import requests
import re
import os
import threading

def get_info(page):
    try:
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        response = requests.get('https://www.vmgirls.com/{}.html'.format(page),headers=headers,timeout=1)
        response.raise_for_status()
        # print(response.text)
        html=response.text
    except:
        print('没有',page)
        return
    # 创建文件夹
    dir_name=re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # 解析图片
    img_down=re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
    print('开始下载')

    # 保存图片
    for img_save in img_down:

        # time.sleep(3)
        file_name=img_save.split('/')[-1]
        response = requests.get(img_save,headers=headers,verify=False)
        with open(dir_name+'/'+file_name,'wb')as f:
            f.write(response.content)


url1 = 'https://www.vmgirls.com'
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
h5 = requests.get(url1,headers=headers)
# print(h5.text)

urls2=re.findall('<a class="media-content" href="https://www.vmgirls.com/(.*?).html"',h5.text)

for url in urls2:
    t=threading.Thread(target=get_info,args=(url,))
    t.start()
    get_info(url)


