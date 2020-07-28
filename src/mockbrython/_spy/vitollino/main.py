from unittest.mock import MagicMock, ANY
class BrythonMock(MagicMock):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg) 
        self.__le__ = MagicMock()
        self.vai = MagicMock()
        
class Elemento(BrythonMock):
    pass
        
class Labirinto(BrythonMock):
    pass
        
class Sala(BrythonMock):
    pass
        
class Musica(BrythonMock):
    pass
        
class Inventario(BrythonMock):
    pass
        
class Codigo(BrythonMock):
    pass
        
class Portal(BrythonMock):
    pass
        
class Salao(BrythonMock):
    pass
        
class Popup(BrythonMock):
    pass
        
class Texto(BrythonMock):
    pass
        
class Point(BrythonMock):
    pass
        
class Cursor(BrythonMock):
    pass
        
class Dragger(BrythonMock):
    pass
        
class Dropper(BrythonMock):
    pass
        
class Droppable(BrythonMock):
    pass
        
class Folha(BrythonMock):
    pass
        
class Suporte(BrythonMock):
    pass
        
class Bloco(BrythonMock):
    pass
        
class Jogo(BrythonMock):
    pass
        
class Cena(BrythonMock):
    pass

# Elemento = BrythonMock()
INVENTARIO = BrythonMock()
STYLE = BrythonMock()
JOGO = Jogo()


