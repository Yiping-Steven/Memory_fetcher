#!/usr/bin/python3
# -*-coding: UTF-8 -*-
import requests
import bs4
import re
import os
try:
	path=input("Enter directory:")
except ValueError:
	path="./"
web="http://www.cs.jhu.edu/~phi/ai/"
nameLenLimit=100
count=0
cnt=0

session=requests.session()
r=session.get(web)
soup=bs4.BeautifulSoup(r.content,"html.parser")
p1=re.compile('/[\w\-\.]*\.pdf')#find the pdf files
p2=re.compile('week\d*')#not necessary
p3=re.compile('lecture\d*')#not necessary

for link in soup.find_all('a'):
	if link.get('href') is not None:
		result=p1.search(link.get('href'))
		if result is not None: #found target pdf file
			tmp=result.group()
			name=tmp[1:]
			if (p2.match(name) is not None):
				name = name[:p2.match(name).end()]+'_'+link.string+name[p2.match(name).end():]
				print(name)
			elif (p3.match(name) is not None):
				name = name[:p3.match(name).end()]+'_'+link.string+name[p3.match(name).end():]
				print(name)
			else:
				name=link.string+'.pdf'
				print(name)

			if len(name)>nameLenLimit:
				print(count, name)
				name = str(count)+'.pdf'
				count=count+1
			url=web+link.get('href')
			print(url)
			r = requests.get(url, stream=True)
			if not os.path.exists(path):
				os.makedirs(path)
			with open(path+'/'+name,'wb') as handle:
				if not r.ok:
					pass
					# raise ValueError('failed in saving:', name, '---', url)
				cnt=cnt+1
				print('start downloading No.', cnt)
				for block in r.iter_content(1024):
					handle.write(block)
			




