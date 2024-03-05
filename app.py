from flask import Flask, request, render_template, json
# from flask import Flask, request, Markup, render_template, json
from markupsafe import Markup, escape

app = Flask(__name__)
global usuario

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    usuario = user_text
    return user_text
    # return "Hola: " + user_text + " bienvenido " + "<br>" + "Permíteme ayudarte con el tema de la célula y sus componentes"


@app.route('/') 
def index():
    return render_template('index.html')

buttons1 = [
    Markup('<button onclick="send_message(\'significado1\')" class="custom-btn btn-16">¿Que es una celula?</button>'),
    Markup('<button onclick="send_message(\'componentes\')" class="custom-btn btn-16">Componentes de una célula</button>'),
    Markup('<button onclick="send_message(\'fcelula\')" class="custom-btn btn-16">Funcionamiento de la celula</button>'),
    Markup('<button onclick="send_message(\'salir\')" class="custom-btn btn-16">Salir</button>')
]

regresar = Markup('<button onclick="send_message(\'regresar\')" class="custom-btn btn-16">regresar</button>')

celulad = [
    Markup('<button onclick="send_message(\'funcioncel\')" class="custom-btn btn-16">Mas sobre la celula</button>'),
]

componentesop = [
    Markup('<button onclick="send_message(\'introcomp\')" class="custom-btn btn-16">Introduccion</button>'),
    Markup('<button onclick="send_message(\'membranacelu\')" class="custom-btn btn-16">Membrana celular</button>'),
    Markup('<button onclick="send_message(\'citoplasma\')" class="custom-btn btn-16">Citoplasma</button>'),
    Markup('<button onclick="send_message(\'nucleo\')" class="custom-btn btn-16">Núcleo</button>'),
    Markup('<button onclick="send_message(\'paredcelu\')" class="custom-btn btn-16">Pared celular</button>'),
]

masmembrana = [
    Markup('<button onclick="send_message(\'masmem\')" class="custom-btn btn-16">Mas sobre la membrana celular</button>'),
]
mascitoplasma = [
    Markup('<button onclick="send_message(\'mascito\')" class="custom-btn btn-16">Mas sobre el citoplasma</button>'),
]

mascitoes=[
    Markup('<button onclick="send_message(\'mascitoe\')" class="custom-btn btn-16">Mas sobre el citoesqueleto</button>'),
]

masorga=[
    Markup('<button onclick="send_message(\'masor\')" class="custom-btn btn-16">Mas sobre el organulo</button>'),
]
infoorga=[
    Markup('<button onclick="send_message(\'infor\')" class="custom-btn btn-16">Mas informacion del organulo</button>'),
]

opcito=[
    Markup('<button onclick="send_message(\'mitocondria\')" class="custom-btn btn-16">MITOCONDRIA</button>'),
    Markup('<button onclick="send_message(\'reticulaendo\')" class="custom-btn btn-16">RETÍCULO ENDOPLÁSMICO</button>'),
    Markup('<button onclick="send_message(\'aparatogolgi\')" class="custom-btn btn-16">APARATO DE GOLGI</button>'),
    Markup('<button onclick="send_message(\'lisosomas\')" class="custom-btn btn-16">LISOSOMAS</button>'),
    Markup('<button onclick="send_message(\'cloroplastos\')" class="custom-btn btn-16">CLOROPLASTOS</button>'),
]

masnucleo=[
    Markup('<button onclick="send_message(\'masnuc\')" class="custom-btn btn-16">Mas informacion del nucleo</button>'),
    Markup('<button onclick="send_message(\'funcnuc\')" class="custom-btn btn-16">Funciones del nucleo</button>'),
]
masaace=[
    Markup('<button onclick="send_message(\'infoaace\')" class="custom-btn btn-16">Mas sobre: ADN, ARN, CELULA EUCARIOTA</button>'),
    Markup('<button onclick="send_message(\'celpro\')" class="custom-btn btn-16">CÉLULA PROCARIOTA</button>'),
]
videocelup = [
    Markup('<button onclick="send_message(\'vidcelp\')" class="custom-btn btn-16">Mas sobre la celula procariota (video)</button>'),
    Markup('<button onclick="send_message(\'nucleoide\')" class="custom-btn btn-16">Nucleoide</button>'),
]

