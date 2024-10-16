import requests
#import urllib

# resource = urllib.urlopen(img)
# out = open("...\img.jpg", 'wb')
# out.write(resource.read())
# out.close()
#
response = requests.get('https://m.stoloto.ru/6x36/archive')
print(response.content)


