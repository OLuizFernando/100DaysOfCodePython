# *args (unlimited arguments)
def somar_tudo(*args):
    return sum(args)


print(somar_tudo(1, 2, 3, 4, 5))