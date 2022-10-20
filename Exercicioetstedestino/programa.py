from classeDestino import Destino
from classeDestinoRepository import DestinoRepository
from Interface import UserInterface


destino = DestinoRepository()
destino.set_adicionarDDD(Destino(88, "Fortaleza"))
destino.set_adicionarDDD(Destino(71, "Salvador"))
destino.set_adicionarDDD(Destino(81, "Recife"))
destino.set_adicionarDDD(Destino(27, "Vitória"))
destino.set_adicionarDDD(Destino(82, "Caruaru"))
destino.set_adicionarDDD(Destino(19, "Campinas"))
destino.set_adicionarDDD(Destino(27, "Vitoria"))
destino.set_adicionarDDD(Destino(48, "Florianópolis"))


print(destino)

user_interface = UserInterface(destino)

while user_interface.get_interacao():
    pass