#!/usr/bin/python
"""Quick and dirty HTTP echo server for REST requests using Gevent.

Based on http example.


libevent 1.4 only supports GET/POST
libevent 2 supports GET/POST/PUT/DELETE

to use just run:
    python echoHTTPserver.py

it prints to stout_
    METHOD URI POST_DATA

and returns a full RESPONSE.
the method and uri can be found in the header,
the response body is json data containing the POST_DATA
variables that was sent in the request.

Altough made for testing REST clients with simple data
its easy to change for other testing uses.

depends on:
    gevent : pip install gevent # needs libevent-dev to compile dependencies




"""


from gevent import http
import urlparse

def callback(request):
    body = dict(urlparse.parse_qsl(request.input_buffer.read()))
    print '%s %s - %s' % (request.typestr, request.uri, body)
    request.add_output_header('Content-Type', 'text/json')
    request.add_output_header('uri', '%s %s' % (request.typestr,request.uri))
    request.send_reply(200, "OK", '%s' % body)

print 'Serving on 8000...'
http.HTTPServer(('0.0.0.0', 8000), callback).serve_forever()
