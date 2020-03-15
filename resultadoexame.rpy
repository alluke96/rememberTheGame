label resultadoexame:
    show Karen normal with fade:
        yalign 1.5
        xalign 0.9
    Karen "Olá novamente!"
    Karen "Alguns dos seus exames ficaram prontos."
    Karen "Vamos dar uma olhada..."
    Karen "Parece que o que deixou você 'cega' foi uma pancada muito forte na cabeça..."
    Karen "Faz sentido com o fato de você estar confusa com as suas memórias..."
    Dory "Sim..."
    Karen "Mas algo me intriga nessa história toda..."
    Karen "Pelo relatório dos socorristas, você estava de cinto de segurança."
    Karen "Seu carro possuía airbag."
    Karen "E no local onde você bateu não havia indícios de algo ter atingido sua cabeça com a força necessária..."
    Karen "Me desculpe, mas eu ouvi sua mãe dizer que você apronta muito né?"
    Dory "Doutora!"
    Karen "Perdão... Mas é uma possibilidade! Você pode ter se envolvido em uma briga antes do acidente!"
    if contou_quebebe == True:
        Karen "Você também me contou que bebe né..."
        Karen "Pode ter sido em um bar ou em uma festa, sei lá!"
    Karen "Isso ou alguém armou todo o acidente para acobertar um delito..."
    Dory "Nossa! Será?"
    Karen "Vou dar mais uma olhada, isso não pode estar correto..."
    Karen "Se cuida, tá bom?"
    Dory "Como assim?"
    Karen "Não sei... Este hospital não possui segurança nenhuma! E se..."
    menu:
        "Doutora, acho que a senhora está exagerando!":
            $ FINAL_yuritemata = True #DEFINICAO DO FINAL 1/?
            Karen "Acho que você tem razão..."
            Karen "Me perdoe."

        "Doutora, acho que a senhora tem toda a razão!":
            $ FINAL_yuriepreso = True #DEFINICAO DO FINAL 1/?
            Karen "Vou avisar meus superiores."
            Karen "Enquanto isso, evite sair do seu quarto!"

    Karen "Bem, eu preciso verificar como estão meus outros pacientes."
    Dory "Está bem..."
    Karen "De qualquer jeito, tome cuidado."
    hide Karen with fade
    ". . ."
    "Será que fiz a escolha certa?"
    jump contfinal
