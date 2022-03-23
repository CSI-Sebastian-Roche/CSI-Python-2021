import bs4
examplefile = open("example.html")
exampleSoup = bs4.BeautifulSoup(examplefile.read(), "html.parser")
elems = exampleSoup.select("#author")
type(elems)
print(len(elems))
type(elems[0])
str(elems[0])
print(elems[0].getText())
