# ⚔️ RPG Battle Simulator

Um simulador de batalha utiliza os pilares fundamentais da Programação Orientada a Objetos. O projeto coloca um Herói contra um Inimigo em um combate dinâmico com cálculos de dano aleatórios.

## 🕹️ Funcionalidades
- **Sistema de Turnos:** O jogador escolhe entre ataques normais e especiais.
- **Cálculo de Dano Dinâmico:** O dano é calculado com base no nível do personagem e um fator de aleatoriedade.
- **Gerenciamento de Estado:** O jogo monitora os pontos de vida e encerra a batalha quando um dos personagens é derrotado.

## 🧠 Conceitos de POO Aplicados
- **Herança:** As classes `Heroi` e `Inimigo` herdam os atributos e métodos base da classe `Personagem`.
- **Encapsulamento Privado:** Uso de `__atributos` para restringir o acesso direto aos dados, utilizando métodos `get` para recuperação.
- **Polimorfismo (Sobrescrita de Método):** O método `exibir_detalhes` foi sobrescrito nas subclasses para incluir informações específicas (Habilidade ou Tipo) mantendo a base da classe pai.