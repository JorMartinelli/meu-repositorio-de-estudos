# A plataforma SkillSwap permite que usuários troquem aulas e mentorias entre si, sem envolver pagamento. 
# Cada Membro pode ofertar habilidades (como “guitarra”, “python”, “cozinha japonesa”) e solicitar sessões com outros membros.

# Uma Habilidade possui nome, nível de proficiência (iniciante, intermediário, avançado) e uma breve descrição. 
# Uma Sessão representa um encontro entre dois membros, e deve armazenar:

# mentor,
# aprendiz,
# habilidade ensinada,
# duração prevista,
# status (agendada, realizada, cancelada).

# Implemente um modelo orientado a objetos em Python que represente esse cenário. Inclua:

# Classes principais com seus atributos e métodos;
# Relações adequadas entre objetos (associação, composição, herança, etc.);
# Um pequeno exemplo de código criando dois membros e simulando a realização de uma sessão.

from __future__ import annotations

class Habilidade:
    """
    Classe que representa as habilidades. Toda habilidade tem um nome, nivel de proficiência e uma breve descrição.
    """

    def __init__(self, nome:str, nivel_proficiencia:str, descricao:str):
        """
        Método construtor da classe habilidade.
        
        Args:
            nome (str): nome da habilidade.
            nivel_proficiencia (str): "Iniciante", "Intermédiario" ou "Avançado.
            descricao (str): breve descrição sobre a habilidade.
        """
        self._nome = nome
        self._nivel_proficiencia = nivel_proficiencia
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome
    
    @property
    def nivel_proficiencia(self):
        return self._nivel_proficiencia
    
    @property
    def descricao(self):
        return self._descricao

class Sessao:
    """
    Classe que representa as sessões. Cada sessão é composta por dois membros. 
    """

    def __init__(self, mentor:Membro, aprendiz:Membro, habilidade:Habilidade, duracao:int):
        """
        Método construtor da classe sessão.
        
        Args:
            mentor (Membro): membro responsável por ensinar.
            aprendiz (Membro): membro que irá aprender.
            habilidade (Habilidade): habilidade que será ensinada na sessão.
            duracao (int): duracao total em horas da sessão.
        """
        self._mentor = mentor
        self._aprendiz = aprendiz
        self._habilidade_ensinada = habilidade
        self._duracao = duracao #horas
        self._status = "agendada" #por padrão, ao inicializar a sessão o "status" é "agendada". mais tarde
        #pode ser atualizado para "realizada" ou "cancelada"

    @property
    def mentor(self):
        return self._mentor
    
    @property
    def aprendiz(self):
        return self._aprendiz
    
    @property
    def habilidade_ensinada(self):
        return self._habilidade_ensinada
    
    @property
    def duracao(self):
        return self._duracao
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, novo_status):
        self._status = novo_status

class Membro:
    """
    Classe que representa um membro. Todo membro tem um nome, lista de habilidades e lista de sessões que solicitou.
    """

    def __init__(self, nome:str):
        """
        Método construtor da classe membro.
        
        Args:
            nome (str): nome do membro.
        """
        self._nome = nome
        self._habilidades = [] #armazena as habilidades do membro
        self._sessoes = [] #armazena as sessões que o membro solicitou

    @property
    def nome(self):
        return self._nome
    
    @property
    def habilidades(self):
        return self._habilidades

    @property
    def sessoes(self):
        return self._sessoes
      
    def ofertar_habilidade(self, habilidade:Habilidade):
        """
        Registra habilidade do membro.
        
        Args:
            habilidade (Habilidade): habilidade a ser ofertada.
        """
        self.habilidades.append(habilidade)
        print(f"{self.nome} ofertou {habilidade.nome}")

    def solicitar_sessao(self, mentor:Membro, habilidade:Habilidade, duracao:int):
        """
        Solicita sessão para o mentor.
        
        Args:
            mentor (Membro): mentor escolhido para aprender uma habilidade.
            habilidade (Habilidade): habilidade escolhida para aprender.
            duracao (int): tempo total em horas das sessões.
        """
        #note que "solicitar" é apenas uma simulação, ao utilizar essa função o membro já cria uma sessão
        #que por padrão tem "status"="agendada"
        sessao = Sessao(mentor, self, habilidade, duracao)
        self.sessoes.append(sessao)
        print(f"{self.nome} solicitou sessão com {mentor.nome} para a habilidade {habilidade.nome} com duração de {duracao} horas.")

    def visualizar_sessoes(self):
        """
        Mostra as sessões que o membro solicitou. 
        """
        for sessao in self.sessoes:
            print(f"-Mentor:{sessao.mentor.nome}\n Habilidade:{sessao.habilidade_ensinada.nome}\n Duração:{sessao.duracao} horas\n Status:{sessao.status}")

    def atualizar_sessao(self, numero_sessao, novo_status):
        """
        Atualiza o status da sessão selecionada pelo membro. O número da sessão é de acordo com a ordem 
        mostrada em "visualizar_sessoes".
        """
        self._sessoes[numero_sessao - 1].status = novo_status

#Driver Code
membro1 = Membro("Jordana")
membro2 = Membro("Miguel")

habilidade1 = Habilidade("Matemática", "Intermediário", "Aulas de reforço")
habilidade2 = Habilidade("Violão", "Avançado", "sem descrição")

membro1.ofertar_habilidade(habilidade2)
membro2.ofertar_habilidade(habilidade1)

membro1.solicitar_sessao(membro2, habilidade1, 2)
membro1.visualizar_sessoes()
membro1.atualizar_sessao(1, "realizada")
membro1.visualizar_sessoes()