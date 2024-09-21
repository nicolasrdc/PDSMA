class Controle:
    def __init__ (self, cor, altura, pronfundidade, largura):     
        self.cor = cor
        self.altura = altura 
        self.profundidade = pronfundidade
        self.largura = largura


    def passar_de_canal(self, botao):
        if botao == "+":
            print('Aumentar o Canal')

        elif botao == '-':
            print('Diminuir o Canal')


controle_remoto = Controle(self.cor, "10cm,", "2cm","2cm")
print(controle_remoto.cor)
controle_remoto.passar_de_canal("+")


controle_remoto2 = Controle("Cinza","10cm","3cm","2cm")
print(controle_remoto2.cor)
controle_remoto2.passar_de_canal("-")

