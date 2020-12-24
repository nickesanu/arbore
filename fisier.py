import re


class Fisier:
    def __init__(self, name, abs_path):
        self.name = name
        self.abs_path = abs_path

    def afisare_continut(self):
        with open(self.abs_path, mode='rt') as f:
            my_list = f.readlines()
            for line in my_list:
                print(line.rstrip('\n'))

    def afisare_continut_regex(self, regex):
        with open(self.abs_path, mode='rt') as f:
            my_list = f.readlines()
            for line in my_list:
                if re.search(regex, line.rstrip('\n')):
                    print(line.rstrip('\n'))
                    
print('spaima hackerului chinez loveste dinou')
