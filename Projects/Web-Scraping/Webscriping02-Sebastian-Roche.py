import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67628/pg67628.txt")
res.raise_for_status()
playFile = open("Youth and life.txt", "wb")
for chunk in res.iter_content(300000):
    playFile.write(chunk)
playFile.close()