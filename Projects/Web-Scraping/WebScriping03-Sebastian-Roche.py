import os
from pathlib import Path
import bs4

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "example.html")

examplefile = open(myOutputFilePath)
exampleSoup = bs4.BeautifulSoup(examplefile.read(), "html.parser")
elems = exampleSoup.select("#author")
type(elems)
print(len(elems))
type(elems[0])
str(elems[0])
print(elems[0].getText())
