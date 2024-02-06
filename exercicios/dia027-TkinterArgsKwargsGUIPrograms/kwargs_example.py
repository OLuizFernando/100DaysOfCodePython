# **kwargs (unlimited key word arguments)
class Pc:
    def __init__(self, **kwargs):
        self.nome = kwargs.get('nome')
        self.cpu = kwargs.get('cpu')
        self.ram = kwargs.get('ram')
        self.ssd = kwargs.get('ssd')
        self.os = kwargs.get('os')
        print(kwargs)


desktop = Pc(cpu='Intel Core i5-10400F', ram=16, ssd=1024, os='Windows 10')
laptop = Pc(nome='Asus Vivobook 16', cpu='Intel Core i7-1255U', ram=16, ssd=512, os='Windows 11')

print(desktop.cpu)
print(laptop.cpu)
