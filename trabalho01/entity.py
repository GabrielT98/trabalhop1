from typing import List


class Video:
    def __int__(self,id:int,url_video:str,url_foto:str,titulo:str,descricao:str,qtd_curtida:int,qtd_visualizacao:int,data_pub:str):
        self.__id = id
        self.__url_video = url_video
        self.__url_foto = url_foto
        self.__titulo = titulo
        self.__descricao = descricao
        self.__qtd_curtida = qtd_curtida
        self.__qtd_visualizacao = qtd_visualizacao
        self.__data_pub = data_pub

class Categoria:
    def __int__(self,id:int,titulo:str,descricao:str,foto:str,videos:List):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__url_foto = foto
        self.__videos = videos


