from typing import List
class Video():
    def __int__(self):
        self.__id = None
        self.__url_video = None
        self.__url_foto = None
        self.__titulo = None
        self.__descricao = None
        self.__qtd_curtida = None
        self.__qtd_visualizacao = None
        self.__data_pub = None

    def set_id(self,id):
        self.__id = id
    def set_url_video(self,video):
        self.__url_video = video
    def set_url_foto(self,foto):
        self.__url_foto = foto
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def set_descricao(self,descricao):
        self.__descricao = descricao
    def set_curtidas(self,curtidas):
        self.__qtd_curtida = curtidas
    def set_visualizacao(self,visu):
        self.__qtd_visualizacao = visu
    def set_data_pub(self,data):
        self.__data_pub = data

    def get_id(self):
        return self.__id
    def get_url_video(self):
        return self.__url_video
    def get_url_foto(self):
        return self.__url_foto
    def get_descricao(self):
        return self.__descricao
    def get_titulo(self):
        return self.__titulo
    def get_qtd_curtida(self):
        return self.__qtd_curtida
    def get_qtd_visualizacao(self):
        return self.__qtd_visualizacao
    def get_data_pub(self):
        return self.__data_pub

class Categoria():
    def __int__(self):
        self.__id = None
        self.__titulo = None
        self.__descricao = None
        self.__url_foto = None
        self.__videos = None

    def set_id(self,id):
        self.__id = id
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def set_descricao(self,descricao):
        self.__descricao = descricao
    def set_url_foto(self,foto):
        self.__url_foto= foto
    def set_videos(self,videos:List):
        self.__videos = videos

    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_descricao(self):
        return self.__descricao
    def get_foto(self):
        return self.__url_foto
    def get_videos(self):
        return self.__videos

