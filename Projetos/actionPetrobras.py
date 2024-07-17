# import yfinance as yf
# import smtplib
# import schedule
# import time

# Configurações do alerta
ACAO = "PETR4.SA"
VALOR_ALVO = 30.00
EMAIL_DE = "pauloengenharia5@yahoo.com,"
EMAIL_PARA = "paulinho_skateboards@yahoo.com.br"
SENHA = "123456"

def enviar_email(mensagem):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_DE, SENHA)
        server.sendmail(EMAIL_DE, EMAIL_PARA, mensagem)
        server.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

def verificar_acao():
    acao = yf.Ticker(ACAO)
    dados = acao.history(period="1d")
    preco_atual = dados['Close'][0]
    print(f"Preço atual da ação {ACAO}: R$ {preco_atual}")

    if preco_atual >= VALOR_ALVO:
        mensagem = f"Alerta: A ação {ACAO} atingiu o valor de R$ {preco_atual}"
        enviar_email(mensagem)

# Agendar a verificação a cada hora
schedule.every(1).hour.do(verificar_acao)

# Loop para manter o script em execução
while True:
    schedule.run_pending()
    time.sleep(1)
