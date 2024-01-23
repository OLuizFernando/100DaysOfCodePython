import pandas

arquivo = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240122.csv')

cinzas = len(arquivo[arquivo['Primary Fur Color'] == 'Gray'])
vermelhos = len(arquivo[arquivo['Primary Fur Color'] == 'Cinnamon'])
pretos = len(arquivo[arquivo['Primary Fur Color'] == 'Black'])

contagem_esquilos_dicio = {
    'Cor': ['cinza', 'vermelho', 'preto'],
    'Quantidade': [cinzas, vermelhos, pretos]
}
contagem_esquilos = pandas.DataFrame(contagem_esquilos_dicio)
contagem_esquilos.to_csv('./contagem_esquilos.csv')