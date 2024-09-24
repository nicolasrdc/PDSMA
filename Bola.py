class Bola:
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mudar_bola(self, troca_cor, trocar_circunferencia, trocar_material):
        self.trocar_cor = troca_cor
        self.trocar_circunferencia = trocar_circunferencia
        self.trocar_material = trocar_material


        
    
bola1 = Bola("Vermelha", "20cm", "plástico")
print(bola1.cor , bola1. circunferencia , bola1.material)

bola2 = Bola("Azul", "45cm", "couro")

trocar = (input("Você quer trocar de bola?: "))

if trocar == "sim":
    bola1.mudar_bola(bola2.cor, bola2.circunferencia, bola2.material)
    print("Sua bola agora é da cor", bola2.cor, "tem a circunferênciade ", bola2.circunferencia, "e seu material primário é o ", bola2.material)

elif trocar == "não":
    print("Você continuou com a mesma bola que tem a cor", bola2.cor, "tem a circunferênciade ", bola2.circunferencia, "e seu material primário é o ", bola2.material)

else:
    raise Exception ("Não foi possível trocar de bola, tente novamente!")


