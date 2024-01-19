with open('./Names/invited_names.txt', mode='r', encoding='utf-8') as arquivo:
    lista = arquivo.readlines()

with open('./Letters/starting_letter.txt', mode='r', encoding='utf-8') as arquivo:
    convite = arquivo.read()

mensagens_prontas = []

for i in range(0, len(lista)):
    with open(f'./Output/ReadyToSend/convite_para_{i}', mode='w', encoding='utf-8') as arquivo:
        arquivo.write(convite.replace('[nome]', lista[i]))



