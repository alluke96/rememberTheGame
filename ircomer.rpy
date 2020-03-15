label ircomer:
pause 1
"Ai que fome..."
"Precisava encontrar alguma coisa neste hospital para eu comer."

menu:
    "Procurar o que comer":
        "Bom, já que não me trouxeram nada, acho que o melhor a se fazer é eu ir procurar por mim mesma."
        "Se eu ir 'agarrando' a parede, talvez eu consiga..."
        "Ah, achei a porta!"
        play sound "sound/Door.wav"
        ". . ."
        "Devo estar em um tipo de corredor."
        "Nossa, esse corredor parece ser bem extenso..."
        "Hum? O que é isso?"
        "Pode ser uma máquina de salgadinhos..."
        "É SIM! E agora?"
        menu:
            "Comprar com o cartão de crédito":
                "Que droga, vou ter que apertar uns botões aleatórios aqui?"
                play sound "sound/Botao.wav"
                pause 3
                stop sound
                "Droga, não consegui."
                "De qualquer jeito, deveria me alimentar melhor..."
                #Intencional
            "Continuar procurando por outras opções":
                "Estou com MUITA fome, preciso encontrar coisas mais saudáveis."
                "Vou continuar andando."
                ". . ."
                ". . ."
                "Até agora ninguém veio me ajudar..."
                "Que lugar estranho."
                "Acho que realmente estou no fim do mundo."
                "Talvez eu devesse pedir comida para uma enfermeira."
                "Vou apertar este botão que a doutora me deu."
                ". . ."
                Dory "Por favor, enfermeira?"
                ". . ."
                "Parece que não está funcionando..."
                "Esse hospital é horrível!"
                "Por que será que me trouxeram aqui?"
                jump voltaraoquarto

    "Pedir comida para uma enfermeira":
        label enfermeira:
            "Vou apertar este botão que a doutora me deu."
            ". . ."
            Dory "Por favor, enfermeira?"
            ". . ."
            "Parece que não está funcionando..."
            "Esse hospital é horrível!"
            "Por que será que me trouxeram aqui?"
            "Bom, já que não me trouxeram nada, acho que o melhor a se fazer é eu ir procurar por mim mesma."
            "Se eu ir 'agarrando' a parede, talvez eu consiga..."
            "Ah, achei a porta!"
            play sound "sound/Door.wav"
            ". . ."
            "Devo estar em um tipo de corredor."
            "Nossa, esse corredor parece ser bem extenso..."
            "Hum? O que é isso?"
            "Pode ser uma máquina de salgadinhos..."
            "É SIM! E agora?"
            menu:
                "Comprar com o cartão de crédito":
                    "Que droga, vou ter que apertar uns botões aleatórios aqui?"
                    play sound "sound/Botao.wav"
                    pause 3
                    stop sound
                    "Droga, não consegui."
                    "De qualquer jeito, deveria me alimentar melhor..."
                    #Intencional
                "Continuar procurando por outras opções":
                    "Estou com MUITA fome, preciso encontrar coisas mais saudáveis."
                    "Vou continuar andando."
                    ". . ."
                    ". . ."
                    "Até agora ninguém veio me ajudar..."
                    "Que lugar estranho."
                    "Acho que realmente estou no fim do mundo."
                    jump voltaraoquarto
label voltaraoquarto:
"Melhor eu voltar para o meu quarto e chamar a Doutora Karen."
scene bgdoctor at center with fade:
    yalign 0.7
Dory "Doutora Karen?"
show Karen normal:
    yalign 1.5
    xalign 0.9
Karen "Sim?"
Dory "Que bom que a senhora está aqui!"
Dory "Eu estou com muita fome, andei pelo hospital inteiro e não encontrei comida."
Karen "Você andou sozinha? Ninguém nem te ajudou?"
Dory "Pois é."
Karen "Perdão! O hospital não é mais o mesmo de alguns anos atrás..."
Karen "Na época, recebíamos apoio de alguns patrocinadores."
Karen "Mas hoje em dia estamos tendo que 'nos virar' com o que temos."
Karen "Infelizmente por causa disso, muitas pessoas não resistem..."
Dory "Que horror!"
Karen "Graças a Deus, você não fez parte dessa estatística."
Karen "Já trago a sua comida."
Dory "Poxa, obrigada doutora!"
Karen "Imagina."
hide Karen
". . ."
"Patrocinadores?"
"Que tipo de hospital tem patrocinadores?"
jump jasmineliga
