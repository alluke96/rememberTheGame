# MENU DE ESCOLHA (sem timer)
if menu_completo == False:
    label quemLigar:
        menu:
            "Jonas":
                hide screen countdown
                if jonas == True:
                    jump quemLigar_jonas
                "Já liguei para ele"
            "Nicole":
                hide screen countdown
                if nicole == True:
                    jump quemLigar_nicole
                "Já liguei para ela"
            "Yuri":
                hide screen countdown
                if yuri == True:
                    jump quemLigar_yuri
                "Já liguei para ele"
            "Jasmine":
                hide screen countdown
                if jasmine == True:
                    jump quemLigar_jasmine
                "Já liguei para ela"

    if (jonas == False and nicole == False and jasmine == False and yuri == False):
        $ menu_completo = True
        jump continuacaodepoisdocelular

    jump quemLigar
###########################################################################################################################
label quemLigar_jonas:
    play sound "sound/Phonering.wav"
    ". . ."
    play sound "sound/Phonering.wav"
    ". . ."
    #play sound "sound/answeringphone"
    Jonas "Alô? Amor?"
    if nome_conhece == False:
        Doryann "'Amor'?"
    else:
        Dory "'Amor'?"
    Jonas "Nossa você sumiu, me deixou preocupado!"
    Jonas "Foi tão bom assim {color=#f99}dormir na casa da Jasmine{/color}?"
    Jonas "Até me esqueceu?"
    if nome_conhece == False:
        Doryann ". . ."
        Jonas "{color=#f00}Dory{/color}, você está bem?"
        Dory "'Dory'?"
        Jonas "Você está muito estranha hoje meu amor..."
    if nome_conhece == True:
        Dory ". . ."
        Jonas "Dory, você está bem?"
    # MENU DE ESCOLHA
    label convJonas:
        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'jonas_slow'
        show screen countdown
        menu:
            "Desculpa mas, de onde a gente se conhece mesmo?":
                hide screen countdown
                jump jon1
            "Não, eu não estou nada bem":
                hide screen countdown
                jump jon1
    label jonas_slow:
        Jonas "Você está aí meu bem?"
        jump convJonas
    label jon1:
        Jonas "Você está me assustando, vida."
        Jonas "Aconteceu alguma coisa?"
        Dory "Olha, eu gostaria de estar brincando, mas estou em um hospital não faço a menor ideia de quem você é!"
        Jonas "Dory, me responda uma coisa:"
        Jonas "Você bebeu novamente?"
        $ lembra_quebebe = True
        Dory "Eu bebo?"
        scene eubebo at center with fade:
            zoom 3
        play sound "sound/Cheer.wav"
        pause 2
        scene bgdoctor at center with fade:
            yalign 0.7
        show Karen normal:
            yalign 1.5
            xalign 0.9
        Karen "Huum?"
        Karen "Você estava longe novamente... Lembrou de algo?"
        menu:
            "Lembrei que bebo":
                Karen "Entendo..."
                Karen "Vou adicionar esta informação ao seu prontuário."
                $ contou_quebebe = True
                jump jonascont
            "Não... (mentir)":
                Karen "Entendo..."
                Karen "Se lembrar de alguma coisa que eu precise saber, estarei aqui."
                jump jonascont
    label jonascont:
        hide Karen
        show phone at right with zoomin:
            zoom 0.7
        Jonas "Dory?"
        Dory "Desculpe 'amor', estava falando com a médica que me socorreu."
        Dory "Sua resposta sobre eu ter bebido é: talvez!"
        Dory "Sofri um acidente ontem a noite e agora estou no hospital."
        Dory "Como consequência deste acidente eu não me lembro de nada!"
        Jonas "Conheço você há 3 anos."
        Jonas "Sei que está falando a verdade."
        Jonas "Qual hospital você está?"
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
        Jonas "Não conheço este hospital..."
        Jonas "Vou procurar onde fica e já te retorno."
        $ FINAL_jonasvindo = True
        Dory "Ok."
        Jonas "Beijos amor, descanse."
        Dory "Está bem..."
        Dory "Tchau!"
        Jonas "Tchau."
        play sound "sound/Phoneend.wav"
    $ jonas = False
    pause 0.5
    jump quemLigar

