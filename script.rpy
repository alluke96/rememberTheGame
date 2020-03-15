#Personagens
define Doryann = Character("?????")
define Karenann = Character("?????", color="#009900")
define Dory = Character("Dory")
define Karen = Character("Karen", color="#009900")
define Yuri = Character("Yuri", color="#123456")
define Nicole = Character("Nicole", color="#202099")
define Jonas = Character("Jonas", color="#987654")
define Jasmine = Character("Jasmine", color="#999900")
define Tuto = Character("NOME AQUI", color="#FF00FF")
define Y = Character ("???", color="#FF00FF")

image Karen normal = "images/Karen.png"
image Karen olhofechado = "images/Karen2.png"
image Karen pensativa = "images/Karen3.png"
image Karen determinada = "images/Karen4.png"
image Yuri = "images/yuri.png"

#Backgrounds
image bgdoctor = "images/bgdoctor.jpg"
image bgdarkroad = "images/darkroad.png"
image bgcrash2 = "images/bgcrash2.jpg"
image bgcrash1 = "images/bgcrash1.jpg"
image phone = "images/phone.png"
image eubebo = "images/eubebo.jpg"

#Sons Recorrentes
define audio.phonering = "sound/Phonering.wav"

#Variaveis
define jasmine = True
define jonas = True
define nicole = True
define yuri = True

define opc1 = False
define opc2 = False

define menu_completo = False

#Lembrancas
define nome_conhece = False
define hospital_conhece = False
define lembra_quebebe = False

#Mentiras
define mentiu_nome = False
define contou_quebebe = False

#Finais
define FINAL_maevindo = False
define FINAL_jasvindo = False
define FINAL_jonasvindo = False

define FINAL_yuritemata = False
define FINAL_yuriepreso= False

#Faces
# image side T1 = "images/doctor1.png"
# image side T2 = "images/doctor2.png"
# image side T3 = "images/doctor3.png"

#Efeitos
image blood = "images/blood.gif"

#########################################
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

# time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out
#######################################################################

label start:
    stop sound
    stop music fadeout 1.0
    scene teste at center with fade
    "Bem vindos à minha história interativa!"
    "Apenas um rápido esclarecimento:"
    "Quando um personagem estiver {color=#f99}FALANDO{/color},"
    "O nome dele aparecerá no canto superior esquerdo."
    play sound "sound/Wow.mp3"
    Tuto "Assim!"
    "Quando a personagem principal estiver {color=#f99}PENSANDO{/color},"
    "Nenhum nome aparecerá!"
    "A personagem principal(você) tem o nome em {color=#ff0000}VERMELHO{/color}"
    "Ah, fique atento às escolhas ao redor do jogo!"
    menu:
        "Como essa por exemplo!":
            play sound "sound/Goodjob.mp3"
        "Ou essa!":
            play sound "sound/Goodjob.mp3"
    "Muito bem!"
    "Algumas terão de ser respondidas rapidamente!"
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'tuto_slow'
    show screen countdown
    menu:
        "Ok!":
            hide screen countdown
            jump t2
    label tuto_slow:
        "Neste caso você não respondeu a tempo!"

    label t2:
    "Bom, era isso!"
    "Boa leitura! ;3"
    jump inicio
