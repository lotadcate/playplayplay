import requests
url = 'https://www.sponichi.co.jp/baseball/news/2022/06/01/'
response = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# タイトルと日付とカテゴリ
elems = soup.find_all("p")
elems

# リンクと画像も取れた
# 横のランキングのデータも取得
elems1 = soup.find_all("li")
elems1

elems2 = soup.find_all("nav")
elems2

elems[0]
elems[0].contents[0]

# どうやって欲しいところが取れるかみる
tmp = elems1[0]
tmp

tmp.find('p')

# find('li')は失敗
tmp.find('a')

# contentsをつけると<a href>が消える
tmp.find('a').contents

tmp.contents

tmp.find('a').attrs['href']

# 何も表示されない
tmp.contents[1].find('a')

# これで hrefが取れると思ったけど
tmp.contents[1].contents[0]

tmp.contents[1].find('p')
tmp.contents[1].find('p').contents[0]

tmp.find('p').contents[0]
elems1[0].find('p').contents[0]

elems1[0].contents[1].attrs['href']


# タイトルとurlを取得
# elems1 は liタグを取得したもの
for elem1 in elems1:
    # pタグあるなら（これで記事のところだけ綺麗に取れる）
    if elem1.find('p'):
        print(elem1.find('p').contents[0]) 
        
        #どちらでもいけるが、タグを指定した方が他でも使えそう
        print('https://www.sponichi.co.jp/' + elem1.find('a').attrs['href'])
        #print('https://www.sponichi.co.jp/' + elem1.contents[1].attrs['href'])
        

'''
urlの取得は .attrs['href']

中身→タグの順番で見つけるか
タグ→中身の順番で見つけるか

'''