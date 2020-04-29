import mysql.connector
import redis
import json
from bottle import Bottle, request
from datetime import date

class Enviador(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.envia)
        self.fila = redis.StrictRedis(host='filaService', port=6379, db=0)
        self.conn = mysql.connector.connect(host="db", user="root", passwd="root", database="emailDocker")

    def registraMensagem(self, assunto, mensagem):
        #conexao = mysql.connector.connect(host="db", user="root", passwd="root", database="emailDocker")
        cursor = self.conn.cursor()
        sql = 'INSERT INTO emails (data_email, assunto, mensagem) VALUES (%s, %s, %s)'
        dataAtual = date.today()
        dataFormatada = dataAtual.strftime('%Y/%m/%d')
        valores = (dataFormatada, assunto, mensagem)
        cursor.execute(sql, valores)
        cursor.close()
        self.conn.commit()
        #self.conn.close()

        mensagem = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('enviador', json.dumps(mensagem))

        print('Mensagem registrada!')

    def envia(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.registraMensagem(assunto, mensagem)

        return 'Mensagem na fila! <br> Assunto: {}. <br> Mensagem: {}.'.format(
            assunto, mensagem
        )

if __name__ == '__main__':
    enviador = Enviador()
    enviador.run(host='0.0.0.0', port = 8080, debug = True)