maspared=[
    Markup('<button onclick="send_message(\'maspu\')" class="custom-btn btn-16">Mas sobre la pared celular</button>'),
    Markup('<button onclick="send_message(\'presionos\')" class="custom-btn btn-16">Presion osmotica</button>'),
]

fcelulac = [
    Markup('<button onclick="send_message(\'obtennutri\')" class="custom-btn btn-16">Obtención de nutrientes</button>'),
    Markup('<button onclick="send_message(\'metabolismo\')" class="custom-btn btn-16">Metabolismo</button>'),
    Markup('<button onclick="send_message(\'reproduccion\')" class="custom-btn btn-16">Reproducción</button>'),
    Markup('<button onclick="send_message(\'comunicacion\')" class="custom-btn btn-16">Comunicación</button>'),
    Markup('<button onclick="send_message(\'elimdese\')" class="custom-btn btn-16">Elimincacion de desechos</button>'),
    
]

opreproduccion = [
    Markup('<button onclick="send_message(\'mitosis\')" class="custom-btn btn-16">Mitosis</button>'),
    Markup('<button onclick="send_message(\'meiosis\')" class="custom-btn btn-16">Meiosis</button>'),
]

opcomuni = [
    Markup('<button onclick="send_message(\'mecacoce\')" class="custom-btn btn-16">Mecanismos de comunicación celular</button>'),
]

opelimidese = [
    Markup('<button onclick="send_message(\'opelimi\')" class="custom-btn btn-16">Formas en que la célula elimina sus desechos</button>'),
]


