class Capital ():
    def __init__(self):
        self.__capitales = {
            'Leticia'               :'https://marandua.com.co/wp-content/uploads/2020/05/LETICIA-AMAZONAS.jpg',
            'Medellín'              :'https://images.pexels.com/photos/4150118/pexels-photo-4150118.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
            'Arauca'                :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnpKMJkBcQSirTr8CQvEAE8Z8ISNVmiYxK0w&usqp=CAU',
            'Barranquilla'          : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6Zbf0gm7TgNBCTwYMzj50r5WfThjGXUh8ng&usqp=CAU',
            'Cartagena'             :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE3_B2TNVp2-98DKFjZdMlYnNvmOqPCCqbNw&usqp=CAU',
            'Tunja'                 :'https://boyaca7dias.com.co/wp-content/uploads/2020/07/plaza-de-bolivar-tunja2.jpeg',
            'Manizales'             :'https://archivo.autonoma.edu.co/sites/default/files/imagenes-articulos/imagen-principal/_dsc0374.jpg',
            'Florencia'             :'https://s3.amazonaws.com/elcomun/imagenes/1571405665.jpg',
            'Yopal'                 :'https://laschivasdelllano.com/wp-content/uploads/2019/06/yopal.png',
            'Popayán'               :'https://i.ytimg.com/vi/T1DjgdA4XCY/maxresdefault.jpg',
            'Valledupar'            :'https://www.semana.com/resizer/PdO6nBq-XiFPVf7fDpcbRz9963E=/1200x675/filters:format(jpg):quality(50)//cloudfront-us-east-1.images.arcpublishing.com/semana/KVPUERVYS5EUXIDCHYBMR6HWGE.jpg', 
            'Quibdó'                :'https://comisiondelaverdad.co/images/zoo/noticias/images/aberre-fotorrelato-quibdo.jpg',
            'Montería'              :'https://cloudfront-us-east-1.images.arcpublishing.com/semana/6USSCRY72NBRBCYS4YEA5M3N2Y.jpg',
            'Bogota'                :'https://bogota.gov.co/sites/default/files/styles/1050px/public/2021-11/ley-seca-en-bogota.jpeg',
            'Inírida'               :'https://www.desdeabajo.info/media/k2/items/cache/68f3bd8850dcd3eb0a89a5d03eec0af0_L.jpg',
            'San José del Guaviare' :'https://media-cdn.tripadvisor.com/media/photo-s/13/1b/5d/af/se-le-nota-el-photoshop.jpg',
            'Neiva'                 :'https://files.rcnradio.com/public/2020-05/neiva_alejandra_herrera_2_0.jpg',
            'Riohacha'              :'https://asawaa.com/wp-content/uploads/2020/01/yoamoriohacha.jpg',
            'Santa Marta'           :'https://www.eltiempo.com/uploads/2019/06/21/5d0d138fba6c7.jpeg',
            'Villavicencio'         :'https://files.rcnradio.com/public/2021-05/img-20210428-wa0352_2_0.jpg?dZpm3jKcZuTED0twOgMHeLvNEElzemk8',
            'Pasto'                 :'https://i0.wp.com/mejoreszonas.com/wp-content/uploads/2019/12/Las-mejores-zonas-donde-alojarse-en-Pasto-Colombia.jpg?fit=2000%2C1156&ssl=1',
            'Cúcuta'                :'https://photo620x400.mnstatic.com/a43d0895dcd22d1f50d95fb47030d930/yo-amo-a-cucuta.jpg',
            'Mocoa'                 :'http://laburramocha.pty.com.co/wp-content/uploads/2020/10/mocoa-mao.jpg',
            'Armenia'               :'https://www.cronicadelquindio.com/files/noticias/120200527083602.jpg',
            'Pereira'               :'https://s3.amazonaws.com/images.vive.travel/images/8772/xlarge/sitios-para-visitar-en-pereira.jpg?1566508064',
            'San Andrés'            :'https://media.staticontent.com/media/pictures/ecc404e8-9a99-46b0-a56a-ead992b5166e',
            'Bucaramanga'           :'https://colombiapais.com/principales-destinos/imagenes/bucaramanga-panoramica-atardecer.jpg',
            'Sincelejo'             :'https://corpsur.b-cdn.net/wp-content/uploads/2019/10/Sincelejo-entre-las-3-mejores-ciudades-para-invertir.jpeg',
            'Ibagué'                :'https://ibague.gov.co/portal/admin/archivos/imagenes/noticias/2017/2297/20170214-2297-1.jpg',
            'Cali'                  :'https://elsolweb.tv/wp-content/uploads/2018/06/Cali.jpg',
            'Mitú'                  :'https://cdn.colombia.com/images/v2/turismo/sitios-turisticos/mitu/rio-amazonas-mitu-800.jpg',
            'Puerto Carreño'        :'https://encolombia.com/wp-content/uploads/2020/02/Turismo-en-Puerto-Carre%C3%B1o-696x398.jpg',
            'Madrid'                :'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Plaza_Mayor_de_Madrid_06.jpg/1024px-Plaza_Mayor_de_Madrid_06.jpg',
            'Londres'               :'https://www.tododisca.com/wp-content/uploads/2019/05/Londres-Portada-1-750x500.jpg',
            'New York'              :'https://www.ngenespanol.com/wp-content/uploads/2018/08/Nuevo-museo-en-la-Estatua-de-la-Libertad.jpg',
            'Buenos Aires'          :'https://imagenes.elpais.com/resizer/EmX_Udn3DVVOIYssB1sA8D1Tr-0=/1960x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/ENYYXKTTXZHHRP5BV4ZAEEUO2A.jpg',
        }

    def url_capital(self, capital):
        url =   self.__capitales.get(capital)
        return url

    


c=Capital()

