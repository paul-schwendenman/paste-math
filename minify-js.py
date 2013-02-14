#!/usr/bin/python2.7

import httplib, urllib, sys

# Define the parameters for the POST request and encode them in
# a URL-safe format.
f = open(sys.argv[1], 'r')

filename = sys.argv[1].split('.')
assert filename[1] == "js"

lines = f.read()

f.close()
filename = filename[0] + '.min.js'

params = urllib.urlencode([
    ('js_code', lines),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
  ])
# 'WHITESPACE_ONLY'


# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()

f = open(filename, 'w')
data = response.read()
f.write(data)
f.close()

conn.close()