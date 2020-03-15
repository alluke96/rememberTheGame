label inicio:
    stop sound
    stop music fadeout 1.0
    play music "music/Ambience.wav"
    #scene bgdoctor at center with Fade(1, 1, 1):
    scene bgdoctor at center with fade:
        yalign 0.7
    pause 2
    "Hum? Onde estou?"
    "Ouço o som da chuva..."
    "Por que eu não estou enxergando?"
    "Este não parece ser o meu quarto..."
    "Pensando bem... Como é meu quarto mesmo?"
    ". . ."
    "Estou confusa..."
    Doryann "Alguém acenda a luz, por favor?"
    play sound "sound/Passo.wav"
    pause 0.5
    "Espera, estou ouvindo alguém vindo."
    Karenann "Opa, veja só quem está acordando!"
    Karenann "Você ficou desacordada por algum tempo."
    Karenann "Ah, onde estão meus modos? Me chamo Karen, prazer!"
    Karen "Consegue me dizer seu nome moça?"
    Doryann "Antes de eu te dizer qualquer coisa, me responda você."
    Doryann "Por que estamos no escuro?"
    Karen "Hum? Estamos é?"
    Karen "Só um minuto."
    scene teste at center with dissolve
    pause 0.5
    scene bgdoctor at center with dissolve
    scene teste at center with dissolve
    pause 0.5
    scene bgdoctor at center with dissolve
    Karen "Parece que o acidente afetou mais coisas do que eu temia."
    Doryann "Espera, você está dizendo que eu estou..."
    Karen "Cega? Não. Pelo menos não totalmente."
    Karen "Suas pupilas dilataram um pouco quando..."
    scene bgdoctor at center with hpunch:
        yalign 0.7
    play sound "sound/Scream.mp3"
    Doryann "AAAAAAHHHHHHHHHhhhh"

    Doryann "Isso não pode estar acontecendo..."
    Doryann "Estou sonhando certo?"
    Karen "Infelizmente não."
    Karen "Estamos em um hospital."
    Karen "Você foi trazida para cá esta madrugada."
    Karen "Deu trabalho te trazer de volta à vida!"
    Doryann ". . ."
    Karen "Sinto muito."
    Karen "Você quer um abraço?"
    Karen "Você pode usar isso como uma forma de me enxergar..."
    Karen "Formando uma imagem através do tato."
    Doryann "Acho que... seria bom..."
    show Karen normal with fade:
        yalign 1.5
        xalign 0.9
    Karen "E aí? Sou parecida com o que você havia imaginado?"
    Doryann "Nem um pouco."
    Karen "Bem, agora que nos conhecemos, você consegue me dizer seu nome?"

    "Eu não me lembro de {color=#f99}NADA{/color}!"
    "O que será que eu respondo?"

# MENU DE ESCOLHA
label primeiraEscolha:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'primeiraEscolha_slow'
    show screen countdown
    menu:
        "Sim (mentir)":
            hide screen countdown
            jump primeiraEscolha_sim
        "Não":
            hide screen countdown
            jump primeiraEscolha_nao

label primeiraEscolha_slow:
    Karen "Será que o acidente afetou a sua voz também? Vamos ter que examinar mais tarde..."
    jump continuacao1

label primeiraEscolha_sim:
    $ mentiu_nome = True
    Doryann "Eu me chamo Karina."
    Karen "Hum? Seus exames mostraram uma lesão em uma certa região do cérebro..."
    Doryann "Qual região?"
    Karen "A que armazena a memória..."
    Karen "Mas você parece se lembrar muito bem!"
    Karen "Ou foi a primeira coisa que pensou quando eu disse que meu nome era Karen?"
    Doryann "Eu estou confusa... Talvez não seja, me desculpe."
    Karen "Está tudo bem, aos poucos você se lembrará."
    jump continuacao1

label primeiraEscolha_nao:
    Doryann "Eu estou confusa... não me lembro, me desculpe."
    Karen "Está tudo bem, aos poucos você se lembrará."
    jump continuacao1
#################

label continuacao1:
    Karen "Descanse um pouco agora."
    Doryann "Mas eu não quero descansar!"
    Doryann "Eu não sei nem onde estou!"
    Karen "Entendo."
    Karen "Precisamos fazer alguns procedimentos antes de te liberarmos,"
    Karen "Afinal, seu acidente foi muito feio."
    Karen "Por falar nisso... O que você lembra do acidente?"

    play music "sound/Heartbeat.wav"
    scene bgdarkroad at center with Fade(0.5, 0.5, 1.5)

    play sound "sound/Tires.wav"
    scene bgcrash1 at center with Fade(0.5, 1, 1.5):
        zoom 1.7

    scene bgcrash2 at center with Fade(0.5, 0.5, 1.5):
        zoom 1.7
    ". . ."
    "Meu carro..."
    "Essa noite..."
    "OS FREIOS!"
    play sound "sound/Ambulance.mp3"
    pause 3
    stop music fadeout 1.0
    play music "music/Ambience.wav"
    scene bgdoctor at center with pixellate:
        yalign 0.7
    show Karen pensativa:
        yalign 1.5
        xalign 0.9
    stop sound
    Karen "Garota?"
    Karen "Você estava longe..."
    show Karen normal:
        yalign 1.5
        xalign 0.9
    Karen "E aí, conseguiu se lembrar?"
    Doryann "Não.. Temo que não.. Apenas borrões..."
    Doryann "Eu vou ficar assim para sempre doutora?"
    Karen "Vamos ter que realizar um acompanhamento semanal para avaliarmos melhor sua recuperação."

    Karen "Falando nisso, você se lembra de algum familiar ou amigo?"
    Karen "Afinal precisamos avisar a alguém que você está aqui."
    Karen "Você pode usar o seu celular para tentar se lembrar de alguém."
    Karen "Encontramos ele milagrosamente intacto ao seu lado nos escombros."
### Dory pega o celular para checar os contatos
    hide Karen
    show phone at right with zoomin:
        zoom 0.7
    Doryann "..."
    Doryann "Ainda não consigo enxergar..."
    Karen "Ah sim, deixe-me dar uma olhada."
    Karen "Vamos ver, aqui nos seus contatos temos Jonas, Nicole, Yuri e Jasmine."
    Doryann "Eu não me lembro de nenhuma dessas pessoas..."
    Karen "Por que não tenta ligar para uma delas? Você pode ter sorte."
    Doryann "Boa ideia!"
    jump quemLigar

###########################################################################################################################
label continuacao2:
    Karen "Talvez você poderia tentar ligar para outra pessoa..."
    jump quemLigar
