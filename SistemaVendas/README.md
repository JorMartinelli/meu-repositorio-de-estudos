# Sistema de Gerenciamento de Pedidos (POO Python) 🛒

Este projeto é um sistema simplificado de e-commerce que demonstra a aplicação de conceitos de **Programação Orientada a Objetos (POO)** em Python, como herança, encapsulamento, classes abstratas e polimorfismo.

## 🚀 Funcionalidades

- **Gestão de Produtos:** Suporte para produtos físicos e digitais.
- **Carrinho de Compras:** Adição de itens, visualização de carrinho e cálculo automático do total.
- **Sistema de Notificações Flexível:** Utiliza o padrão de projeto para disparar diferentes tipos de notificações (E-mail, Correio, etc.) de forma extensível.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Módulo ABC (Abstract Base Classes):** Para garantir a estrutura das classes filhas.
- **Type Hinting:** Para melhor legibilidade e manutenção do código.

## 📐 Estrutura do Código

O projeto utiliza uma classe abstrata `Produto` que serve de base para `ProdutoFisico` e `ProdutoDigital`. O sistema de notificações segue a mesma lógica, permitindo que novos métodos de envio sejam adicionados sem alterar a lógica principal do `Pedido`.