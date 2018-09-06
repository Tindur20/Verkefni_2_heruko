from sys import argv

import bottle
from bottle import *

#bottle.debug(True)

@route('/')
def index():
       return """ 
        <a href="/a">Liður A</a>
        <a href="/b">Liður B</a>       
       """

@route('/a')
def about():
        return """ 
        <h2>Verkefni 2.A</h2>
        <a href="/">heim</a><br>
        <a href="/sida/1">Sida 1</a><br>
        <a href="/sida/2">Sida 2</a><br>
        <a href="/sida/3">Sida 3</a><br>
       """

@route('/sida/<id>')
def page(id):
        if id == '1':
            return "Þetta er síða eitt<br><a href='/a'>til baka</a>"
        elif id == '2':
            return "Þetta er síða tvö<br><a href='/a'>til baka</a>"
        elif id == '3':
            return "Þetta er síða þrjú<br><a href='/a'>til baka</a>"
        else:
            abort(404,"Þessi síða virkar ekki")


@route('/b')
def about():
        return """ 
           <a href="/">heim</a><br>
           <a href="/sida2?mynd=monkas"><img src='mynd/monkas.png'></a>
           <a href="/sida2?mynd=pepehands"><img src='mynd/pepehands.png'></a>
           <a href="/sida2?mynd=omegalul"><img src='mynd/omegalul.png'></a>
           <a href="/sida2?mynd=forsen"><img src='mynd/frosen.png'></a>
           
       """

@route('/sida2')
def query():
    l = request.query.mynd
    if l == 'monkas':
        return "<a href='/b'>liður b</a><br> <img src='mynd/monkas.png'>"
    l = request.query.mynd
    if l == 'pepehands':
        return "<a href='/b'>liður b</a><br> <img src='mynd/pepehands.png'>"
    l = request.query.mynd
    if l == 'omegalul':
        return "<a href='/b'>liður b</a><br> <img src='mynd/omegalul.png'>"

    l = request.query.mynd
    if l == 'forsen':
        return "<a href='/b'>liður b</a><br> <img src='mynd/frosen.png'>"



@route('/mynd/<filename>')
def server_static(filename):
    return static_file(filename, root='./myndir')

@error(404)
def error404(error):
    return "<h1 style='color:red'>Þessi síða virkar ekki eða er ekki til.</h1><br><h1>Error 404</h1>"


@error(405)
def error405(error):
    return "<h1 style='color:red'>Þessi síða virkar ekki eða er ekki til.</h1><br><h1>Error 405</h1>"



#run(host='localhost', port=8800, debug = True, reloader=True)

bottle.run(host='0.0.0.0', port=argv[1])
