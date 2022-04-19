from django.shortcuts import render
from trabalho01.entity import Video,Categoria

video1 = Video()
video1.set_id(1)
video1.set_url_video("videos/animais_fantasticos3.mp4")
video1.set_url_foto("img/Animais-Fantasticos-3.jpg")
video1.set_titulo("Animais Fantásticos 3")
video1.set_descricao("Animais Fantásticos 3 - Os segredos de Dumbledore")
video1.set_curtidas(10000)
video1.set_visualizacao(240000)
video1.set_data_pub("14 de abril de 2022")

video2 = Video()
video2.set_id(2)
video2.set_url_video("videos/batman3.mp4")
video2.set_url_foto("batman.jpg")
video2.set_titulo("Batman 3")
video2.set_descricao("O mais novo filme do batman")
video2.set_curtidas(4000)
video2.set_visualizacao(20000)
video2.set_data_pub("20 de março de 2022")

video3 = Video()
video3.set_id(3)
video3.set_url_video("videos/vingadores_ultimato.mp4")
video3.set_url_foto("img/vingadores.jpg")
video3.set_titulo("Vingadores Ultimato")
video3.set_descricao("Ultimo filmes com todos os vingadores")
video3.set_curtidas(100000)
video3.set_visualizacao(3000000)
video3.set_data_pub("27 de agosto 2019")

video4 = Video()
video4.set_id(4)
video4.set_url_video("videos/doutor_estranho2.mp4")
video4.set_url_foto("img/images.jpeg")
video4.set_titulo("Doutor Estranho")
video4.set_descricao("Doutor Estranho no Multiverso da Loucura")
video4.set_curtidas(2000)
video4.set_visualizacao(30000)
video4.set_data_pub("14 de abril de 2022")

video5 = Video()
video5.set_id(5)
video5.set_url_video("videos/oscroods2.mp4")
video5.set_url_foto("img/croods.jpg")
video5.set_titulo("Os crods")
video5.set_descricao("Os croods 2 - Agora nos cinemas")
video5.set_curtidas(1000)
video5.set_visualizacao(7000)
video5.set_data_pub("19 de julho de 2022")

video6 = Video()
video6.set_id(6)
video6.set_url_video("videos/madagascar2.mp4")
video6.set_url_foto("img/madagascar2.jpg")
video6.set_titulo("Madagascar 2")
video6.set_descricao("Madagascar em mais uma aventura")
video6.set_curtidas(100)
video6.set_visualizacao(1000)
video6.set_data_pub("20 de março de 2010")

categoria1 = Categoria()
categoria1.set_id(1)
categoria1.set_descricao("Filmes de Super-Herói")
categoria1.set_titulo("Super-Herói")
categoria1.set_url_foto("categoria_sh.jpeg")
categoria1.set_videos([video2,video3,video4])

categoria2 = Categoria()
categoria2.set_id(2)
categoria2.set_descricao("Filmes de fantasia")
categoria2.set_titulo("Fantasia")
categoria2.set_url_foto("fantasia.jpg")
categoria2.set_videos([video1,video5,video6])
list_categoria = [categoria1,categoria2]
def listar_videos(request):
    return render(request, "home.html", {"categorias": list_categoria})

def ver_video(request,id:int):
    for categoria in list_categoria:
        for video in categoria.get_videos():
            if video.get_id() == id:
                return render(request,"video.html",{"video": video})
