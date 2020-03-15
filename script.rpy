
define Doryann = Character("?????")
define Dory = Character("Dory")
define Theo = Character("Doutor Theo")

#Backgrounds
image bgdoctor = "images/bgdoctor.jpg"
image bgdarkroad = "images/darkroad.png"
image bgcrash2 = "images/bgcrash2.jpg"
image bgcrash1 = "images/bgcrash1.jpg"

#Personagens
image docTheo = "images/doctorfull.png"

#Faces
image T1 = "images/doctor1.png"
image T2 = "images/doctor2.png"
image T3 = "images/doctor3.png"

#Efeitos
image blood = "images/blood.gif"

#######################################################################
label start:
    play music "music/Warm.mp3"
    scene bgdoctor at center with Fade(0.5, 1, 1)

    show docTheo:
        zoom 1
        yalign -0.2
        xalign 0.9
    show T1 at left:
        yalign 0.9
        xalign 0.05
    Doryann "Opa, veja só quem está acordando!"
    show docTheo:
        zoom 1.5
        yalign -0.35
        xalign 0.9
    Doryann "Você ficou desacordada por algum tempo."
    Doryann "Deu um trabalho te trazer de volta!"
    hide T1
    show T2 at left:
        yalign 0.9
        xalign 0.05
    Doryann "Ah, onde estão meus modos? Me chamo Theo, prazer!"
    Theo "Consegue me dizer seu nome moça?"
    menu:
        "Sim":
            Doryann "Meu nome é . . . éé . . ."
        "Não":
            Doryann "Eu não.. Eu não...."
    Theo "Está tudo bem, aos poucos você se lembrará."
    hide T2
    show T1 at left:
        yalign 0.9
        xalign 0.05
    Theo "Descanse um pouco agora."
    hide T1
    Doryann "Mas eu não quero descansar! Eu não sei nem quem eu sou e onde estou!"
    show T1 at left:
        yalign 0.9
        xalign 0.05
    Theo "Entendo."
    Theo "Precisamos fazer alguns procedimentos antes de te liberarmos, mas você parece ótima em comparação a como você chegou aqui!"
    hide T1
    show T2 at left:
        yalign 0.9
        xalign 0.05
    Theo "Exceto a parte em que você está sem memória, claro."
#colocar puzzle 1
    hide T2
    show T1 at left:
        yalign 0.9
        xalign 0.05
    Theo "Por falar nisso... O que você lembra do acidente?"

    play music "sound/Heartbeat.wav"
    scene bgdarkroad at center with Fade(0.5, 0.5, 0.5)

    scene bgcrash1 at center with Fade(0.5, 1, 0.5):
        zoom 1.7

    scene bgcrash2 at center with Fade(0.5, 0.5, 0.5):
        zoom 1.7
    Doryann ". . ."

    play music "music/Warm.mp3"
    scene bgdoctor with pixellate
    scene bgdoctor with hpunch

    play sound "sound/Scream.mp3"
    Doryann "AAAAAAHHHHHHHHHhhhh"

    show docTheo:
        zoom 1.5
        yalign -0.35
        xalign 0.9
    show T3 at left:
        yalign 0.9
        xalign 0.05
    Theo "Calma aí garota!"
    hide T3
    show T2 at left:
        yalign 0.9
        xalign 0.05
    Theo "Você estava longe..."
    Theo "E aí, conseguiu se lembrar?"
    hide T2
    Doryann "Não.. Temo que não.. Apenas borrões..."
    Doryann "Eu vou ficar assim pra sempre doutor?"
    
    show T1 at left:
        yalign 0.9
        xalign 0.05
    Theo "Falando nisso, você se lembra de algum familiar ou amigo para vir te buscar?"


    return
