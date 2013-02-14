#!/usr/bin/python2.7

import httplib, urllib, sys

# Define the parameters for the POST request and encode them in
# a URL-safe format.

def read(filename):
    with open(sys.argv[1], 'r') as f:
        output = f.read()
    return output

def write(filename, input):
    with open(filename, 'w') as f:
        f.write(input)


def sendrecieve(input):
    params = urllib.urlencode([
        ('js_code', input),
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
    data = response.read()
    conn.close()
    return data


if __name__ == '__main__':
    filename = sys.argv[1].split('.')
    if filename[-1] == 'js' and len(filename) == 2:
        try:
            try:
                content = read(sys.argv[1])
            except:
                print "read error"
                raise Exception()
            try:
                data = sendrecieve(content)
            except Exception as e:
                print "connection error"
                raise Exception()
            try:    
                write(filename[0] + '.min.js', data)
            except Exception as e:
                print "write error"
                print e
                raise Exception()
        except:
            pass
        else:
            print "done"
        finally:
            pass
    else:
        print "skipped"



