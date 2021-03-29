from bs4 import BeautifulSoup
import urllib.request
file = open("big_data.txt", "w")
#small data link
#link = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%AF&filefrom=%D0%AF&pagefrom=%D0%AF#mw-pages"
#big data link
link = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
go = True
#i = 0
while go == True: #and i < 2:
    req = urllib.request.Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")
    a_names = soup.find_all('div', attrs={"class":"mw-category-group"})
    print(len(a_names))
    for b_names in a_names:
        c_names = b_names.find("ul")
        d_names = c_names.find_all("li")
        for e_names in d_names:
            name = e_names.find("a")['title']
            file.write(name)
            file.write(", ")
            print(name)
            if name == "Ящурки":
                go = False
                break
        linkteg = soup.find("a", string="Следующая страница")
        bad_link = linkteg.attrs["href"]
        link = "https://ru.wikipedia.org" + bad_link
        #i += 1
file.close()
    
    
    



