import os
import re


class Director:
    def __init__(self, name, abs_path):
        self.name = name
        self.abs_path = abs_path

    def afisare_elemente(self):
        print(os.listdir(self.abs_path))

    def afisare_elemente_regex(self, regex):
        my_list = os.listdir(self.abs_path)
        for elem in my_list:
            if re.search(regex, elem):
                print(elem)
