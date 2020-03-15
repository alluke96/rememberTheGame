label continuacaodepoisdocelular:
    "Acho que já liguei para todo mundo..."
    pause 1
    play sound "sound/Toquedocel.wav"
    pause 1
    "O quê?"
    Dory "O que está acontecendo?"
    Karen "O Yuri está te ligando!"
    play sound "sound/Toquedocel.wav"
    pause 1
    hide phone
    show Karen normal with dissolve:
        yalign 1.5
        xalign 0.9
    Karen "Eu preciso sair por um minuto."
    Karen "Já volto!"
    Dory "Está bem..."
    hide Karen
    play sound "sound/Passo.wav"
    pause 1
    show phone at right with zoomin:
        zoom 0.7
    Dory "Alô?"
    Yuri "Eaí gata! Por que não apareceu na festa ontem à noite?"
    Dory "'Gata'?"
    Yuri "Foi mal... Esqueço que você não curte."
    Yuri "E aí, tá fazendo o quê?"

    # MENU DE ESCOLHA
    label Yuriliga:
        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'yuriliga_slow'
        show screen countdown
        menu:
            "Para sua informação, estou em um hospital":
                hide screen countdown
                jump yuriliga1
            "Te conheço de onde mesmo?":
                hide screen countdown
                jump yuriliga1

    label yuriliga_slow: #nao respondeu
        Yuri "Qual foi 'gata'? O gato comeu sua língua?"
        jump Yuriliga

    label yuriliga1: # pra sua informacao
        Yuri "Hum? Bebeu demais foi?"
        if lembra_quebebe == False:
            Dory "Eu bebo?"
            scene eubebo at center with fade:
                zoom 3
            play sound "sound/Cheer.wav"
            ""
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
                    jump contyuriligando
                "Não... (mentir)":
                    Karen "Entendo..."
                    Karen "Se lembrar de alguma coisa que eu precise saber, estarei aqui."
                    jump contyuriligando
        label contyuriligando:
            hide Karen
            show phone at right with zoomin:
                zoom 0.7
            Dory "Não me venha com essa história novamente!"
            Dory "Eu nunca mais beberei."
            Yuri "De novo com essa frase, Dory?"
            Yuri "A gente já conversou muito sobre isso..."
            Yuri "Você só promete, promete e nunca cumpre."
            Dory "Dessa vez é diferente."
            Dory "Sofri um acidente, sabia?"
            Yuri "Cuidado bebê, bebida e direção não combinam."
            Dory "Como é?"
            Dory "Eu nunca disse que meu acidente foi de carro."
            Yuri "Ah, se liga né gatinha."
            Yuri "Tu sempre bebe e sai por aí dando risada com seu carro."
            Yuri "Não foi difícil assimilar as coisas."
            Dory "Não lembrava disso..."
            Yuri "É sério? Como foi o acidente então?"
            Yuri "Agora tu me deixou curioso."
            Dory "Eu não... me lembro direito."

            Dory "Mas me diga:"
            menu:
                "Por quê deu uma festa?":
                    Yuri "Eu ia ficar chateado por você não se lembrar..."
                    Yuri "Mas parece que você esqueceu até de nós..."
                    Dory "Como assim nós?"
                    Yuri "Poxa bebê, assim você me machuca."
                    Dory "Mas e o Jonas?"
                    Dory "Eu achava que ele era meu namorado!"
                "Você não sabe que tenho namorado?":
                    Dory "Afinal você fica me chamando de 'gatinha' e 'bebê'"
                    Dory "Por acaso você não conhece o Jonas?"
            Yuri "AHAHAHAHAHAHAHA!"
            Dory "Está rindo do quê?"
            Yuri "Você considera aquele magrelo como sendo seu 'namorado'?"
            Yuri "Acorda Dory!"
            Yuri "O que fazemos é muito melhor, não acha?"
            Dory "Só pelo jeito de você falar, eu não acho."
            Yuri "Não foi isso que você me disse segunda-feira."
            menu:
                "Mas afinal, por quê deu uma festa?":
                    Yuri "Oras, eu ia te anunciar como minha namorada!"
                    Yuri "A gente que planejou tudo."
                "O que eu disse segunda-feira?":
                    Yuri "Que me amava e queria ficar comigo, oras!"
                    Yuri "A gente tinha até planejado essa festa juntos!"
                    Yuri "Eu ia te anunciar como minha namorada!"
            Yuri "Você disse para o Jonas que ia {color=#f99}dormir na casa da Jasmine{/color}..."
            Yuri "Enquanto isso estava vindo para cá."
            Yuri "Te esperamos a noite toda."
            Yuri "Como você não veio, a Jasmine ficava 'dando em cima' de mim."
            Yuri "Mas relaxa gata, só tenho olhos pra você!"

            "Não sei se acredito em uma palavra sequer do que este rapaz me diz."
            Dory "Olha, agora eu tenho que desligar."
            Dory "Estão me chamando para fazer alguns exames aqui."
            Yuri "Ah sim, claro."
            Yuri "Fique à vontade, {color=#f99}te amo{/color}!"
            Dory ". . ."
            Dory "Tchau!"
            play sound "sound/Phoneend.wav"
        hide phone
        pause 2
        ". . ."
        "É amedrontador ficar aqui sozinha..."
        "Pensando bem, vai ser sempre assim..."
        "No escuro..."
        "Ai Deus, faça isso ser temporário...Por favor!"
        "Pelo menos agora que a Doutora se foi eu consigo pôr a cabeça no lugar."
        "Vamos lá..."
        "Pelo que eu entendi o Jonas é meu namorado."
        "Ou será que estou enganada e eu sou mesmo infiel?"
        "Seja como for, não gosto como este tal de Yuri fala comigo."
        "Pelo menos o meu 'novo eu' não gosta..."
        "Será que eu sou uma bêbada mesmo?"
        "E onde foi parar a ligação do Jonas?"
        "Ele disse que ia procurar onde fica o hospital e até agora não retornou a ligação!"
        "Isso não pode demorar tanto assim..."
        "Tantas perguntas..."
        "Tomara que eu não acabe enlouquecendo."
        "Era só o que me faltava..."
        "Uma cega louca."
        "Esse é o fim que eu mereço?"
        pause 2
        "Esse perfume é familiar."
        pause 1
        show Karen normal:
            yalign 1.5
            xalign 0.9
        Karen "Olá moça."
        Dory "Oi."
        Karen "Conseguiu se lembrar do seu nome?"
        Dory "Sim, me chamo Dory."
        Karen "Ah, prazer Dory!"
        if mentiu_nome == True:
            Karen "Parece que {color=#f99}Karina{/color} foi apenas um reflexo da sua mente então, não é?"
            Dory "Pois é, me desculpe novamente."
            Karen "Não se preocupe, nas suas condições isso é perfeitamente plausível."
        Karen "Se precisar de alguma coisa, vou te dar este controle."
        Karen "Ele é pequeno e tem só um botão."
        Karen "Você aperta ele e uma enfermeira vem lhe ajudar."
        Dory "Ok, obrigada."
        Karen "De nada. Até mais."
        play sound "sound/Passo.wav"
        hide Karen

        jump retornonicole
