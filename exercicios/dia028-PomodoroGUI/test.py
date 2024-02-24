from time import sleep


def contador(minutos):
    segundos = minutos * 60
    for i in range(segundos):
        mins, secs = divmod(segundos - i, 60)
        print(f'{mins:02d}:{secs:02d}')
        sleep(1)