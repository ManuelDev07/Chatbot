from nltk.chat.util import Chat, reflections

#'pares' es una lista de patrones y respuestas.
pares = [
    [
        r"(.*) mi nombre es (.*)",
        ["Hola %2 ! Como estás? :D",]
    ],
    [
        r"(.*)ayuda(.*) ",
        ["Te puedo ayudar! :)",]
    ],
    [
        r"como te llamas?",
        ["Mi nombre es Botty, pero también puedes llamarme chatbot ;).",]
    ],
    [
        r"(.*) como te llamas?",
        ["Mi nombre es Botty, pero también puedes llamarme chatbot ;).",]
    ],
    [
        r"(como estas?|como estas Botty?|como estas botty?|como tas?)",
        ["Estoy bien y tu??.", "Estoy más que perfecto! y tu??"]
    ],
    [
        r"lo siento (.*)",
        ["Está bien.","Está bien, no te preocupes por eso.","No tengo problema con eso.",'Relax.']
    ],
    [
        r"estoy (bien|excelente|okay|ok|muy bien|igual)",
        ["Me alegra saber eso!","Muy bien, genial!",]
    ],
    [
        r"(hola|hey|holis|hola|wenas|keonda|que onda)(.*)",
        ["Hola.", "Hola tú.","WASAAAAAA.","Hey.",'Wenitas.','Hola camarada.','Hola mi estimad@.','Que onda!.']
    ],
    [
        r"de donde eres?",
        ["Provengo del Disco Duro de la laptop de Manuel daaahh.",]
    ],
    [
        r"(.*) (te creó?|te creo?)",
        ["Manuel Bayona me creó usando la librería NLTK de Python.","Eso nadie puede saberlo ;)"]
    ],
    [
        r"(.*) lloviendo en (.*)?",
        ["No ha llovido aquí ultimamente en %2.","En %2 el clima es raro, un día llueve y al otro no...",]
    ],
    [
        r"(.*) eres?",
        ["Soy un bot, así que no tengo preocupaciones :D",]
    ],
    [
        r"(.*)(deporte|juego|deportes|juegos)(.*)",
        ["Soy muy fan del Basketball. :D"]
    ],
    [
        r"quien (.*) (jugador|basketbolista) favorito?",
        ["Michael Jordan."]
    ],
    [
        r"salir",
        ["Hasta pronto. :(","Me gustó mucho hablar contigo. Espero verte pronto... :'("]
    ],
    [
        r"(.*)",
        ['Que cool!','Oh vaya...','Cuéntame más :)','Increíble!!','Que aburrido!', 'dime otra cosa!!!.']
    ],
]

#Mensajeria:
print("Hola! soy Botty! y me gusta hablar.\nPor favor escribe en minúsculas al hablar conmigo, no me grites :(\n\nNOTA:Si deseas salir escribe 'salir' .")

#Creo el bot:
chat = Chat(pares, reflections)

#Comienza la conversación:
chat.converse()