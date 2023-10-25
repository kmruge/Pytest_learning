import json


class Student:
    def __int__(self):
        self.__json_File=None

    def loadFile(self,filePath):
        with open(filePath) as file:
            self.__json_File=json.load(file)

    def get_data(self,name,ObjectName):
        for dict1 in self.__json_File[ObjectName]:
            if dict1["name"]==name:
                return dict1