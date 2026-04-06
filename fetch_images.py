import urllib.request
import re
import json

urls = [
'https://pin.it/3JuzBoecG'
]
images = []
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req)
        html = resp.read().decode('utf-8', errors='ignore')
        # Try to find high-res images
        links = re.findall(r'https://i\.pinimg\.com/originals/[^\s\"\']+\.jpg', html)
        if not links:
            links = re.findall(r'https://i\.pinimg\.com/736x/[^\s\"\']+\.jpg', html)
        
        if links:
            # take the first unique one
            images.append(list(set(links))[0])
        else:
            images.append('NOT FOUND in ' + u)
    except Exception as e:
        images.append('ERROR ' + str(e))

print(json.dumps(images, indent=2))
