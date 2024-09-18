class Carro:
    def __init__ (self, marca, modelo, cor, ano, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__preco = preco

# Marca 

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

# Modelo 

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

# Cor 

    def get_cor(self):
        return self.__cor
    
    def set_cor(self, nova_cor):
        self.__cor = nova_cor

# Ano 

    def get_ano(self):
        return self.__ano
    
    def set_ano(self, novo_ano):
        self.__ano = novo_ano

# Preço 

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

# Teste 

c = Carro('Mitsubishi', 'lancer','Preto', 2014, 40.000)

# Getters 

print(c.get_marca()) # Mitsubishi
print(c.get_modelo()) # Lancer
print(c.get_cor()) # Preto
print(c.get_ano()) # 2014
print(c.get_preco()) # 40.000

# Setters 

c.set_marca('Honda')
c.set_modelo('Civic')
c.set_cor('Cinza')
c.set_ano('2010')
c.set_preco('50.000')

# Teste final

print(c.get_marca()) # Honda
print(c.get_modelo()) # Civic
print(c.get_cor()) # Cinza
print(c.get_ano()) # 2010
print(c.get_preco()) # 50.000