###########################################################################################################################
label quemLigar_nicole:
    play sound "sound/Phonering.wav"
    ". . ."
    #play sound "sound/answeringphone"
    Nicole "{color=#f00}DORY{/color}! ONDE VOCÊ SE METEU MENINA?"
    $ nome_conhece = True
    Dory ". . ."
    Nicole "DORY, ME RESPONDA AGORA MOCINHA!"
    # MENU DE ESCOLHA
    label convNicole:
        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'nic_slow'
        show screen countdown
        menu:
            "Desculpa mas, de onde a gente se conhece mesmo?":
                hide screen countdown
                jump nic1
            "Dá para parar de gritar?":
                hide screen countdown
                jump nic2

    label nic_slow: #nao respondeu
        Nicole "Tem alguém aí?"
        jump convNicole

    label nic1: # desculpa
        Nicole "Que brincadeira é essa garota? ONDE VOCÊ ESTÁ HEIN?"
        Dory "Olha, eu gostaria de estar brincando, mas estou em um hospital não faço a menor ideia de quem você é!"
        Nicole "{color=#f99}Filha{/color}, isso é sério?"
        Dory "'Filha'?"
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
        Nicole "Sim, verdade, me desculpe."
        Dory "Só sei que me envolvi em um acidente."
        Nicole "Estou indo para aí, me aguarde."
        Nicole "Até o anoitecer eu chego."
        Dory "Ok."
        Nicole "Te amo filha, espero que não seja alguma pegadinha."
        Nicole "Você pode até ter esquecido, mas eu não esqueci das coisas que você aprontou!"
        Dory "Credo! É verdade, eu juro!"
        Nicole "Veremos."
        Dory ". . ."
        play sound "sound/Phoneend.wav"
        $ FINAL_maevindo = True
        $ nicole = False
        pause 0.5
        jump continuacao2

    label nic2: # para de gritar
        Nicole "O QUÊÊÊ???"
        Nicole "VOLTE AGORA PRA CASA, TEMOS QUE CONVERSAR!"
        Dory "Mas..."
        play sound "sound/Phoneend.wav"
        Dory ". . ."

        $ nicole = False
        pause 0.5
        jump continuacao2

###########################################################################################################################
label quemLigar_yuri:
    play sound phonering
    pause 1
    play sound phonering
    pause 1.5
    play sound "sound/Busy.wav"
    pause 0.5
    if nome_conhece == False:
        Doryann "Ninguém atende..."
    if nome_conhece == True:
        Dory "Ninguém atende..."
    $ yuri = False
    pause 0.5
    jump continuacao2

