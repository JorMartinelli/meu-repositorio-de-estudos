from __future__ import annotations
from abc import ABC, abstractmethod

class Produto(ABC):
    """
    Classe abstrata de produtos. Todo produto deve ter um nome e um preço em reais.
    """

    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self): 
        return self._nome
    
    @property
    def preco(self): 
        return self._preco
    
class ProdutoDigital(Produto):
    """
    Classe de produtos digitais. Todo produto digital necessita de um e-mail.
    """

    def __init__(self, nome:str, preco:float, email:str):
        super().__init__(nome, preco)
        self._email = email
    
    @property
    def email(self): 
        return self._email
    
class ProdutoFisico(Produto):
    """
    Classe de produtos físicos. Todo produto físico tem um peso em quilogramas.
    """

    def __init__(self, nome:str, preco:float, peso:float):
        super().__init__(nome, preco)
        self._peso = peso
    
    @property
    def peso(self): 
        return self._peso
    
class Notificador(ABC):
    """
    Classe de notificações.
    """

    @abstractmethod
    def notificar(self, pedido): pass

class Email(Notificador):
    """
    Classe de notificações por e-mail.
    """

    def notificar(self, pedido:Pedido):
        print(f"Pedido enviado para {pedido.cliente} por e-mail.")

class Correio(Notificador):
    """
    Classe de notificações de envio por correio.
    """

    def notificar(self, pedido:Pedido):
        print(f"Pedido enviado para {pedido.cliente} pelo Correio.")

class Pedido:
    """
    Classe de pedidos. Todo pedido é feito por um cliente. 
    """

    def __init__(self, cliente:str): #deve ser passado o nome do cliente
        self._cliente = cliente 
        self._itens = [] # o cliente inicia com o carrinho vazio e adicona produtos posteriormente

    @property
    def cliente(self):
        return self._cliente 
    
    @property
    def itens(self):
        return self._itens
    
    def adicionar_item(self, item:Produto):
        """
        Adiciona produto ao carrinho do pedido.
        
        Args:
            item (Produto): produto a ser adicionado
        """
        self.itens.append(item)
        print(f"{item.nome} adicionado ao carrinho com sucesso!")

    def visualizar_carrinho(self):
        """
        Permite visualizar os produtos que estão no carrinho de compras do pedido.
        """
        for item in self.itens:
            print(f"(->) {item.nome}: R${item.preco}")

    def calcular_total(self):
        """
        Calcula o preço total do pedido.
        """
        total = 0
        for item in self.itens:
            total += item.preco
        print(f"O preço total do seu carrinho é R${total}")

    def finalizar(self, lista_notificadores:list[Notificador]):
        """
        Finaliza a compra enviando notificação para o cliente.
        """
        for notificador in lista_notificadores:
            notificador.notificar(self)