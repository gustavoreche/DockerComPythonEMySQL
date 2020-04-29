import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    pegaRedis = redis.Redis(host='filaService', port=6379, db=0)
    while True:
        mensagem = json.loads(pegaRedis.blpop('enviador')[1])
        #Simulando envio de e-mail
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem:', mensagem['assunto'], 'enviada')