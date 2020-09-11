import requests
import bs4

result = requests.get("http://www.example.com")
print(type(result))
print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup)

soup.select('title')
print(soup.select('title'))
print(soup.select('p'))

print(soup.select('title')[0].getText())
site_paragraphs = soup.select("p")
print(type(site_paragraphs[0]))
print(site_paragraphs[0].getText())


#grabbing all elements of a class
# First get the request
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

# Create a soup from request
soup = bs4.BeautifulSoup(res.text,"lxml")


# note depending on your IP Address, 
# this class may be called something different
print(soup.select(".toctext"))

for item in soup.select(".toctext"):
    print(item.text)



#Getting an Image from a Website

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')
image_info = soup.select('.thumbimage')
print(image_info)
print(
len(image_info))
computer = image_info[0]
print(type(computer))
print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
image_link.content


f = open('my_new_file_name.jpg','wb')
print(f.write(image_link.content))
f.close()


#Working with Multiple Pages and Items

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup.select(".product_pod"))
products = soup.select(".product_pod")
example = products[0]
print(type(example))
print(example.attrs)
print(list(example.children))
print(example.select('.star-rating.Three'))
print(example.select('.star-rating.Two'))
print(example.select('a'))
print(example.select('a')[1])
print(example.select('a')[1]['title'])


two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)






