# -*- coding: utf-8 -*-
# kilo.main.py
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

class Main:
    """ classe exemplo.
        : param:versão deste exemplo

    """

    def __init__(self, versao="20.07"):
        self.versao = versao
        #print ("classe exemplo, versao {}".format (versao))

    def get_versao(self):
        """retorna a versao do sistema.
           :return: a versao do sistema
        """
        return self.versao
if __name__ == "__main__":
    print (Main().get_versao())