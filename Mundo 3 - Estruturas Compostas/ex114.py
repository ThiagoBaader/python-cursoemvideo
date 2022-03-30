"""
Site está acessível?
"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urlib.error.URLError:
    print('O site Pudim não está acessível!')
else:
    print('Consegui acessar o site Pudim sucesso!')
