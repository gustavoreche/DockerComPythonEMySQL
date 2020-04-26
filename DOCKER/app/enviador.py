import mysql.connector
from bottle import route, run, request
from datetime import date

def registraMensagem(assunto, mensagem):
    conexao = mysql.connector.connect(host="db", user="root", passwd="root", database="emailDocker")
    cursor = conexao.cursor()
    sql = 'INSERT INTO emails (data_email, assunto, mensagem) VALUES (%s, %s, %s)'
    dataAtual = date.today()
    dataFormatada = dataAtual.strftime('%Y/%m/%d')
    valores = (dataFormatada, assunto, mensagem)
    cursor.execute(sql, valores)
    cursor.close()
    conexao.commit()
    conexao.close()

    print('Mensagem registrada!')

@route('/', method="POST")
def envia():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    registraMensagem(assunto, mensagem)

    return 'Mensagem na fila! <br> Assunto: {}. <br> Mensagem: {}.'.format(
        assunto, mensagem
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port = 8080, debug = True)