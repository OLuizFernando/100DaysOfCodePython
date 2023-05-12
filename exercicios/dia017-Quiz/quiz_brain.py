class Quiz:
    def __init__(self, lista_perguntas):
        self.numero_pergunta = 0
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