label retornonicole:
    play sound "sound/Toquedocel.wav"
    "Hum?"
    show phone at right with zoomin:
        zoom 0.7
    "Quem será?"
    play sound "sound/Toquedocel.wav"
    ". . ."
    menu:
        "Deixar tocar":
            hide phone
            show Karen normal:
                yalign 1.5
                xalign 0.9
            Karen "Ei!"
            Dory "Que susto doutora, ainda está aí?"
            Karen "Ah, me desculpe..."
            play sound "sound/Toquedocel.wav"
            Karen "Seu celular está tocando!"
            Dory "É, eu sei."
            Karen "Não vai atender?"
            Dory "Acho que não."
            play sound "sound/Toquedocel.wav"
            Karen "Mas você não precisava se lembrar das pessoas?"
            Karen "Creio que isso ajude na sua recuperação."
            Dory "Talvez você tenha razão..."
            Dory "Obrigada doutora."
            hide Karen
            jump atendernicole
        "Atender":
            label atendernicole:
            show phone at right with zoomin:
                zoom 0.7
            if FINAL_maevindo == False:
                Nicole "Alô?"
                Dory "Oi..."
                Nicole "Oi {color=#f99}filha{/color}."
                Nicole "Desculpa ter desligado na sua cara antes."
                Dory "'Filha'?"
                Nicole "Sim garota, eu ligo para pedir desculpas e você se finge de surda?"
                Dory ". . ."
                Nicole "Que brincadeira é essa garota? Onde você tá hein?"
                Dory "Olha, eu gostaria de estar brincando, mas estou em um hospital não faço a menor ideia de quem você é!"
                Nicole "Se isso é realmente verdade, para qual hospital você foi?"
                if hospital_conhece == False:
                    Dory "Deixa eu perguntar."
                    hide phone
                    show Karen normal:
                        yalign 1.5
                        xalign 0.9
                    Dory "Com licença, doutora?"
                    Karen "Sim?"
                    Dory "Em qual hospital estamos?"
                    hide Karen
                    show Karen olhofechado:
                        yalign 1.5
                        xalign 0.9
                    $ hospital_conhece = True
                    Karen "Estamos no Saint Peterson."
                    Dory "Obrigada!"
                    hide Karen
                    show phone at right with zoomin:
                        zoom 0.7
                Dory "Estou no Saint Peterson."
                Nicole "Nossa, faz tempo que não ouço falar neste nome..."
                Nicole "Fora que fica longe daqui de casa."
                Nicole "O que você estava fazendo filha?"
                Dory "Como disse, eu não lembro..."
                Dory "Só sei que me envolvi em um acidente."
                Nicole "Sim, verdade, me desculpe."
                Nicole "Estou indo para aí, me aguarde."
                Nicole "Até o anoitecer eu chego."
                Dory "Ok."
                Nicole "Te amo filha, espero que não seja alguma pegadinha."
                Nicole "Você pode até ter esquecido, mas eu não esqueci das coisas que você aprontou!"
                Dory "Credo! É verdade, eu juro!"
                Nicole "Veremos."
                Dory ". . ."
                $ FINAL_maevindo = True
                Nicole "Você já comeu?"
                Dory "Ainda não mãe."
                Nicole "Está sendo bem tratada?"
                Dory "Sim."
                Nicole "Está precisando de dinheiro?"
                Nicole "Qualquer coisa pode usar o seu cartão de crédito."
                Nicole "Eu aumentei um pouco o limite dele para você."
                Dory ". . ."
                Dory "Mãe, me diga uma coisa,"
                Dory "O quão 'ricos' nós somos?"
                Nicole "Certo, vou ter que me acostumar com essa história de perda de memória."
                Nicole "Assim filha, desde que seu pai morreu..."
                Dory "MEU PAI MORREU?"
                Nicole "Ah... Sim... Já se fazem alguns anos... O tempo passa né..."
                Dory ". . ."
                jump pergnicole

            if FINAL_maevindo == True:
                Nicole "Alô, filha?"
                Dory "Oi mãe."
                Nicole "Você já comeu?"
                Dory "Ainda não mãe."
                Nicole "Está sendo bem tratada?"
                Dory "Sim."
                Nicole "Está precisando de dinheiro?"
                Nicole "Qualquer coisa pode usar o seu cartão de crédito."
                Nicole "Eu aumentei um pouco o limite dele para você."
                Dory ". . ."
                Dory "Mãe, me diga uma coisa,"
                Dory "O quão 'ricos' nós somos?"
                Nicole "Certo, vou ter que me acostumar com essa história de perda de memória."
                Nicole "Assim filha, desde que seu pai morreu..."
                Dory "MEU PAI MORREU?"
                Nicole "Ah... Sim... Já se fazem alguns anos... O tempo passa né..."
                Dory ". . ."
                jump pergnicole
                
            label pergnicole:
                if opc1 == False or opc2 == False:
                    menu:
                        "Como meu pai era?" if opc1 == False:
                            Nicole "Ele foi um bom homem..."
                            Nicole "Um bom pai..."
                            Nicole "Um bom marido..."
                            Nicole "Nunca deixou que faltasse nada para nós..."
                            Nicole "Vocês eram bem apegados."
                            Dory "E como ele era? Digo, fisicamente falando."
                            Nicole "Gordo, muita bebida coitado..."
                            Nicole "Era careca e usava um bigode que eu sempre pedi para ele tirar..."
                            Dory "Você parece que gostava muito dele..."
                            Dory "Me inveja de certa forma por não lembrar disso."
                            Nicole "Você era apenas um bebê quando ele se foi."
                            Dory "Se não for perguntar muito, como foi que ele morreu?"
                            Nicole "Acidente de avião."
                            Nicole "Ele era piloto de jatinhos particulares... E bebeu muito naquele dia."
                            Dory "Nossa!"
                            Nicole "Pois é..."
                            $ opc1 = True
                            jump pergnicole
                        "E então, somos ricos?" if opc2 == False:
                            Nicole "Pode se dizer que sim."
                            Nicole "A fortuna que seu pai fez acabou ficando para nós."
                            Nicole "O coitado nem teve tempo para desfrutá-la."
                            Nicole "'Quando eu me aposentar eu aproveito'- dizia ele."
                            Dory "Entendi..."
                            $ opc2 = True
                            jump pergnicole

                    if opc1 == True and opc2 == True:
                        jump nicolefim

label nicolefim:
    Dory "Mãe, agora eu vou comer alguma coisa."
    Nicole "Está bem filha, fique bem."
    Dory "Beijos, tchau!"
    Nicole "Te amo filha, me aguarde."
    play sound "sound/Phoneend.wav"
    hide phone
    jump ircomer
