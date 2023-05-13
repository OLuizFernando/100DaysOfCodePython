from question_model import Pergunta
from data import dados_perguntas
from quiz_brain import Quiz

banco_perguntas = []

for pergunta in dados_perguntas:
    banco_perguntas.append(Pergunta(texto=pergunta['texto'], resposta=pergunta['resposta']))

quiz = Quiz(banco_perguntas)

while quiz.ainda_tem_pergunta():
    quiz.proxima_pergunta()
    print()

print('O quiz chegou ao fim.')
print(f'Sua pontuação final foi: {quiz.pontuacao}/{quiz.numero_pergunta}')