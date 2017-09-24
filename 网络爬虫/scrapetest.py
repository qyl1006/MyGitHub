from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
#bsObj = BeautifulSoup(html)
#nameList = bsObj.findAll("span", {"class":"green"})
#for name in nameList:
	#print(name.get_text())

#nameList2 = bsObj.findAll(text="the prince")
#print(len(nameList2))

#nameList3 = bsObj.findAll(class_='green')
##for a in nameList3:
	##print(a.get_text())
#print(nameList3[0])

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
#for child in bsObj.find("table",{'id':'giftList'}).children:
	#print(child)

print(bsObj.find('img',{'src':'../img/gifts/img2.jpg'}).parent.previous_sibling.get_text())
