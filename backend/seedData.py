from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
from models import Usuario, Receta, Ingrediente, ListaCompra
import random

DATABASE_URL = "postgresql://recetario_db_umim_user:dKZeM7dUPtt4HkS0TNB7BoWp5goBNyb5@dpg-d3jaanili9vc73a6u7dg-a.frankfurt-postgres.render.com/recetario_db_umim"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

usuarios = [
    Usuario(username="Aitor Etxeberria", email="aitor@example.com", password="12435"),
    Usuario(username="Nerea Irigoyen", email="nerea@example.com", password="yhytfhtbhty"),
    Usuario(username="Jon Mendizabal", email="jon@example.com", password="ythbtyhbtr"),
    Usuario(username="Amaia Goikoetxea", email="amaia@example.com", password="gbhfgtrgf"),
    Usuario(username="Mikel Olazabal", email="mikel@example.com", password="rtvgrtfg"),
    Usuario(username="Leire Garate", email="leire@example.com", password="trvgrtf"),
]
session.add_all(usuarios)
session.commit()

recetas_data = [
    {
        "nombre": "Marmitako",
        "preparacion": """<ol>
            <li><p>Prepara los ingredientes: pela y pica finamente la cebolla, corta el pimiento en dados pequeños y lamina o pica los ajos. Pela las patatas y córtalas en trozos irregulares (romperlas con el cuchillo ayuda a espesar el caldo). Corta el bonito en dados de tamaño regular y resérvalo en frío.</p></li>
            <li><p>En una cazuela amplia calienta el aceite de oliva a fuego medio. Añade la cebolla y el pimiento y pocha con una pizca de sal hasta que la cebolla esté transparente y suave (8–10 min). Incorpora el ajo y rehoga 1 minuto más sin que se dore.</p></li>
            <li><p>Agrega el pimentón dulce, remueve rápidamente para que no se queme y añade inmediatamente el tomate triturado. Cocina a fuego medio-bajo hasta que el tomate reduzca y pierda el agua (6–8 min), removiendo de vez en cuando.</p></li>
            <li><p>Incorpora las patatas a la cazuela y rehógalas 2–3 minutos para que se impregnen del sofrito. Cubre con agua o con un fumet ligero de pescado hasta que sobre 1–2 cm por encima de las patatas. Sube el fuego hasta llevar a ebullición y después baja a fuego medio.</p></li>
            <li><p>Añade sal y pimienta al gusto y deja cocer con la cazuela semi-tapada unos 20–30 minutos, hasta que las patatas estén tiernas al pincharlas. Si es necesario, añade más caldo o agua caliente durante la cocción.</p></li>
            <li><p>Cinco minutos antes de terminar, incorpora los dados de bonito y cuece a fuego suave (no hierva fuerte para evitar que el bonito se reseque) hasta que el pescado esté hecho pero jugoso (3–5 min).</p></li>
            <li><p>Rectifica de sal y pimienta. Apaga el fuego y deja reposar 2–3 minutos antes de servir para que los sabores se asienten. Sirve caliente, opcionalmente con perejil picado o un chorrito de aceite crudo por encima.</p></li>
            </ol>
            <p>Consejos: si usas bonito muy fresco, añádelo casi al final para que quede jugoso; si usas atún, el tiempo es similar. No dejes hervir el pescado fuerte para evitar que se desmenuce demasiado.</p>""",
        "tiempo_preparacion": "1 hora",
        "imagen_url": "https://imag.bonviveur.com/marmitako-de-bonito_1000.webp",
        "video_url": "https://www.youtube.com/watch?v=6XlgTBAM-WM",
        "ingredientes": [
            {"nombre": "Bonito del norte", "cantidad": 400, "unidad": "gr"},
            {"nombre": "Patatas", "cantidad": 600, "unidad": "gr"},
            {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Pimiento verde", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Ajo", "cantidad": 2, "unidad": "dientes"},
            {"nombre": "Tomate triturado", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Aceite de oliva", "cantidad": 60, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 8, "unidad": "gr"},
            {"nombre": "Pimienta negra", "cantidad": 3, "unidad": "gr"},
            {"nombre": "Pimentón dulce", "cantidad": 5, "unidad": "gr"},
        ]
    },
    {
        "nombre": "Txangurro",
        "preparacion": """<ol>
            <li><p>Si el centollo está entero, abre el caparazón con cuidado y extrae toda la carne, reservando también la parte interior del caparazón limpia para presentar. Separa la carne de posibles cartílagos y trocéala en pedacitos.</p></li>
            <li><p>Pica finamente la cebolla. En una sartén amplia calienta el aceite y pocha la cebolla a fuego medio-bajo hasta que esté muy tierna y casi caramelizada (10–12 min). Añade el tomate rallado o triturado y cocina hasta que reduzca y el agua se haya evaporado (6–8 min).</p></li>
            <li><p>Incorpora la carne del centollo a la sartén, mezcla bien y añade sal y pimienta al gusto. Vierte el brandy, sube el fuego y, si te sientes cómodo, flamea para evaporar el alcohol (con cuidado y manteniendo distancia) o deja que reduzca a fuego vivo para concentrar el sabor.</p></li>
            <li><p>Prueba y rectifica de sal y pimienta. Si la mezcla queda muy líquida, deja reducir un poco más o añade una cucharada de pan rallado para espesar ligeramente.</p></li>
            <li><p>Rellena los caparazones (o cazuelitas individuales) con la mezcla de centollo. Espolvorea una capa fina de pan rallado por encima y añade una pequeña porción de mantequilla o un chorrito de aceite para que dore.</p></li>
            <li><p>Gratina en el horno precalentado a 200 °C durante 5–8 minutos hasta que la superficie quede dorada y crujiente. Sirve inmediatamente para que conserve la textura.</p></li>
            </ol>
            <p>Consejos: puedes añadir un chorrito de nata para ligar la mezcla si la quieres más cremosa, y una pizca de perejil picado para dar frescor al final.</p>""",
        "tiempo_preparacion": "50 minutos",
        "imagen_url": "https://cdn.elcocinerocasero.com/imagen/paso-receta/1000/2021-02-19-20-04-23/txangurro-a-la-donostiarra-paso-9.jpeg",
        "video_url": "https://www.youtube.com/watch?v=xxrtez55Zak",
        "ingredientes": [
            {"nombre": "Centollo cocido", "cantidad": 400, "unidad": "gr"},
            {"nombre": "Cebolla", "cantidad": 120, "unidad": "gr"},
            {"nombre": "Tomate", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Pan rallado", "cantidad": 50, "unidad": "gr"},
            {"nombre": "Brandy", "cantidad": 30, "unidad": "ml"},
            {"nombre": "Aceite de oliva", "cantidad": 40, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 5, "unidad": "gr"},
            {"nombre": "Pimienta", "cantidad": 2, "unidad": "gr"},
        ]
    },
    {
        "nombre": "Bacalao a la vizcaína",
        "preparacion": """<ol>
            <li><p>Si utilizas pimientos choriceros secos, hidrátalos en agua caliente durante 20–30 minutos y extrae la pulpa raspando con una cuchara. Reserva la pulpa. Si usas pulpa ya preparada, pasa al siguiente paso.</p></li>
            <li><p>Pica la cebolla y lamina los dientes de ajo. En una sartén amplia y con fondo calienta el aceite a fuego medio y pocha la cebolla lentamente hasta que esté muy blanda y translúcida (10–12 min). Añade el ajo y rehoga 1 minuto.</p></li>
            <li><p>Incorpora el tomate triturado y cocina a fuego bajo hasta que el tomate pierda parte de su agua y la mezcla tenga textura de salsa (10–12 min). Añade la pulpa de pimiento choricero y mezcla bien; cocina 5–8 minutos más para integrar sabores. Si prefieres una salsa lisa, tritura y cuela la salsa.</p></li>
            <li><p>Comprueba que el bacalao está desalado; si no, desálalo con antelación (remojar en agua fría 24–48 h cambiando el agua). Escurre y seca los lomos con papel de cocina.</p></li>
            <li><p>En una sartén aparte marca ligeramente los lomos de bacalao por el lado de la piel (unos 1–2 minutos a fuego fuerte) para sellarlos, o cuécelos directamente en la salsa a fuego muy suave.</p></li>
            <li><p>Coloca el bacalao sobre la salsa y cocina a fuego muy bajo durante 4–6 minutos, dependiendo del grosor, hasta que el pescado esté tierno y se desmenuce al probar con un tenedor.</p></li>
            <li><p>Sirve cada lomo bañado con abundante salsa vizcaína y, si quieres, acompaña con unas patatas cocidas o al vapor.</p></li>
            </ol>
            <p>Consejos: ajusta la sal al final (si el bacalao ha sido desalado, puede requerir poco sal). La textura y el color de la salsa son claves: debe ser brillante y con cuerpo.</p>""",
        "tiempo_preparacion": "45 minutos",
        "imagen_url": "https://imag.bonviveur.com/bacalao-a-la-vizcaina-receta-tradicional.jpg",
        "video_url": "https://www.youtube.com/watch?v=5Su1VDmqnrU",
        "ingredientes": [
            {"nombre": "Bacalao desalado", "cantidad": 500, "unidad": "gr"},
            {"nombre": "Pimiento choricero", "cantidad": 2, "unidad": "unidad"},
            {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Tomate triturado", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Ajo", "cantidad": 3, "unidad": "dientes"},
            {"nombre": "Aceite de oliva", "cantidad": 70, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 7, "unidad": "gr"},
            {"nombre": "Pimienta", "cantidad": 3, "unidad": "gr"},
        ]
    },
    {
        "nombre": "Pintxos variados",
        "preparacion": """<ol>
            <li><p>Corta la barra de pan en rebanadas de 1–1.5 cm y tuéstalas ligeramente por ambos lados hasta que queden crujientes pero no demasiado duras.</p></li>
            <li><p>Pintxo clásico jamón y tomate: frota cada rebanada con un diente de ajo cortado por la mitad (opcional), frota tomate maduro por la superficie y añade una loncha de jamón serrano. Añade un chorrito de aceite de oliva y una pizca de sal.</p></li>
            <li><p>Pintxo de queso y pimiento: coloca una loncha de queso Idiazabal sobre la rebanada ligeramente tostada, añade una tira de pimiento del piquillo y, si te gusta, gratina unos segundos para que el queso funda ligeramente.</p></li>
            <li><p>Pintxo de anchoa y aceituna: coloca una anchoa en salazón sobre la rebanada, añade media aceituna troceada o una cucharada pequeña de tapenade y un hilo de aceite de oliva.</p></li>
            <li><p>Montajes alternativos: combina pan, tomate rallado, un trozo de queso y jamón; o utiliza pimientos asados con anchoa; o una base de crema de queso con salmón ahumado. Fija los pintxos con un palillo si llevan varias capas.</p></li>
            <li><p>Dispón los pintxos en una bandeja y sirve a temperatura ambiente o ligeramente templados.</p></li>
            </ol>
            <p>Consejos: prepara los pintxos justo antes de servir para que el pan conserve la textura; adapta cantidades de ingredientes por rebanada según tamaño del pan.</p>""",
        "tiempo_preparacion": "30 minutos",
        "imagen_url": "https://i.ytimg.com/vi/2JH37P3RAFY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBQzWLjJkqWMl4tai_9LeFDXK_3Ng",
        "video_url": "https://www.youtube.com/watch?v=2JH37P3RAFY",
        "ingredientes": [
            {"nombre": "Pan de barra", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Jamón serrano", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Queso Idiazabal", "cantidad": 80, "unidad": "gr"},
            {"nombre": "Pimientos del piquillo", "cantidad": 60, "unidad": "gr"},
            {"nombre": "Aceitunas", "cantidad": 50, "unidad": "gr"},
            {"nombre": "Anchoas", "cantidad": 30, "unidad": "gr"},
            {"nombre": "Aceite de oliva", "cantidad": 30, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 3, "unidad": "gr"},
        ]
    },
    {
        "nombre": "Goxua",
        "preparacion": """<ol>
            <li><p>Prepara la crema pastelera: calienta la leche con la mitad del azúcar en un cazo hasta que humee pero sin hervir. En un bol mezcla las yemas con el resto del azúcar y la harina hasta obtener una crema homogénea. Vierte poco a poco la leche caliente sobre las yemas sin dejar de remover (temperado) y devuelve la mezcla al cazo.</p></li>
            <li><p>Cocina la crema a fuego medio-bajo removiendo continuamente hasta que espese y cubra la cuchara. Retira del fuego, añade una cucharada de mantequilla si quieres brillo y tapa con film en contacto para evitar costra. Deja enfriar.</p></li>
            <li><p>Monta la nata fría con un 10% de azúcar hasta que esté firme pero cremosa. Reserva en frío.</p></li>
            <li><p>Prepara el bizcocho: si usas bizcocho comprado córtalo a medida; si lo haces casero, hornea un bizcocho genovés y córtalo en capas finas. Opcional: remoja ligeramente el bizcocho con un almíbar ligero para aportarle humedad.</p></li>
            <li><p>Carameliza: si quieres caramelo líquido, calienta azúcar hasta obtener un caramelo dorado y viértelo sobre la base de las raciones (con cuidado). Otra opción es verter caramelo por encima al final.</p></li>
            <li><p>Montaje: coloca una base de bizcocho caramelizado, cubre con una capa generosa de crema pastelera fría y por último una capa de nata montada. Refrigera al menos 1–2 horas para que las capas se compacten.</p></li>
            <li><p>Antes de servir, decora con caramelo líquido por encima o con azúcar quemada para un acabado crujiente.</p></li>
            </ol>
            <p>Consejos: la clave está en la crema pastelera bien templada y la nata firme; monta la nata justo antes de montar el postre para que no se baje.</p>""",
        "tiempo_preparacion": "1 hora 15 minutos",
        "imagen_url": "https://imag.bonviveur.com/presentacion-final-del-goxua-vasco-detalle.jpg",
        "video_url": "https://www.youtube.com/watch?v=muO0V8PF0g8",
        "ingredientes": [
            {"nombre": "Leche", "cantidad": 500, "unidad": "ml"},
            {"nombre": "Azúcar", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Harina", "cantidad": 60, "unidad": "gr"},
            {"nombre": "Huevos", "cantidad": 4, "unidad": "unidad"},
            {"nombre": "Nata para montar", "cantidad": 200, "unidad": "ml"},
            {"nombre": "Bizcocho", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Caramelo líquido", "cantidad": 50, "unidad": "ml"},
        ]
    },
    {
        "nombre": "Txuleton a la parrilla",
        "preparacion": """<ol>
            <li><p>Saca el chuletón del frigorífico al menos 45–60 minutos antes de cocinar para que alcance temperatura ambiente. Sécalo con papel de cocina y deja la pieza entera (no cortes) para cocerla de forma uniforme.</p></li>
            <li><p>Precalienta la parrilla o la plancha a alta temperatura hasta que esté muy caliente. Si usas carbón, espera a que las brasas estén blancas y constantes.</p></li>
            <li><p>Opcional: unge ligeramente la carne con un poquito de aceite y añade sal gruesa por ambos lados justo antes de ponerla en la parrilla. La sal gruesa ayuda a crear costra.</p></li>
            <li><p>Coloca el chuletón sobre la parrilla caliente y séllalo sin moverlo 3–5 minutos por cada lado (dependiendo del grosor y del punto deseado). Para un chuletón de 3–4 cm: 3–5 min por lado para poco hecho/medio. Gira solo una vez para obtener marcas buenas.</p></li>
            <li><p>Reduce el fuego o sube la rejilla y deja que termine de cocinarse al punto deseado; usa el método del tacto o un termómetro (45–50 °C poco hecho, 52–55 °C a punto, 58–62 °C tres cuartos).</p></li>
            <li><p>Retira la carne y deja reposar 8–10 minutos cubierta con papel de aluminio suelamente para que los jugos se redistribuyan.</p></li>
            <li><p>Antes de servir, añade una pizca final de sal gruesa y pimienta recién molida. Corta en rodajas en contra de la fibra y sirve.</p></li>
            </ol>
            <p>Consejos: no pinches la carne al darle la vuelta para evitar pérdida de jugos; el reposo es clave para obtener un chuletón jugoso.</p>""",
        "tiempo_preparacion": "40 minutos",
        "imagen_url": "https://tienda.hostalrioara.com/wp-content/uploads/2020/06/chuleton-de-ternera.jpg",
        "ingredientes": [
            {"nombre": "Txuleton (chuletón)", "cantidad": 700, "unidad": "gr"},
            {"nombre": "Sal gruesa", "cantidad": 10, "unidad": "gr"},
            {"nombre": "Pimienta", "cantidad": 5, "unidad": "gr"},
            {"nombre": "Aceite de oliva", "cantidad": 20, "unidad": "ml"},
        ]
    },
    {
        "nombre": "Porrusalda",
        "preparacion": """<ol>
            <li><p>Limpia muy bien los puerros: separa la parte blanca y la parte verde clara, córtalos en rodajas diagonales y lávalos bajo agua fría para eliminar posible arena entre las capas.</p></li>
            <li><p>Pela y corta las patatas en trozos medianos y las zanahorias en rodajas o trozos uniformes.</p></li>
            <li><p>En una cazuela amplia calienta el aceite de oliva a fuego medio y añade los puerros. Pocha suavemente hasta que estén tiernos pero sin dorar (8–10 min). Añade las zanahorias y rehógalas 2–3 minutos.</p></li>
            <li><p>Incorpora las patatas, cubre con agua o caldo hasta que sobre un dedo y añade sal. Lleva a ebullición y reduce a fuego medio-bajo. Cocina unos 20–30 minutos hasta que las verduras estén tiernas.</p></li>
            <li><p>Rectifica de sal y, si quieres, añade un chorrito de aceite de oliva crudo antes de servir. Sirve caliente en plato hondo.</p></li>
            </ol>
            <p>Consejos: la porrusalda debe ser suave y con las verduras bien integradas; evita cocer a fuego muy fuerte para no deshacer completamente las patatas.</p>""",
        "tiempo_preparacion": "45 minutos",
        "imagen_url": "https://www.justspices.es/media/recipe/porrusalda.webp",
        "video_url": "https://www.youtube.com/watch?v=QWzaO4VcTOI",
        "ingredientes": [
            {"nombre": "Puerros", "cantidad": 400, "unidad": "gr"},
            {"nombre": "Patatas", "cantidad": 300, "unidad": "gr"},
            {"nombre": "Zanahorias", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Aceite de oliva", "cantidad": 50, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 7, "unidad": "gr"},
            {"nombre": "Agua", "cantidad": 1000, "unidad": "ml"},
        ]
    },
    {
        "nombre": "Txistorra al vino",
        "preparacion": """<ol>
            <li><p>Calienta una sartén amplia con un poco de aceite de oliva a fuego medio. Si las txistorras vienen en tripa natural y te preocupa que revienten, pínchalas ligeramente con un tenedor.</p></li>
            <li><p>Dora las txistorras enteras en la sartén, girándolas para que tomen color por todos sus lados. Retíralas y reserva.</p></li>
            <li><p>En la misma sartén sofríe la cebolla picada a fuego medio hasta que esté translúcida y ligeramente caramelizada (8–10 min).</p></li>
            <li><p>Vuelve a incorporar las txistorras a la sartén, vierte el vino tinto y sube un poco el fuego para que el alcohol se evapore y la salsa reduzca. Baja el fuego y cocina tapado 10–15 minutos hasta que la salsa espese ligeramente y las txistorras estén cocidas por dentro.</p></li>
            <li><p>Rectifica de sal si es necesario y sirve caliente, cortadas por la mitad o enteras, con pan para mojar la salsa.</p></li>
            </ol>
            <p>Consejos: si quieres una salsa más ligada, puedes retirar las txistorras, triturar un poco la cebolla con la reducción y devolverlas para mezclar. El vino aporta acidez; ajusta al gusto.</p>""",
        "tiempo_preparacion": "40 minutos",
        "imagen_url": "",
        "video_url": "https://www.youtube.com/watch?v=z_6HnpKzIsE",
        "ingredientes": [
            {"nombre": "Txistorra", "cantidad": 500, "unidad": "gr"},
            {"nombre": "Vino tinto", "cantidad": 300, "unidad": "ml"},
            {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Aceite de oliva", "cantidad": 40, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 5, "unidad": "gr"},
        ]
    },
    {
        "nombre": "Alubias de Tolosa",
        "preparacion": """<ol>
            <li><p>Pon las alubias en remojo la noche anterior (mínimo 8–12 horas) con agua fría, cubriéndolas ampliamente. Escurre y desecha el agua de remojo antes de cocinar.</p></li>
            <li><p>En una olla grande, pocha la cebolla picada y el pimiento verde en aceite hasta que estén tiernos. Añade los ajos machacados 1 minuto antes de incorporar las alubias.</p></li>
            <li><p>Añade las alubias escurridas a la olla y cubre con agua fría (aprox. 2–3 veces el volumen de las alubias). Añade la hoja de laurel y lleva a ebullición a fuego medio-fuerte.</p></li>
            <li><p>Cuando empiece a hervir, reduce el fuego a suave y añade el chorizo y la morcilla (enteros o en trozos, según prefieras). Cocina a fuego lento y mantenido entre 1.5 y 2 horas, controlando que las alubias no queden al descubierto y añadiendo agua caliente si es necesario.</p></li>
            <li><p>Durante la cocción, retira la espuma que pueda formarse en la superficie para obtener un caldo limpio. Ve probando la textura; las alubias están listas cuando están tiernas pero enteras.</p></li>
            <li><p>Un punto importante: no añadas sal hasta que las alubias estén casi tiernas (si añades sal al principio pueden endurecerse). Ajusta la sal al final.</p></li>
            <li><p>Cuando estén listas, deja reposar 10–15 minutos antes de servir para que el guiso asiente. Sirve caliente con trozos de chorizo y morcilla en la misma cazuela.</p></li>
            </ol>
            <p>Consejos: las alubias de Tolosa son muy agradecidas con cocción lenta; si tienes caldo de pollo o huesos, úsalo para añadir profundidad al guiso. Controla la sal teniendo en cuenta la sal de la morcilla y el chorizo.</p>""",
        "tiempo_preparacion": "2 horas",
        "imagen_url": "https://www.getariakotxakolina.eus/wp-content/uploads/2020/12/Alubias-de-Tolosa-BLOG.png",
        "video_url": "https://www.youtube.com/watch?v=TQ96ruNejeE",
        "ingredientes": [
            {"nombre": "Alubias negras", "cantidad": 500, "unidad": "gr"},
            {"nombre": "Morcilla", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Chorizo", "cantidad": 200, "unidad": "gr"},
            {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Pimiento verde", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Ajo", "cantidad": 3, "unidad": "dientes"},
            {"nombre": "Aceite de oliva", "cantidad": 60, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 8, "unidad": "gr"},
            {"nombre": "Laurel", "cantidad": 1, "unidad": "hoja"},
        ]
    },
    {
        "nombre": "Pastel vasco",
        "preparacion": """<ol>
            <li><p>Mezcla la harina, el azúcar y la levadura en un bol grande.</p></li>
            <li><p>Añade la mantequilla a temperatura ambiente y mezcla con las manos hasta obtener una textura arenosa.</p></li>
            <li><p>Incorpora los huevos uno a uno y amasa hasta conseguir una masa homogénea.</p></li>
            <li><p>Forma una bola, cúbrela con film y refrigera 30 minutos.</p></li>
            <li><p>Unta el molde con mantequilla y espolvorea harina para evitar que se pegue.</p></li>
            <li><p>Divide la masa en dos partes (una más grande que la otra). Extiende la parte mayor y cubre el fondo y los bordes del molde.</p></li>
            <li><p>Rellena con la crema pastelera de forma uniforme y cubre con la masa restante, sellando bien los bordes.</p></li>
            <li><p>Precalienta el horno a 180 °C, pinta la superficie con huevo batido y hornea 35-40 minutos hasta que esté dorado.</p></li>
            <li><p>Deja enfriar antes de desmoldar para evitar que se rompa. Sirve a temperatura ambiente o ligeramente frío.</p></li>
            </ol>""",
        "tiempo_preparacion": "1 hora 30 minutos",
        "imagen_url": "https://www.infobae.com/resizer/v2/QBYJETMIO5BDRJ246XEXHIHFL4.jpeg?auth=9e70467b34c1198fe65a73a27a7717b0c9e12f9036b50e78d93c7eca419c2147&smart=true&width=1200&height=1200&quality=85",
        "video_url": "https://www.youtube.com/watch?v=3-GbnDSZApg",
        "ingredientes": [
        {"nombre": "Harina", "cantidad": 250, "unidad": "gr"},
        {"nombre": "Azúcar", "cantidad": 150, "unidad": "gr"},
        {"nombre": "Mantequilla", "cantidad": 150, "unidad": "gr"},
        {"nombre": "Huevos", "cantidad": 3, "unidad": "unidad"},
        {"nombre": "Levadura", "cantidad": 10, "unidad": "gr"},
        {"nombre": "Crema pastelera", "cantidad": 300, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Talo con chistorra",
        "preparacion": """<ol>
            <li><p>Mezcla la harina de maíz con la sal en un bol.</p></li>
            <li><p>Añade el agua tibia poco a poco y amasa hasta que la masa sea suave y manejable.</p></li>
            <li><p>Divide la masa en bolas y aplánalas con un rodillo hasta obtener tortitas finas.</p></li>
            <li><p>Calienta una sartén o plancha y cocina cada talo 1-2 minutos por cada lado.</p></li>
            <li><p>Fríe la chistorra en otra sartén hasta que esté dorada y jugosa.</p></li>
            <li><p>Coloca la chistorra sobre los talos calientes, dobla y sirve inmediatamente.</p></li>
            </ol>""",
        "tiempo_preparacion": "25 minutos",
        "imagen_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR67mUHDbtn1Vct5Jgm3fGjxKMpRgk_NlpM2A&s",
        "video_url": "https://www.youtube.com/watch?v=mbZodZgyqQw",
        "ingredientes": [
        {"nombre": "Harina de maíz", "cantidad": 200, "unidad": "gr"},
        {"nombre": "Chistorra", "cantidad": 250, "unidad": "gr"},
        {"nombre": "Agua", "cantidad": 180, "unidad": "ml"},
        {"nombre": "Sal", "cantidad": 5, "unidad": "gr"},
        {"nombre": "Aceite para freír", "cantidad": 100, "unidad": "ml"}
        ]
    },
    {
        "nombre": "Bacalao al pil pil",
        "preparacion": """<ol>
            <li><p>Si el bacalao está en salazón, desálalo durante 24-48 horas, cambiando el agua varias veces.</p></li>
            <li><p>Calienta el aceite en una cazuela baja a fuego suave. Añade los ajos laminados y la guindilla; sofríe hasta dorar y retira.</p></li>
            <li><p>Coloca el bacalao con la piel hacia abajo en el aceite templado y cocina lentamente para que suelte su gelatina sin que hierva el aceite.</p></li>
            <li><p>Retira el bacalao y deja templar un poco el aceite. Mueve la cazuela en círculos hasta que la gelatina emulsione con el aceite formando el pil pil.</p></li>
            <li><p>Devuelve el bacalao a la cazuela y caliéntalo brevemente. Sirve decorado con los ajos y la guindilla.</p></li>
            </ol>""",
        "tiempo_preparacion": "35 minutos",
        "imagen_url": "",
        "video_url": "https://www.youtube.com/watch?v=Fyjza6ex_ao",
        "ingredientes": [
        {"nombre": "Bacalao desalado", "cantidad": 500, "unidad": "gr"},
        {"nombre": "Aceite de oliva", "cantidad": 250, "unidad": "ml"},
        {"nombre": "Ajo", "cantidad": 4, "unidad": "dientes"},
        {"nombre": "Guindilla", "cantidad": 1, "unidad": "unidad"},
        {"nombre": "Sal", "cantidad": 5, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Carrillera de cerdo",
        "preparacion": """<ol>
            <li><p>Limpia bien las carrilleras retirando el exceso de grasa.</p></li>
            <li><p>Salpimiéntalas y dóralas en una cazuela con aceite caliente para sellarlas.</p></li>
            <li><p>Retíralas y en la misma cazuela sofríe la cebolla, zanahoria y ajo picados hasta que se ablanden.</p></li>
            <li><p>Vuelve a incorporar las carrilleras y añade el vino tinto. Deja reducir el alcohol a fuego fuerte.</p></li>
            <li><p>Cubre con agua o caldo y cocina a fuego lento 1 hora y media hasta que estén tiernas.</p></li>
            <li><p>Retira las carrilleras y tritura la salsa para que quede fina.</p></li>
            <li><p>Devuelve las carrilleras a la salsa, calienta unos minutos más y sirve caliente.</p></li>
            </ol>""",
        "tiempo_preparacion": "2 horas",
        "imagen_url": "https://www.annarecetasfaciles.com/files/carrilleras-cerdo-vino-tinto-1.jpg",
        "video_url": "https://www.youtube.com/watch?v=xOxe8FJAQCo",
        "ingredientes": [
        {"nombre": "Carrilleras de cerdo", "cantidad": 600, "unidad": "gr"},
        {"nombre": "Vino tinto", "cantidad": 200, "unidad": "ml"},
        {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
        {"nombre": "Zanahoria", "cantidad": 100, "unidad": "gr"},
        {"nombre": "Ajo", "cantidad": 3, "unidad": "dientes"},
        {"nombre": "Aceite de oliva", "cantidad": 60, "unidad": "ml"},
        {"nombre": "Sal", "cantidad": 8, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Gambas a la plancha",
        "preparacion": """<ol>
            <li><p>Lava las gambas y sécalas con papel de cocina.</p></li>
            <li><p>Calienta una plancha o sartén grande a fuego fuerte.</p></li>
            <li><p>Espolvorea sal gruesa sobre la plancha y coloca las gambas.</p></li>
            <li><p>Cocina 1-2 minutos por cada lado hasta que cambien de color.</p></li>
            <li><p>Sirve inmediatamente con un chorrito de limón.</p></li>
            </ol>""",
        "tiempo_preparacion": "15 minutos",
        "imagen_url": "https://olemarisco.es/cdn/shop/articles/Gambones_a_la_Plancha_1100x.webp?v=1724148304",
        "ingredientes": [
        {"nombre": "Gambas frescas", "cantidad": 500, "unidad": "gr"},
        {"nombre": "Sal gruesa", "cantidad": 10, "unidad": "gr"},
        {"nombre": "Limón", "cantidad": 50, "unidad": "ml"}
        ]
    },
    {
        "nombre": "Mousse de queso Idiazabal",
        "preparacion": """<ol>
            <li><p>Ralla el queso Idiazabal y fúndelo a fuego suave con un poco de nata líquida.</p></li>
            <li><p>Hidrata la gelatina en agua fría y añádela a la mezcla caliente removiendo bien.</p></li>
            <li><p>Monta el resto de la nata con el azúcar hasta que esté firme.</p></li>
            <li><p>Incorpora la mezcla de queso fundido (ya templada) a la nata montada con movimientos envolventes.</p></li>
            <li><p>Reparte en moldes y refrigera al menos 3 horas para que cuaje.</p></li>
            <li><p>Sirve bien frío, decorado con frutos secos o hierbas si lo deseas.</p></li>
            </ol>""",
        "tiempo_preparacion": "3 horas",
        "imagen_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE_e0qVJ6tDjp4W9dFDHel6dnHTt0yCkZbfA&s",
        "ingredientes": [
        {"nombre": "Queso Idiazabal", "cantidad": 250, "unidad": "gr"},
        {"nombre": "Nata para montar", "cantidad": 300, "unidad": "ml"},
        {"nombre": "Azúcar", "cantidad": 50, "unidad": "gr"},
        {"nombre": "Gelatina", "cantidad": 10, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Tortilla de bacalao",
        "preparacion": """<ol>
            <li><p>Desala el bacalao si es necesario y desmígalo en trozos pequeños.</p></li>
            <li><p>Bate los huevos en un bol con una pizca de sal.</p></li>
            <li><p>Sofríe el bacalao en una sartén con un poco de aceite hasta que se vuelva blanco.</p></li>
            <li><p>Añade el bacalao a los huevos batidos junto con perejil picado.</p></li>
            <li><p>Vierte la mezcla en la sartén caliente y cuaja la tortilla a tu gusto, jugosa o más hecha.</p></li>
            <li><p>Sirve caliente.</p></li>
            </ol>""",
        "tiempo_preparacion": "30 minutos",
        "imagen_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP2MfmUHNYTUE7rHovrXAEB85zLVj26azApw&s",
        "video_url": "https://www.youtube.com/watch?v=R0gE4y8LFVA&list=PLij7F-lhbxiu2Fxs1WWgxWF8AEmcz9b_4",
        "ingredientes": [
        {"nombre": "Bacalao desalado", "cantidad": 200, "unidad": "gr"},
        {"nombre": "Huevos", "cantidad": 6, "unidad": "unidad"},
        {"nombre": "Aceite de oliva", "cantidad": 50, "unidad": "ml"},
        {"nombre": "Perejil", "cantidad": 5, "unidad": "gr"},
        {"nombre": "Sal", "cantidad": 6, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Txipirones en su tinta",
        "preparacion": """<ol>
            <li><p>Limpia bien los txipirones retirando la pluma y vísceras, reserva las bolsas de tinta.</p></li>
            <li><p>Pica la cebolla y el ajo muy finos y sofríe en aceite de oliva hasta que estén dorados.</p></li>
            <li><p>Añade los txipirones y rehoga unos minutos.</p></li>
            <li><p>Disuelve la tinta en un poco de agua caliente y añádela junto con el vino blanco.</p></li>
            <li><p>Cocina a fuego lento 20-25 minutos hasta que la salsa espese y los txipirones estén tiernos.</p></li>
            <li><p>Sirve con arroz blanco o pan para acompañar la salsa.</p></li>
            </ol>""",
        "tiempo_preparacion": "50 minutos",
        "imagen_url": "https://www.hola.com/horizon/landscape/e7b05c262f1e-chipirones-tinta-t.jpg",
        "video_url": "https://www.youtube.com/watch?v=Cd0OWoVM0Dg",
        "ingredientes": [
        {"nombre": "Txipirones", "cantidad": 500, "unidad": "gr"},
        {"nombre": "Tinta de calamar", "cantidad": 10, "unidad": "gr"},
        {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
        {"nombre": "Ajo", "cantidad": 3, "unidad": "dientes"},
        {"nombre": "Aceite de oliva", "cantidad": 60, "unidad": "ml"},
        {"nombre": "Vino blanco", "cantidad": 100, "unidad": "ml"},
        {"nombre": "Sal", "cantidad": 8, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Pochas con almejas",
        "preparacion": """<ol>
            <li><p>Lava bien las pochas frescas y déjalas en remojo en agua fría durante al menos 8 horas o toda la noche para que se hidraten.</p></li>
            <li><p>Limpia las almejas y déjalas en agua con sal durante 30 minutos para que suelten la arena. Escúrrelas bien antes de cocinarlas.</p></li>
            <li><p>Pica finamente la cebolla, el pimiento verde y los ajos.</p></li>
            <li><p>En una cazuela grande, calienta el aceite de oliva a fuego medio y sofríe la cebolla, el pimiento y el ajo hasta que estén tiernos y transparentes.</p></li>
            <li><p>Añade el tomate triturado y cocina 5-7 minutos hasta que reduzca ligeramente y concentre su sabor.</p></li>
            <li><p>Incorpora las pochas escurridas y suficiente agua para cubrirlas. Añade sal al gusto y cocina a fuego lento durante aproximadamente 1 hora, hasta que las pochas estén tiernas.</p></li>
            <li><p>Cinco minutos antes de finalizar la cocción, añade las almejas y cocina hasta que se abran. Retira cualquier almeja que no se abra.</p></li>
            <li><p>Espolvorea perejil fresco picado por encima antes de servir para aportar color y aroma.</p></li>
            </ol>""",
        "tiempo_preparacion": "1 hora 30 minutos",
        "imagen_url": "https://vod-hogarmania.atresmedia.com/hogarmania/images/images01/2016/09/14/5c000b1c5a2c1100017751dc/1239x697.jpg",
        "ingredientes": [
            {"nombre": "Pochas frescas", "cantidad": 500, "unidad": "gr"},
            {"nombre": "Almejas", "cantidad": 300, "unidad": "gr"},
            {"nombre": "Cebolla", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Pimiento verde", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Tomate triturado", "cantidad": 150, "unidad": "gr"},
            {"nombre": "Ajo", "cantidad": 3, "unidad": "dientes"},
            {"nombre": "Aceite de oliva", "cantidad": 70, "unidad": "ml"},
            {"nombre": "Sal", "cantidad": 7, "unidad": "gr"},
            {"nombre": "Perejil", "cantidad": 10, "unidad": "gr"}
        ]
    },
    {
        "nombre": "Pastel de cabracho",
        "preparacion": """<ol>
            <li><p>Cocina el cabracho limpio en agua con sal hasta que la carne esté tierna. Escúrrela y desmenúzala retirando espinas y pieles.</p></li>
            <li><p>Prepara un puré suave triturando el cabracho con la nata líquida y los huevos hasta obtener una mezcla homogénea y cremosa.</p></li>
            <li><p>Añade la mayonesa, la sal y un chorrito de limón, mezclando bien para integrar los sabores.</p></li>
            <li><p>Vierte la mezcla en un molde previamente engrasado o forrado con film transparente.</p></li>
            <li><p>Cocina al baño maría en el horno precalentado a 180 °C durante 40-50 minutos, hasta que el pastel esté firme y ligeramente dorado por encima.</p></li>
            <li><p>Deja enfriar a temperatura ambiente y luego refrigera al menos 1 hora antes de desmoldar.</p></li>
            <li><p>Sirve frío, acompañado de unas hojas de lechuga o decoración al gusto.</p></li>
            </ol>""",
        "tiempo_preparacion": "1 hora 20 minutos",
        "imagen_url": "https://cdn7.recetasdeescandalo.com/wp-content/uploads/2017/10/Pastel-de-cabracho.-Receta-asturiana.jpg",
        "video_url": "https://www.youtube.com/watch?v=HW_57Ap4d8Y",
        "ingredientes": [
            {"nombre": "Cabracho", "cantidad": 600, "unidad": "gr"},
            {"nombre": "Huevos", "cantidad": 4, "unidad": "unidad"},
            {"nombre": "Nata líquida", "cantidad": 200, "unidad": "ml"},
            {"nombre": "Mayonesa", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Sal", "cantidad": 8, "unidad": "gr"},
            {"nombre": "Limón", "cantidad": 30, "unidad": "ml"}
        ]
    },
    {
        "nombre": "Sorbete de sidra",
        "preparacion": """<ol>
            <li><p>En un cazo, calienta la sidra natural con el azúcar hasta que el azúcar se disuelva completamente, sin llegar a hervir.</p></li>
            <li><p>Deja enfriar la mezcla a temperatura ambiente y luego refrigérala durante al menos 30 minutos para que esté bien fría.</p></li>
            <li><p>Bate las claras de huevo a punto de nieve firme y añádelas suavemente a la sidra fría, mezclando con movimientos envolventes.</p></li>
            <li><p>Agrega el jugo de limón y mezcla ligeramente para integrar.</p></li>
            <li><p>Vierte la mezcla en un recipiente apto para congelador y congela durante 2-3 horas, removiendo cada 30 minutos para obtener una textura suave de sorbete.</p></li>
            <li><p>Sirve en copas frías, decorado con unas hojas de menta si deseas un toque fresco adicional.</p></li>
            </ol>""",
        "tiempo_preparacion": "15 minutos",
        "ingredientes": [
            {"nombre": "Sidra natural", "cantidad": 400, "unidad": "ml"},
            {"nombre": "Azúcar", "cantidad": 100, "unidad": "gr"},
            {"nombre": "Clara de huevo", "cantidad": 2, "unidad": "unidad"},
            {"nombre": "Limón", "cantidad": 20, "unidad": "ml"}
        ]
    }
]

recetas_objs = []
for data in recetas_data:
    imagen_url = data.get("imagen_url") or None
    video_url = data.get("video_url") or None
    receta = Receta(
        nombre=data["nombre"],
        preparacion=data["preparacion"],
        tiempo_preparacion=data["tiempo_preparacion"],
        imagen_url=imagen_url,
        video_url=video_url
    )
    for ing in data["ingredientes"]:
        receta.ingredientes.append(Ingrediente(**ing))
    recetas_objs.append(receta)

session.add_all(recetas_objs)
session.commit()

for usuario in usuarios:
    recetas_seleccionadas = random.sample(recetas_objs, k=3)
    recetas_favoritas = random.sample(recetas_objs, k=min(3, len(recetas_objs)))  
    for receta in recetas_seleccionadas:
        for ing in receta.ingredientes:
            lista_item = ListaCompra(
                usuario_id=usuario.id,
                ingrediente_nombre=ing.nombre,
                cantidad=ing.cantidad,
                unidad=ing.unidad
            )
            session.add(lista_item)
    for receta in recetas_favoritas:
        if receta not in usuario.recetas_favoritas:
            usuario.recetas_favoritas.append(receta)

session.commit()

print("Seed data creada con éxito.")
