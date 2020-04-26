# Instale o Docker
Se o seu ambiente for linux, seguem os comandos:

- Instalando o Docker

  sudo apt-get update

  sudo apt-get install     apt-transport-https     ca-certificates     curl     gnupg-agent     software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

  sudo apt-get update

  sudo apt-get install docker-ce docker-ce-cli containerd.io

- Após os comandos acima, execute o comando abaixo e deve ser retornado os comandos do Docker
  
  docker --help
 
- Após ter a certeza de que o Docker está instalado no seu ambiente, execute o comando abaixo para que você possa executar o Docker como usuário normal, ou seja, sem sudo
  
  sudo chown USUARIODAMAQUINA /var/run/docker.sock
  
- Execute o comando abaixo para ver o seu primeiro container sendo executado
  
  sudo docker container run hello-world
  
- Execute o comando abaixo para instalar o Docker Compose, que serve para inicializarmos diversos containers com apenas um comando

  sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  
- Execute o comando abaixo para dar permissões ao Docker Compose

  sudo chmod +x /usr/local/bin/docker-compose
  
# Executando o projeto

- Abra o terminal no diretório em que está o arquivo "docker-compose.yml"

- Lembrando que, os diretórios "app", "nginx", "scripts", e "web" tem que estar no mesmo diretório que o arquivo "docker-compose.yml"

- Execute o comando abaixo para inicializar os containers
  
  docker-compose up --build -V
  
- Abra seu navegador, e digite o endereço "http://localhost:80", e tem que aparecer o html criado

- Insira um assunto, uma mensagem, e selecione o botão "enviar"

- Terá que aparecer as mensagens abaixo
  Mensagem na fila!
  Assunto: ASSUNTO QUE VOCE DIGITOU.
  Mensagem: MENSAGEM QUE VOCE DIGITOU.
  
- Para verificar se gravou no banco de dados o assunto e a mensagem digitados, execute o seguinte comando em um novo terminal
  docker exec -t containerBancoDeDados mysql -uroot -proot -e "use emailDocker; select * from emails"
  
# Alterando o projeto

- Alterando o Banco de Dados
  - Para realizar alterações no arquivo "init.sql"(como criar mais tabelas, inserts, deletes, etc..), no diretório "scripts", apague o diretório onde os dados são persistidos, que no nosso exemplo é o diretório ".docker", que fica no mesmo diretório que o arquivo "docker-compose.yml". Esse diretório é mapeado no arquivo "docker-compose.yml", no services, db, volumes, e mapeia o seguinte diretório do container do MySQL -> /var/lib/mysql.
  
- Alterando o Front-End
  - Para alterar a página que envia as informações do usuário, substitua o arquivo "index.html", no diretório "web", lembrando que o botão que irá enviar os dados ao app, que fará a comunicação com o banco de dados, tem que enviar para o seguinte endereço
    http://localhost/api
