from curses.ascii import US
from classeDestinoRepository import DestinoRepository
from classeUsuario import Usuario


class UserInterface:
    def __init__(self, destino: DestinoRepository) -> None:
        self.destino = destino

    def solicitar_input(self) -> Usuario:
        result = input(
            "Digite o DDD: ").split()
        return Usuario(int(result[0]))
    
    
    def exibir_destino(self, destino: Usuario) -> int:
        return self.destino.localizar_destino(destino)


    def get_interacao(self) -> bool:
        Usuario = self.solicitar_input()
        if(self.destino.verificar_destino(Usuario) == False):
            print("DDD não encontrado no cadastro!")
            return False

        print(f"Cidade do DDD: {self.destino.obter_destino(Usuario)}")

        return True