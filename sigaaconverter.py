import argparse
import curses

characters = {'M': ["Manhã", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00"], 'T': [
    "Tarde", "14:00", "15:00", "16:00", "17:00"], 'N': ["Noite", "18:00", "19:00", "20:00", "21:00", "22:00"]}
dias = {'2': "Segunda", '3': "Terça",
        '4': "Quarta", '5': "Quinta", '6': "Sexta"}
dias_formato_fudido = ['M', 'T', 'N']


def beautify(lista_final):
    print("AQUI SEU HORÁRIO BRO:\n")
    print("------------------------------------")
    print("| => " + lista_final[0])
    for dias in lista_final[1]:
        print("| - " + dias)
    print("| Horários:")
    for horarios in lista_final[2]:
        print("| - " + horarios)
    print("------------------------------------\n")


def formatar(lista_formatada):
    _list = list()
    _list.append(characters[lista_formatada[0]][0])
    _list.append(list())
    _list.append(list())
    # print(_list)
    for days in lista_formatada[1]:
        _list[1].append(dias[days])
    # print(_list)
    for hours in lista_formatada[2]:
        _list[2].append(characters[lista_formatada[0]][int(hours)])
    # print(_list)
    return _list


def split(word):
    return [char for char in word]


def converter(horario):
    lista_horarios = list()
    lista_formatada = list()
    for char in horario:
        if char in dias_formato_fudido:
            lista_horarios = horario.split(char)
            lista_formatada.append(char)

            horarios_1 = list(split(lista_horarios[0]))
            horarios_2 = list(split(lista_horarios[1]))

            lista_formatada.append(horarios_1)
            lista_formatada.append(horarios_2)

    return formatar(lista_formatada)


def main():
    while(1):
        try:
            print("INSIRA SEU HORÁRIO BRO:")
            horario = input()
            lista_final = list(converter(horario))
            beautify(lista_final)
        except:
            print(
                "Horário não reconhecido bro. Tem certeza que escreveu certo?")


main()
