import time
from fsapi import FSAPI
from radiodeets import URL, PIN, TIMEOUT

# for reference purposes FSAPI: https://github.com/zhelev/python-fsapi

fs = FSAPI(URL, PIN, TIMEOUT)

# print('Power: %s' % fs.power)
# print('Volume: %s' % fs.volume)
# print('Mode: %s' % fs.mode)

fs.volume = 1
fs.mode = 'DAB'
time.sleep(2)
fs.power = False
fs.volume = 12

# print('Power: %s' % fs.power)
# print('Volume: %s' % fs.volume)
# print('Mode: %s' % fs.mode)


"""
>>> from fsapi import FSAPI
>>> URL = 'http://192.168.1.39:80/device'
>>> PIN = 1234
>>> TIMEOUT = 1
>>> fs = FSAPI(URL,PIN,TIMEOUT)
>>> print('Volume: %s' % fs.volume)
"""