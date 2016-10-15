import os
import sys
from wsgiref.simple_server import make_server

def App(environ,start_response):
    status="404 Not Found"
    response_headers = [('Content-type','text/html')]
    notfound = ['File not found.']
    path = '.' + environ['PATH_INFO']
    if path == "/" or path=="/index.html":
        file = open("index.html")
        result = file.read()
        status = "200 OK"
        file.close()

    elif path == "/about/aboutme.html":
        file = open("about/aboutme.html")
        notfound = file.read()
        status = "200 OK"
        file.close()
        
    start_response(status,response_headers)
    return notfound


class Middleware:
    def __init__(self,app):
        self.app = app
    def __call__(self,environ,start_response):
        top_tag = "<body>"
        bottom_tag = "</body>"
        top_string = "\n<div class='top'>Middleware TOP</div>"
        bottom_string = "<div class='bottom'>Middleware BOTTOM</div>\n"

        string=self.app(environ,start_response)
        if string == ['File not found.']:
            return ;
        top_index = string.index(top_tag)
        bottom_index = string.rindex(bottom_tag)

        if bottom_index > -1:
            string = string[:bottom_index-1] + bottom_string + string[bottom_index:]

        if top_index > -1:
            string = string[:top_index+len(top_tag)] + top_string + string[top_index + len(top_tag):]        

        return string

if __name__ == '__main__':
    server=make_server("localhost",8080,Middleware(app))
    print ("Serving localhost on port 8080...")
    server.serve_forever()