class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'
        
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
    
    def __getitem__(self, item):
        return self._programas[item]        
                
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tlou = Serie('The last of us', 2023, 1)
dvpf = Filme("de volta pro futuro", 1985, 120)
tbbt = Serie("The big bang theory", 2007, 12)

dvpf.dar_likes()
dvpf.dar_likes()
dvpf.dar_likes()
dvpf.dar_likes()
dvpf.dar_likes()
dvpf.dar_likes()
tbbt.dar_likes()
tbbt.dar_likes()
tbbt.dar_likes()
tbbt.dar_likes()
tbbt.dar_likes()
tbbt.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tlou.dar_likes()
tlou.dar_likes()
tlou.dar_likes()
tlou.dar_likes()
tlou.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {tlou.nome} - Likes: {tlou.likes}')

filmes_e_series = [vingadores, tbbt, dvpf, tlou]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
  
  
class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Junior(Alura):
    pass
''
class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()