@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    buttons = [buttons1]
    
    message_map = {
        'Comenzar': buttons,
        'Concepto': [
            f"<p class='comentario burbuja'>texto de concepto</p>",
            *buttons
        ],
        'significado1': [
            f"<p class='comentarior burbujar'>significado celula respuesta</p>",
            f"<p class='comentario burbuja'>Una célula es la unidad más pequeña y básica de la vida. Todas las formas de vida, desde organismos unicelulares como las bacterias hasta organismos multicelulares como los seres humanos que están compuestas por una o más células. Las células realizan todas las funciones necesarias para mantener la vida, como la obtención y utilización de nutrientes, la eliminación de desechos y la reproducción. Las células tienen una variedad de componentes, incluyendo una membrana celular que rodea la célula y regula el movimiento de materiales dentro y fuera de la célula, el núcleo que contiene el material genético de la célula, y el citoplasma, que es el líquido que llena la célula y contiene muchas estructuras subcelulares como los órganos.</p>",
            celulad,
            regresar
        ],
        'funcioncel': [
            f"<p class='comentarior burbujar'>Mas sobre la celula respuesta (video)</p>",
            f'<p class="comentario burbuja"> <iframe width="300" height="250" src="https://www.youtube.com/embed/aoj9oTvVJ8o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> </p>',
            regresar
        ],
        'componentes': [
            # f"<p class='comentarior burbujar'>Tema de Estructura de control <img src='../static/gifs/chatbotAnimated.gif' width='100px'></p>",
            f"<p class='comentarior burbujar'>Componentes de la celula</p>",
            componentesop,
            regresar
        ],
        'introcomp': [
            f"<p class='comentarior burbujar'>Introduccion a los componentes</p>",
            f'<p class="comentario burbuja"> Las células tienen varios componentes, algunos de los cuales son comunes a todos los tipos de células, mientras que otros son específicos de ciertos tipos de células. A continuación, se presentan algunos de los componentes comunes de una célula eucariota típica: MEMBRANA CELULAR, CITOPLASMA, NÚCLEO, PARED CELULA <br> <img src="../static/img/img1.png" width="200px"> </p>',
            componentesop,
            regresar
        ],
        'membranacelu': [
            f"<p class='comentarior burbujar'>membrana celular respuesta</p>",
            f"<p class='comentario burbuja'>Es una capa delgada y flexible que rodea la célula y la separa del entorno. Regula el intercambio de materiales entre la célula y su entorno.</p>",
            masmembrana,
            regresar
        ],
        'masmem': [
            f"<p class='comentarior burbujar'>mas de membrana celular respuesta</p>",
            f"<p class='comentario burbuja'>La membrana celular es una estructura esencial para la supervivencia de la célula, ya que regula el intercambio de materiales y protege la célula del entorno externo. Regula el movimiento de sustancias dentro y fuera de la célula, esta compuesta principalmente de fosfolípidos, proteínas y carbohidratos unidos a los fosfolípidos y las proteínas que ayudan a la célula a reconocer y comunicarse con otras células.</p>",
            componentesop,
            regresar
        ],
        'citoplasma': [
            f"<p class='comentarior burbujar'>Citoplasma respuesta</p>",
            f"<p class='comentario burbuja'>Es el líquido viscoso que llena la célula. Contiene los organulos celulares y es el lugar donde ocurren muchas de las funciones celulares.</p>",
            mascitoplasma,
            regresar
        ],
        'mascito':[
            f"<p class='comentarior burbujar'>mas del citoplasma respuesta</p>",
            f"<p class='comentario burbuja'>El citoplasma es una estructura celular que se encuentra entre la membrana celular y el núcleo. Está compuesto por un líquido llamado citosol y por diversas estructuras celulares, como orgánulos y citoesqueleto. La función del citoplasma es proporcionar soporte y estructura a la célula, permitir la realización de procesos metabólicos, transportar sustancias y moléculas dentro de la célula y permitir la movilidad y la posición de los órganos celulares.</p>",
            mascitoes, masorga,
            regresar
        ],
        'mascitoe':[
            f"<p class='comentarior burbujar'>mas del citoplaesqueleto respuesta</p>",
            f'<p class="comentario burbuja">El citoesqueleto, que forma parte del citoplasma, es una red de filamentos proteicos que proporciona soporte y ayuda a mantener la forma de la célula. También ayuda a la célula a moverse ya mantener la posición de los órganos celulares. <br> <img src="../static/img/img2.png" width="200px"> </p>',
            componentesop,
            regresar
        ],
        'masor':[
            f"<p class='comentarior burbujar'>mas del organulos respuesta</p>",
            f'<p class="comentario burbuja">Los orgánulos son estructuras membranosas que se encuentran dentro de las células eucariotas y que tienen funciones específicas en la célula. Cada tipo de orgánulo tiene una estructura y función únicas que contribuyen al funcionamiento de la célula en su conjunto. Algunos ejemplos de orgánulos en las células eucariotas incluyen: Núcleo, Mitocondrias, Retículo endoplásmico, Aparato de Golgi, Lisosomas, Cloroplastos </p>',
            componentesop, infoorga, opcito,
            regresar
        ],
        'infor':[
            f"<p class='comentarior burbujar'>Mas informacion del organulos respuesta (video)</p>",
            f'<p class="comentario burbuja"> <iframe width="300" height="250" src="https://www.youtube.com/embed/dslZxeP8qQE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> </p>',
            componentesop, opcito,
            regresar
        ],

        #JNGRESO DE LAS RESPUESTAS 5 COMPONENTES DE LOS ORGANULOS
        'mitocondria':[
            f"<p class='comentarior burbujar'> respuesta la mitocondria </p>",
            f'<p class="comentario burbuja"> Son los orgánulos encargados de la producción de energía en la célula, a través de la respiración celular </p>',
            opcito,
            regresar,
        ],
        'reticulaendo':[
            f"<p class='comentarior burbujar'> respuesta dee la reticula endoplastica </p>",
            f'<p class="comentario burbuja"> Es una red de membranas que se extiende por toda la célula y se divide en dos tipos: el retículo endoplásmico rugoso (RER), que tiene ribosomas adheridos a su superficie y se encarga de la síntesis de proteínas, y el retículo endoplásmico liso (REL), que no tiene ribosomas y se encarga de la síntesis de lípidos. </p>',
            opcito,
            regresar,
        ],
        'aparatogolgi':[
            f"<p class='comentarior burbujar'> respuesta aparato de golgi </p>",
            f'<p class="comentario burbuja"> Es el orgánulo encargado de modificar, clasificar y distribuir las proteínas y lípidos producidos por la célula. </p>',
            opcito,
            regresar,
        ],
        'lisosomas':[
            f"<p class='comentarior burbujar'> respuesta lisosomas </p>",
            f'<p class="comentario burbuja"> Son orgánulos que contienen enzimas digestivas que se encargan de la degradación de macromoléculas y de la eliminación de materiales de desecho. </p>',
            opcito,
            regresar,
        ],
        'cloroplastos':[
            f"<p class='comentarior burbujar'> respuesta cloropastos </p>",
            f'<p class="comentario burbuja"> Son orgánulos exclusivos de las células vegetales y se encargan de la fotosíntesis. </p>',
            opcito,
            regresar,
        ],


        #TEMA DEL NUCLEO
        'nucleo': [
            f"<p class='comentarior burbujar'>Nucleo respuesta</p>",
            f"<p class='comentario burbuja'>Es el centro de control de la célula, contiene el material genético de la célula, el ADN, y dirige la síntesis de proteínas y la replicación del ADN.</p>",
            masnucleo,
            regresar
        ],
        'masnuc': [
            f"<p class='comentarior burbujar'>mas del nucleo respuesta</p>",
            f"<p class='comentario burbuja'>El núcleo es una estructura celular que se encuentra en la mayoría de las células eucariotas. La función principal del núcleo es regular la expresión génica y controlar la replicación y división celular.</p>",
            masaace,
            regresar, 
        ],
        'funcnuc': [
            f"<p class='comentarior burbujar'>Funciones del nucleo tema respuesta</p>",
            f"<p class='comentario burbuja'>Almacenamiento del ADN: El ADN es esencial para la supervivencia y el funcionamiento de la célula, ya que contiene la información necesaria para la síntesis de proteínas y otras moléculas. Regulación de la expresión génica: El núcleo regula la expresión génica, es decir, qué genes se transcriben y traducen en proteínas y en qué momento. Síntesis de ARN: El ARN se transcribe a partir del ADN y luego se transporta al citoplasma, donde se traduce en proteínas. Control del ciclo celular: Controla el ciclo celular el proceso de división y crecimiento de la célula. </p>",
            masnucleo,
            regresar
        ],
        'infoaace': [
            f"<p class='comentarior burbujar'>ADN, ARN, CELULA EUCARIOTA tema respuesta</p>",
            f"<ul class='comentario burbuja'><li>El ADN (ácido desoxirribonucleico) es una molécula compleja que contiene la información genética de los organismos vivos. Su estructura única y secuencia de nucleótidos es importante para su función, incluyendo la síntesis de proteínas y la replicación celular.</li><li>El ARN (ácido ribonucleico) es una molécula de cadena única que se encuentra en todas las células vivas. El ARN desempeña varios roles importantes en la célula, incluyendo la síntesis de proteínas, la regulación génica y el procesamiento de otros tipos de ARN.</li><li>La célula eucariota es un tipo de célula que se encuentra en organismos multicelulares y unicelulares más complejos, como plantas, animales, hongos y protistas. La característica principal que distingue a las células eucariotas de las células procariotas (como las bacterias) es la presencia de un núcleo definido y separado del resto de la célula por una membrana nuclear.</li><strong>Si te interesa saber más sobre la regulación génica ve las funciones del Núcleo</strong></ul>",
            masnucleo,
            regresar
        ],
        'celpro': [
            f"<p class='comentarior burbujar'>CÉLULA PROCARIOTA tema respuesta</p>",
            f"<p class='comentario burbuja'>La célula procariota es un tipo de célula que se encuentra en organismos unicelulares, como bacterias y arqueas. A diferencia de las células eucariotas, las células procariotas no tienen un núcleo definido y separado del resto de la célula por una membrana nuclear.El material genético en las células procariotas se encuentra en una región llamada nucleoide. Las células procariotas son generalmente más pequeñas que las células eucariotas y tienen una forma más simple. </p>",
            masnucleo, videocelup, opcito,
            regresar
        ],
        'vidcelp': [
            f"<p class='comentarior burbujar'>Celula procariota tema respuesta (video)</p>",
            f'<p class="comentario burbuja"><iframe width="300" height="250" src="https://www.youtube.com/embed/vhHlWwFZakM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>',
            masnucleo,
            regresar
        ],
        'nucleoide': [
            f"<p class='comentarior burbujar'>Nucleoide tema respuesta</p>",
            f'<p class="comentario burbuja"> El nucleoide es la región en una célula procariota donde se encuentra el material genético de la célula. Aunque el nucleoide no está rodeado por una membrana nuclear, está organizado y estructurado por proteínas y enzimas especiales que ayudan a empacar y organizar el ADN. El ADN en el nucleoide es esencial para la supervivencia de la célula, ya que contiene la información genética necesaria para la síntesis de proteínas y la replicación celular. <br> <img src="../static/img/img3.png" width="200px"> </p>',
            masnucleo,
            regresar
        ],

        #TEMA DE LA PARED CELULAR
        'paredcelu': [
            f"<p class='comentarior burbujar'>Pared celular respuesta</p>",
            f"<p class='comentario burbuja'>Proporciona soporte y protección a la célula, manteniendo su forma y evitando que se dañe bajo presión osmótica. Además, también puede actuar como una barrera selectiva para el movimiento de sustancias.</p>",
            maspared,
            regresar
        ],
        'maspu': [
            f"<p class='comentarior burbujar'>Mas sobre la pared celulartema respuesta</p>",
            f"<p class='comentario burbuja'>La pared celular es una estructura rígida presente en algunas células, como las células vegetales, las células fúngicas y las células bacterianas, su función principal es proporcionar soporte y protección a la célula, manteniendo su forma y evitando que se dañe bajo presión osmótica.  En las células vegetales, la pared celular está compuesta principalmente de celulosa, mientras que en las células fúngicas está compuesta de quitina. En las células bacterianas, la pared celular está compuesta de peptidoglicano.</p>",
            regresar,
        ],
        'presionos': [
            f"<p class='comentarior burbujar'>Presion osmotica tema respuesta</p>",
            f"<p class='comentario burbuja'>La presión osmótica se refiere a la tendencia de las células a absorber agua, lo que puede hacer que se hinchen y exploten si no tienen una pared celular resistente para mantener su forma.</p>",
            regresar,
        ],

        #FUNCIONAMIENTO DE UNA CÉLULA
        'fcelula':[
            f"<p class='comentarior burbujar'>Funcion de la celula tema respuesta</p>",
            f"<ul class='comentario burbuja'>El funcionamiento de una célula es extremadamente complejo y varía dependiendo del tipo de célula y de su función en el organismo. Sin embargo, a continuación se presentan algunos conceptos básicos que ocurren en la mayoría de las células:<li>Obtención de nutrientes: Las células necesitan nutrientes para obtener energía y construir moléculas necesarias para su supervivencia.</li> <li>Metabolismo: Una vez que las células han obtenido nutrientes, las moléculas son procesadas en el citoplasma y en los órganos celulares para obtener energía y construir nuevas estructuras.</li><li>Reproducción: Las células pueden reproducirse mediante la división celular, en la que una célula se divide en dos células hijas idénticas. Este proceso es esencial para el crecimiento y la reparación de los tejidos del cuerpo.</li><li>Comunicación: Las células pueden comunicarse entre sí y con su entorno mediante señales químicas que pueden activar o desactivar ciertas funciones celulares.</li><li>Eliminación de desechos: Los lisosomas y otros orgánulos desempeñan un papel importante en la eliminación de desechos celulares.</li></ul>",
            fcelulac, 
            regresar
        ],  
        'obtennutri': [
            f"<p class='comentarior burbujar'>Obtencion de nutrientes tema respuesta</p>",
            f"<ul class='comentario burbuja'>Las células obtienen nutrientes a través de dos vías principales:<li>Transporte pasivo: Este proceso implica el movimiento de moléculas y iones a través de la membrana celular sin gasto de energía, puede ocurrir por difusión simple, o por ósmosis.</li><li>Transporte activo: Este proceso requiere el gasto de energía celular para mover moléculas y iones en contra de su gradiente de concentración. </li>Una vez dentro de la célula, los nutrientes pueden ser utilizados para diferentes procesos metabólicos, como la producción de energía a través de la respiración celular, la síntesis de proteínas y la formación de nuevas células durante la división celular.</ul>",
            regresar,
        ],
        'metabolismo': [
            f"<p class='comentarior burbujar'>metabolismo tema respuesta</p>",
            f"<p class='comentario burbuja'>El metabolismo de una célula es el conjunto de reacciones químicas que ocurren en su interior para mantener su funcionamiento, crecimiento y reproducción. La mayoría de las células utilizan el proceso de respiración celular para obtener energía. Además de la respiración celular, las células también pueden obtener energía a través de la fermentación y la fotosíntesis en el caso de las células fotosintéticas.</p>",
            regresar,
        ],
        'reproduccion': [
            f"<p class='comentarior burbujar'>Reproduccion tema respuesta</p>",
            f"<p class='comentario burbuja'>La reproducción de una célula se lleva a cabo a través del proceso de división celular, que se divide en dos tipos principales: la mitosis y la meiosis.</p>",
            opreproduccion,
            regresar
        ],
        'comunicacion': [
            f"<p class='comentarior burbujar'>Comunicacion tema respuesta</p>",
            f"<p class='comentario burbuja'>La comunicación celular es el proceso por el cual las células intercambian información entre sí para coordinar sus funciones y mantener la homeostasis en el organismo. </p>",
            regresar
        ],
        'elimdese': [
            f"<p class='comentarior burbujar'>Eliminacion de desechos tema respuesta</p>",
            f"<p class='comentario burbuja'>La eliminación de desechos de la célula es un proceso importante para mantener la homeostasis y prevenir daño celular. Los desechos celulares se generan como resultado del metabolismo celular normal, así como de procesos de reparación y eliminación de células muertas o dañadas.</p>",
            opelimidese,
            regresar
        ],
        #opciones de reproduccion
        'mitosis': [
            f"<p class='comentarior burbujar'>Mitosis tema respuesta</p>",
            f"<p class='comentario burbuja'>La mitosis es el proceso de división celular que ocurre en las células somáticas o células no reproductoras. En este proceso, una célula madre se divide en dos células hijas genéticamente idénticas, que contienen la misma cantidad de cromosomas y material genético. La mitosis se lleva a cabo en cuatro etapas principales: la profase, la metafase, la anafase y la telofase.</p>",
            regresar
        ],
        'meiosis': [
            f"<p class='comentarior burbujar'>Meiosis tema respuesta</p>",
            f"<p class='comentario burbuja'>La meiosis es el proceso de división celular que ocurre en las células reproductoras. En este proceso, una célula madre se divide en cuatro células hijas, cada una con la mitad del número de cromosomas y la mitad del material genético de la célula madre. La meiosis se lleva a cabo en dos etapas principales: la meiosis I y la meiosis II, cada una de las cuales consta de profase, metafase, anafase y telofase.</p>",
            regresar
        ],
        #opciones de comunicacion
        'mecacoce': [
            f"<p class='comentarior burbujar'>Mecanismos de comunicación celular tema respuesta</p>",
            f"<ul class='comentario burbuja'><li>Comunicación directa: Ocurre entre células que están en contacto físico a través de canales de comunicación especializados llamados uniones de hendidura. </li><li>Señalización paracrina: Ocurre cuando las células liberan moléculas señalizadoras, llamadas factores de crecimiento, en el medio extracelular cercano. Estos factores pueden actuar sobre células cercanas y estimular su crecimiento y diferenciación.</li><li>Señalización endocrina: Ocurre cuando las células liberan moléculas señalizadoras en el torrente sanguíneo, que luego actúan sobre células distantes en diferentes partes del cuerpo.</li><li>Señalización autocrina: Ocurre cuando las células liberan moléculas señalizadoras que actúan sobre la propia célula que las produce, estimulando su crecimiento y actividad.</li><li>Señalización neuronal: Ocurre en el sistema nervioso, donde las células nerviosas utilizan neurotransmisores para transmitir información entre sí.</li></ul>",
            regresar
        ],
        #opciones de la eliminacion de desechos
        'opelimi': [
            f"<p class='comentarior burbujar'>Formas en que la célula elimina sus desechos tema respuesta</p>",
            f"<ul class='comentario burbuja'><li>Exocitosis: Es un proceso en el cual los desechos se empaquetan en vesículas y se liberan fuera de la célula.</li><li>Fagocitosis: En este proceso, las células especializadas llamadas fagocitos engullen y degradan materiales extraños o desechos celulares mediante la fusión de vesículas de digestión con los lisosomas.</li><li>Autófagos: En este proceso, la célula digiere su propio material celular, a través de la formación de autófagosomas que se fusionan con lisosomas.</li><li>Difusión: Algunos productos de desecho pueden difundirse directamente a través de la membrana celular y ser eliminados por difusión a través del medio extracelular.</li></ul>",
            regresar
        ],
        #SALIR
        'salir': [
            f"<p id='estado' class='comentarior burbujar'>Hasta luego</p>",
            f"<p id='estado' class='comentario burbuja'>Nos vemos, buen dia</p>"
        ],
        'regresar': buttons
    }   
    return message_map.get(message, "Lo siento, no entendí tu mensaje.")

#if __name__ == '__main__':
    #app.run(debug=True)

#SET FLASK_APP=app.py
#python app.py
