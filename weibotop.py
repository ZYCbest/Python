'''用于爬取微博热搜榜'''
# author   : Zyc
# time     : 2019/4/4 17:00
# python version : Python 3.7.0

import requests
from bs4 import BeautifulSoup


def gettop():
	topurl = 'https://s.weibo.com/top/summary?cate=total&key=person'
	resoup = requests.get(topurl)
	soup = BeautifulSoup(resoup.text,'lxml')
	allclasses = soup.find_all(class_='td-02')
	top=[]
	for classes in allclasses:
		top.append(classes.a.string)
	return top

def main():
	tops = gettop()
	print('置顶'+' '+tops[0])
	for seq,top in zip(range(1,51),tops[1:]):
		print(str(seq)+' '+top)

if __name__ == "__main__":
	main()
