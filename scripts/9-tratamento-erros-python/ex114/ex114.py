import urllib 
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("Ops! Deu erro...")
else:
    print("Que legal... consegui enxergar o site!")