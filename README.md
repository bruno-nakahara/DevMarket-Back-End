<h1>DevMarket-Back-End</h1>

<h2>Como é a aplicação?</h2>

<p>Projeto que cria, mostra, edita e remove produtos, um CRUD com upload de imagem</p>

<h2>Tecnologias e ferramentas</h2>

<ul>
  <li>Python</li>
  <li>MongoDB</li>
  <li>Flask</li>
  <li>GridFs</li>
  <li>Codecs</li>
</ul>

<h2>Instalação e uso</h2>

<h3>Requisitos</h3>
<p>No seu computador, com sistema operacional windows, tem que ter o <a href="https://www.python.org/downloads/">Python</a> e o <a href="https://www.mongodb.com/try/download/community">MongoDB</a> instalados.</p>

<p>Cria uma pasta onde irá baixar os códigos. Após criar a pasta siga os passos abaixo:</p>

```
# No terminal da pasta criada, copie o repositório com o seguinte comando
$ git clone https://github.com/bruno-nakahara/Freshmania-Back-End.git

# Após clonar o repositório, pelo terminal, entra na pasta usando o comando
$ cd Freshmania-Back-End

# Criar um ambiente virtual com nome venv para instalar as dependências
$ python -m venv venv

# Depois de criar o ambiente virtual, ative o virtualenv com o comando
$ venv\Scripts\Activate.bat

# Após a ativação, baixe as dependências utilizando o comando 
$ pip install -r requirements.txt

# Verifica as dependências instaladas do requirements.txt com comando
$ pip list

# Se tem todas as dependências, então rode a aplicação com
$ py server.py

# e pronto! Back-end da Aplicação rodando.
# Na pasta images tem algumas imagens para testar a aplicação.
```
