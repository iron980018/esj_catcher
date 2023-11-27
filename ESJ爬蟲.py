import os
import requests
import time
from bs4 import BeautifulSoup

#func
def catch_web(url,first_time,floder_name,floder_adress,episode,the_cookie):
    #以下為每次抓不同小說所需調整的
    headers = {
        "cookie":the_cookie
    }
    #以上為每次抓不同小說所需調整的

    target = requests.get(url,headers=headers)
    soup = BeautifulSoup(target.text,"html.parser")
    
    #建立資料夾
    if first_time == 1:
        Title = soup.title.string
        parts = Title.split("第一話", 1)
        part1 = parts[0].strip()
        part1 = part1[:-2]
        floder_name = part1
        if not os.path.isdir("C:\\Users\\iron0\\Downloads\\" + floder_name):
            os.mkdir("C:\\Users\\iron0\\Downloads\\" + floder_name)
        floder_adress = "C:\\Users\\iron0\\Downloads\\" + floder_name
        first_time = 0

    #獲取文章內容
    get_content = soup.select("p")
    content = ""
    for s in get_content:
        content += s.text+"\n"
    #print(content)

    #存檔
    episode_to_string = str(episode)
    path = floder_adress+"\\"+episode_to_string+"."+soup.title.string+".txt"
    f = open(path , "w", encoding='UTF-8')
    f.write(content)
    f.close

    #抓取下一話
    next_url = ""
    for link in soup.select("a.btn-next"):
        next_url = link["href"]

    if next_url == "":
        print("結束抓取 !")
    else:
        print("5秒後抓取下一話!")
        time.sleep(5)
        catch_web(next_url,first_time,floder_name,floder_adress,episode + 1)



print("ESJ爬蟲 by i9")
print("此程式為教育使用，個人實作皆屬個人行為，本作者不負任何法律責任")
cookie = input("請輸入你的cookie(請登入後再輸入):")
start_url = input("請輸入起始網址(第1話):")

first_time = 1
floder_name = ""
floder_adress = ""

catch_web(start_url,first_time,floder_name,floder_adress,1,cookie)

