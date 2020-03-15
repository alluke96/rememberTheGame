label contfinal:
    play sound "sound/Toquedocel.wav"
    ". . ."
    show phone at right with zoomin:
        zoom 0.7
    "A doutora não está aqui..."
    "Será que eu atendo?"
    play sound "sound/Toquedocel.wav"
    ". . ."
    Dory "Alô?"
    Nicole "Oi filha."
    Dory "Ah, oi mãe!"
    Nicole "Nossa, você está ofegante!"
    Nicole "Aconteceu alguma coisa?"
    Dory "Nada não, mãe."
    Nicole "Filha, você não vai gostar do que eu vou te falar."
    Dory "Hum?"
    Nicole "Tem uma árvore caída na estrada por causa da chuva."
    Nicole "Não vou conseguir chegar aí tão cedo!"
    Nicole "Amanhã eu vou, ok?"
    Dory ". . ."
    Nicole "Filha?"
    Dory "Está bem."
    Nicole "Mil perdões..."
    Dory "Imagina, a culpa não é sua!"
    Nicole "Mesmo assim..."
    Nicole "Depois, se você ainda estiver acordada, eu te ligo."
    Nicole "Te amo, tchau!"
    Dory "Tchau mãe."
    play sound "sound/Phoneend.wav"
    hide phone
    pause 3
    "E agora?"
    "Ainda tem a Jasmine para vir me buscar..."
    "E o Jonas ainda não me ligou."

    play sound "sound/Toquedocel.wav"
    ". . ."
    show phone at right with zoomin:
        zoom 0.7
    Dory "Mãe? Mudou de ideia?"
    Jasmine "Não sou sua mãe doida!"
    Dory "Ah, desculpa amiga!"
    Jasmine "Meu nome aparece no seu celular..."
    Jasmine "Ficou cega foi?"
    Dory ". . ."
    Jasmine "Liguei pra falar que o Jo as  ã   i  con  e  i   r  í"
    Dory "Como é?"
    Jasmine "O Jo as  ã   i  con  e  i   r  í!"
    Dory "Alô? Amiga, a ligação está ruim!"
    Jasmine "Sér   ux    anc  d  o s   al  ev   r   i"
    Dory "Alô?"
    Jasmine ". . ."
    Dory "Alô??"
    play sound "sound/Phoneend.wav"
    hide phone
    pause 1

    "Que droga!"
    "O que será que ela queria me falar?"
    "Acho que eu entendi que o Jonas estava vindo aqui..."
    "Ou será que foi minha imaginação desejando ter ouvido isso?"
    stop music fadeout 1.0
    play music "music/Thunder.wav"
    Y "Amor?"
    Dory "Hum? Quem está aí?"
    Y "Sou eu vida!"
    Dory "Jonas, é você?"
    Y "Você continua perfeita meu amor!"
    Dory "Err, o que você quer dizer com isso?"
    Y "Desde aquele momento, no seu carro..."
    Dory "Você está me assustando..."
    Y "Me desculpe, venha aqui."
    "Ele está me deixando tocá-lo."
    show Yuri with fade:
        yalign 1.5
        xalign 0.9
    Y "E agora? Me reconhece?"
    Dory "Bem, você é magrelo... hahaha!"
    Y "Hum?"
    Y "Tanto quanto o Jonas?"
    scene bgdoctor at center with hpunch
    show Yuri:
        yalign 1.5
        xalign 0.9
    Dory "O QUÊ?"
    Dory "Se você não é o Jonas, quem é você?"
    Y "HAHAHAHAHA!"
    Dory "Essa risada..."
    Dory "Yuri..."
    Yuri "Olha só, até que enfim me reconheceu!"
    Yuri "Achei que a pancada tinha sido o suficiente para te deixar lelé!"
    Yuri "Mas acho que devia ter {color=#f99}caprichado{/color} melhor!"
    if FINAL_yuriepreso == True:
        Dory "EU SABIA!"
    if FINAL_yuritemata == True:
        Dory "EU DEVERIA TER SUSPEITADO!"
    Dory "Você armou tudo, não foi?"
    Yuri "Claro gata e aposto que você nem sabe o porquê..."
    Dory "Então me diga você."
    Yuri "Sua família era a maior patrocinadora do Saint Peterson."
    Yuri "E foi em uma noite assim, que meu pai... morreu."
    scene bgdoctor at center with hpunch
    show Yuri:
        yalign 1.5
        xalign 0.9
    Yuri "E FOI TUDO CULPA DE VOCÊS QUE PARARAM DE SUSTENTAR ESSE LUGAR!!!"
    Yuri "Meu pai morreu..."
    Yuri "Mas a princesinha tinha que ter sobrevivido né?"
    Yuri "E essa droga de celular..."
    Yuri "Procurei por toda parte naqueles destroços e não o encontrei."
    Yuri "Você deve ter escondido ele pra valer né?"
    Yuri "Depois da conversa que tivemos enquanto você dirigia..."
    Yuri "Sua irresponsável! Era o crime perfeito!"
    Yuri "E então, quando estou desfrutando minha vingança bem sucedida,"
    Yuri "Você me assusta, como um fantasma me ligando desse número maldito!"
    Dory "Seu despresível!"
    Yuri "Silêncio! Agora sou eu quem falo."
    menu:
        "SOCORRO! DOUTORA!":
            play sound "sound/Shoot.ogg"
            scene teste at center with dissolve
            pause 0.5
            scene bgdoctor at center with dissolve
            pause 2
            Yuri "Uma pena que teve que ser assim..."
            Yuri "A propósito, aquela doutorazinha morreu mais rápido que você!"
            Yuri "AHAHAHAHAHAHA!"
            ""
            "{color=#f99}FINAL RUIM{/color}"
        "Está bem, diga o que quer":
            Yuri "Você morta, é claro!"
            Yuri "Senão eu não teria dado o trabalho de sabotar seu carro..."
            if FINAL_yuriepreso == True:
                Yuri "Uma pena que teve que ser assim..."
                play sound "sound/Shoot.ogg"
                scene teste at center with dissolve
                pause 0.5
                scene bgdoctor at center with dissolve
                pause 2
                hide Yuri
                "Ué, eu não sinto dor..."
                "Será que é assim morrer?"
                Karen "DORY!"
                show Karen normal with fade:
                    yalign 1.5
                    xalign 0.9
                Karen "Graças a Deus eu cheguei a tempo!"
                Dory "O quê?"
                Dory "Doutora?"
                Dory "Você matou o Yuri?"
                Karen "Eu não, mas a polícia sim..."
                Karen "Eu chamei eles depois da nossa conversa."
                Karen "Estávamos assistindo tudo, bem atrás do Yuri!"
                Karen "Por sorte você está assim e não nos viu!"
                Karen "Teria estragado nosso ataque surpresa!"
                Karen "Nosso plano era apenas prendê-lo..."
                Karen "Mas não tivemos escolha quando ele sacou a arma."
                Karen "Você está ferida?"
                Dory "Não... MUITO OBRIGADA DOUTORA!!!"
                Karen "Venha, vamos avisar a todos que estamos bem!"
                scene teste at center with dissolve
                pause 2
                ""
                "{color=#f999}FINAL BOM{/color}"
            if FINAL_yuritemata == True:
                Yuri "Uma pena que teve que ser assim..."
                play sound "sound/Shoot.ogg"
                scene teste at center with dissolve
                pause 0.5
                scene bgdoctor at center with dissolve
                pause 2
                Yuri "A propósito, aquela doutorazinha morreu mais rápido que você!"
                Yuri "AHAHAHAHAHAHA!"
                ""
                "{color=#f99}FINAL RUIM{/color}"
