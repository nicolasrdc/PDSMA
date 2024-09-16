class Livro:
    def __init__ (self, titulo, autor, ano, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__preco = preco

# Titulo
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

# Autor 

    def get_autor(self):
        return self.__autor
  
    def set_autor(self, novo_autor):
        self.__autor = novo_autor

# Ano 

    def get_ano(self):
        return self.__ano
     
    def set_ano(self, novo_ano):
        self.__ano = novo_ano

# Preco 

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

# Teste     

l = Livro("Don Quixote","Miguel de Cervantes", 1605, 25.00)

# Getters 

print(l.get_titulo()) # Don Quixote
print(l.get_autor()) # Miguel de Cervantes
print(l.get_ano()) # 1605
print(l.get_preco()) # 25.00

# Setters

l.set_titulo("Harry Potter e a Pedra Filosofal")
l.set_autor("J.K. Rowling")
l.set_ano(1997)
l.set_preco(60.00)

# teste final

print(l.get_titulo()) # Harry Potter e a Pedra Filosofal
print(l.get_autor()) # J.K. Rowling
print(l.get_ano()) # 1997
print(l.get_preco()) # 60+00

