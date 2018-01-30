#python3
import requests
from lxml import etree
import urllib.request as ur
import os,time
from multiprocessing.dummy import Pool as ThreadPool
url = 'https://tieba.baidu.com/p/4840077002?pn={num}'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener = ur.build_opener()
opener.addheaders=[headers]
ur.install_opener(opener)
def main():
    os.chdir(os.getcwd())
    os.mkdir("tieba")
    a = time.time()
    for j in range(1,5):
        r = requests.get(url.format(num=j)).content 
        s = etree.HTML(r)
        img_url = s.xpath('//*[@class="BDE_Image"]/@src')
        try:
            for i in img_url:
                file_name = i.split("/")[-1]
                download_path = "tieba"
                file = os.path.join(download_path, file_name)
                ur.urlretrieve(i, file)
        except Exception as e:
            print('万万没想到:'+str(e))
os.chdir(os.getcwd())
os.mkdir("image")
def get_img(url):    
    r = requests.get(url).content
    s = etree.HTML(r)
    img_url = s.xpath('//*[@class="BDE_Image"]/@src')
    try:
        for i in img_url:
            file_name = i.split("/")[-1]
            download_path = "image"
            file = os.path.join(download_path, file_name)
            ur.urlretrieve(i, file)
    except Exception as e:
        print('万万没想到:'+str(e)) 
if __name__ == "__main__":
    a = time.time()
    main()
    print('这次花费时间为:{num}s'.format(num=time.time()-a))
    c = time.time()
    urls = [url.format(num=i) for i in range(1,5)]
    pool = ThreadPool(12)
    pool.map(get_img,urls)
    print('这次花费时间为:{num}s'.format(num=time.time()-c))
    pool.close()
    pool.join()
