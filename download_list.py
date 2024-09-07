import requests
fname = 'getadmiral-domains.txt'
url = 'https://raw.githubusercontent.com/LanikSJ/ubo-filters/master/filters/' + fname
r = requests.get(url)
open(fname , 'wb').write(r.content)