###########################################################################################################################
label quemLigar_jasmine:
    play sound "sound/Phonering.wav"
    ". . ."
    #play sound "sound/answeringphone"
    Jasmine "AMIGAAAAAAA!!!"
    if nome_conhece == False:
        Doryann "Olá?!"
        Jasmine "O QUE ACONTECEU COM VOCÊ SUMIDA?"
        Jasmine "Todo mundo ficou te esperando na {color=#f99}festa do Yuri{/color} e você não apareceu!"
        Jasmine "Poxa amiga, que mancada..."
        Doryann ". . ."
        Jasmine "Aconteceu alguma coisa, amiga?"
        Doryann "Desculpa mas, de onde a gente se conhece mesmo?"
        Jasmine "O QUÊÊÊ???"
        Doryann "É que minha cabeça está um pouco confusa..."
        Doryann "Eu acordei em um hospital e não lembro nem quem eu sou direito!"
        Jasmine "Espera, isso é sério?"
        Doryann "Infelizmente sim."
        Jasmine "{color=#f00}Dory{/color}, você realmente não tá zuando com a minha cara né?"
        $ nome_conhece = True
        Dory "'Dory'?"
    if nome_conhece == True:
        Dory "Olá?!"
        Jasmine "O QUE ACONTECEU COM VOCÊ SUMIDA?"
        Jasmine "Todo mundo ficou te esperando na {color=#f99}festa do Yuri{/color} e você não apareceu!"
        Jasmine "Poxa amiga, que mancada..."
        Dory ". . ."
        Jasmine "Aconteceu alguma coisa, amiga?"
        Dory "Desculpa mas, de onde a gente se conhece mesmo?"
        Jasmine "O QUÊÊÊ???"
        Dory "É que minha cabeça tá um pouco confusa..."
        Dory "Eu acordei em um hospital e não lembro nem quem eu sou direito!"
        Jasmine "Espera, isso é sério?"
        Dory "Infelizmente sim."
        Jasmine "Dory, você realmente não tá zuando com a minha cara né?"
        Dory "Gostaria de estar, 'amiga'."

    Jasmine "Meu Deus!"
    Jasmine "Tadinha da minha amiga!"
    Jasmine "Você tá bem?"
    Jasmine "Já ligou pra sua mãe?"
    Jasmine "Você quer que eu vá te buscar?"
    # MENU DE ESCOLHA
    label convJasmine:
        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'jas_slow'
        show screen countdown
        menu:
            "Gostaria":
                hide screen countdown
                jump jas1
            "Por quê tantas perguntas?":
                hide screen countdown
                jump jas2

    label jas_slow: #nao respondeu
        Jasmine "Desculpa amiga, como sempre eu fiz perguntas demais né?"
        Jasmine "Tô tentando melhorar... Mas me responde só essa por favor?"
        Jasmine "Você quer que eu vá te buscar?"
        jump convJasmine

    label jas1: # gostaria
        Jasmine "Está bem amiga."
        Jasmine "Chegando aí a gente conversa, ok?"
        Dory "Ok."
        Jasmine "Se cuida."
        play sound "sound/Phoneend.wav"
        $ FINAL_jasminevindo = True
        $ jasmine = False
        jump continuacao2

    label jas2: # por que tanta pergunta
        Jasmine "Credo amiga, só tô preocupada contigo!"
        Jasmine "Só porquê você se esqueceu de mim, não quer dizer que tem que ser uma babaca!"
        Dory "Mas..."
        Jasmine "Eu sei que você deve estar bem confusa, no seu lugar eu estaria pirando."
        Jasmine "Mas não precisa falar assim com a sua MELHOR amiga!"
        Dory "Somos melhores amigas?"
        Jasmine "Não sei se tá zuando ou tá falando sério ainda..."
        Jasmine "Lembra daquela vez que a Leticia estava praticando bullying contigo na aula de Francês?"
        Jasmine "Não lembra que fui eu que te defendi?"
        Dory "Não faço a menor ideia de quem seja Leticia."
        Dory "O contato dela nem estava no meu celular."
        Jasmine "Claro né amiga, ela sumiu depois que nos formamos."
        Jasmine "Fora que ela sempre foi uma otária."
        Jasmine "Mas enfim..."
        Dory "Bom, acho que seria bom você vir aqui então..."
        Jasmine "Ótimo, estou saindo daqui."
        Jasmine "A propósito, pra qual hospital você foi mesmo?"
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
        Jasmine "Nossa que longe!"
        Jasmine "Vai demorar um pouco pra chegar aí..."
        Jasmine "Me aguarde ok?"
        Dory "Ok."
        Jasmine "Se cuida."
        play sound "sound/Phoneend.wav"
        $ FINAL_jasminevindo = True
        $ jasmine = False
        pause 0.5
        jump continuacao2
