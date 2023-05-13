from data import dados_perguntas

class Quiz:
    def __init__(self, lista_perguntas):
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.lista_perguntas = lista_perguntas

    def ainda_tem_pergunta(self):
        return self.numero_pergunta < len(self.lista_perguntas)

    def proxima_pergunta(self):
        pergunta_atual = self.lista_perguntas[self.numero_pergunta]
        self.numero_pergunta += 1
        while True:
            resposta_usuario = input(f'Q.{self.numero_pergunta}: {pergunta_atual.texto}\n(V/F): ')
            if resposta_usuario.strip().lower()[0] in 'vf':
                break
            else:
                print(f'Erro: "{resposta_usuario}" não é uma resposta válida.')
        self.conferir_resposta(resposta_usuario, pergunta_atual.resposta)

    def conferir_resposta(self, resposta_usuario, resposta_certa):
        if resposta_usuario.strip().lower()[0] == resposta_certa.strip().lower()[0]:
            print('ACERTOU!')
            self.pontuacao += 1
        else:
            print('ERROU!')
            print(f'A resposta certa seria: {resposta_certa}.')
        if self.numero_pergunta < len(dados_perguntas):
            print(f'Sua pontuação atual é: {self.pontuacao}/{self.numero_pergunta}')