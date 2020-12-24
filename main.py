from director import Director
from fisier import Fisier
import os


def rec_list(file_name):
    global list_file, list_dir
    if not os.listdir(file_name):
        return
    else:
        my_list = os.listdir(file_name)
        for file in my_list:
            if os.path.isdir(file_name + '\\' + file):
                list_dir.append(Director(file, file_name + '\\' + file))
                rec_list(file_name + '\\' + file)
            else:
                list_file.append(Fisier(file, file_name + '\\' + file))


list_file = []
file_path = input('Introduceti calea directorului sursa: ')
list_dir = [Director(os.path.basename(file_path), file_path)]
rec_list(file_path)
print('Lista de fisiere este:')
for i in list_file:
    print(i.name, i.abs_path)
print('Lista de directoare este:')
for i in list_dir:
    print(i.name, i.abs_path)

for director in list_dir:
    print(f'Elementele din directorul {director.name} sunt:')
    director.afisare_elemente()

for fisier in list_file:
    print(f'Continutul fisierului {fisier.name} este:')
    fisier.afisare_continut()

for fisier in list_file:
    print(f'Continutul fisierului {fisier.name} este:')
    fisier.afisare_continut_regex(r'Test\d')
