import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os

try:
    print('Enviando...')
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    # Coloque seu email no arquivo de texto 'email.txt'
    with open('email.txt', 'r') as e:
        email = e.read()
    # Coloque sua senha no arquivo de texto 'senha.txt'
    with open('senha.txt', 'r') as s:
        senha = s.read()
    # Coloque emails que deseja enviar a mensagem no arquivo de texto 'lista-emails.txt'
    # separados por virgula dessa forma: fulano@gmail.com, ciclano@gmail.com
    with open('lista-emails.txt', 'r') as l:
        lista = l.read()
    # Coloque o texto que deseja enviar dentro do arquivo mensagem.txt
    with open('mensagem.txt', 'r') as m:
        mensagem = m.read()

    login=0
    try:
        login = server.login(email, senha)
    except Exception as e:
        pass
    if (login == 0):
        print('Algo de errado ocorreu, tente as dicas abaixo:')
        print('1- Verifique se escreveu o email e senha corretamente')
        print('2- Libere acesso ao seu email em: \n Passo 1: https://myaccount.google.com/u/2/security \n Passo 2: Acesso a apps menos seguros[Ativar]')
    else:
        print('Acesso concedido...')

    Assunto = "Assunto" # modifique aqui
    De = "Alguem"  # modifique aqui
    Para = lista

    msg = MIMEMultipart()
    msg['From'] = De
    msg['To'] = Para
    msg['Subject'] = Assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    Text = msg.as_string()

    server.sendmail(email, Para, Text)
    print('Email Enviado')

    server.close()
except Exception as e:
        pass