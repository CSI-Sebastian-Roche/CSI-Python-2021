import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67628/pg67628.txt")
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:300])