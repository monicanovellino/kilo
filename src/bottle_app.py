# =*- coding:utf-8-*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file
from main import Main

@route('/')
def hello_world():
    return 'Tutorial Dois - apredendo git e bottle!'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota!'

@route('/vs')
def versao():
    return 'Tutorial Dois - versão do sistema: {}!'.format(Main().get_versao())

@route('/doc/<filename:.*\.html>')
def documento():
    return static_file(filename, root='home/monicanovellino/desenvolvimento/kilo/docs/build/html', mimetype='text/html')

@route('/doc/<filename:.*\.css>')
def docu():
    return static_file (filename, root='home/monicanovellino/desenvolvimento/kilo/docs/build/html/_static', mimetype='text/css')

application = default_app()

