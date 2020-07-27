
# -*- coding: utf-8 -*-
# bottle_app.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Tutorial Dois - Brincando de git.
.. codeauthor:: Monica Novellino <monicanovellino@gmail.com>
- Como criar repositorio no github
- como clonar usando o comando git
- como comitar usando o comando git
Classes neste módulo:
    :py:class:`Main ` Exemplo de classe qualquer
Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial
"""

from bottle import default_app, route, static_file
from main import Main

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota!'

@route("vs")
def vs_mundo():
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/monicanovellino/dev/kilo/docs/_build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/monicanovellino/dev/kilo/docs/_build/html/', mimetype='text/css')

application = default_app()

