class Admin():
    def __init__(self):
        # Variaveis privadas para não ter acesso // Mas tem que criar uma base de dados para poder modificar e manter mesmo
        # depois de reiniciar o programa
        self.__user = 'admin'
        self.__pw = 'admin'

    # Unica coisa que deve ter acesso é a checar a senha e user
    def check_password(self,Password):
        if(self.__pw == Password):
            return 1
        else:
            return 0

    def check_username(self,username):
        if(self.__user == username):
            return 1
        else:
            return 0
        
