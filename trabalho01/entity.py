from typing import List


class Video:
    def __int__(self,id,url_video,url_foto,titulo,descricao,qtd_curtida,qtd_visualizacao,data_pub):
        self.__id = id
        self.__url_video = url_video
        self.__url_foto = url_foto
        self.__titulo = titulo
        self.__descricao = descricao
        self.__qtd_curtida = qtd_curtida
        self.__qtd_visualizacao = qtd_visualizacao
        self.__data_pub = data_pub

class Categoria:
    def __int__(self,id,titulo,descricao,foto,videos:List):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__url_foto = foto
        self.__videos = videos


