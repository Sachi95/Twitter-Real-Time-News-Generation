import urllib2
proxy_support = urllib2.ProxyHandler({"http":"http://172.31.1.4:8080"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
html = urllib2.urlopen(urllib2.Request("http://www.google.com",headers=hdr)).read()
print html

