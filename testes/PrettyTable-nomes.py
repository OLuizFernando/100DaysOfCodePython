from prettytable import PrettyTable
tabela = PrettyTable()
tabela.add_column('Nome', ['Luiz', 'Milena', 'Nina', 'Cocada', 'Amora'])
tabela.add_column('Idade', [17, 16, 14, 5, 1])
tabela.align = 'l'
print(tabela)