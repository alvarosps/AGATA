# AGATA
Automatic Generation of AIML from Text Acquisition

<div>
	<h3>*IMPORTANTE*</h3>
	<p>Caso já tenha instalado, sempre fazer um <strong><em>git pull origin master</em></strong> antes de utilizar, para garantir que está usando a versão mais atualizada do sistema. Para isso, deve estar na pasta do projeto(comando <em>cd</em>)</p>

<div>
	<h3>Como fazer a instalação</h3>
	<ul>
		<li>Necessário Python 3.6, instalador: https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe</li>
		<b>*Cuidar na instalação:</b> [X] no "Add Python to System Path", na primeira parte da instalação <br>
		<li>Baixar o zip do projeto, ou git fork/clone no repositório git.</li>
			<ol type='1'>
				<li>Para clonar o repositório, basta dar Fork nele, e então <strong><em>git clone ...</em></strong>, onde ... é a url do repositório com fork de vocês</li>
		</ol>
	</ul>
</div>

<div>
	<h3>Setup inicial(necessário fazer apenas 1 vez), Com Python já instalado:</h3>
	<ol type='1'>
		<li>Abrir Prompt de Comando do Windows (digitar <em><strong>cmd</strong></em> na barra de pesquisa/tarefas)</li>
		<li>Instalar bibliotecas necessárias ao projeto, digitando os seguintes comandos, 1 a 1</li>
			<ol type='1'>
				<li><strong><em>pip install django</em></strong></li>
				<li><strong><em>pip install django-bootstrap-form</em></strong></li>
				<li><strong><em>pip install bs4</em></strong></li>
				<li><strong><em>pip install lxml</em></strong></li>
				<li><strong><em>pip install nltk</em></strong></li>
			</ol>
		<li>No terminal, digitar(para abrir o console do Python): <strong><em>python</em></strong></li>
			<ol type='1'>
				<li><strong><em>import nltk</em></strong></li>
				<li><strong><em>nltk.download('punkt')</em></strong></li>
				<li><strong><em>exit()</em></strong></li>
			</ol>
		<li>Agora, ir para a pasta que o projeto está(por exemplo, o meu projeto está em "C:\Users\alvarosps\git\textMining")</li>
			<ol type='1'>
				<li><strong><em>cd "C:\Users\alvarosps\git\textMining"</em></strong></li>
				<li><strong><em>dir</em></strong> (vai listar os arquivos que estão na pasta, para garantir, verifique se o arquivo manage.py está na pasta)</li>
				<li>Com o arquivo manage.py na pasta, digitar: <strong><em>python manage.py migrate</em></strong></li>
			</ol>
	</ol>
</div>

<div>
	<h3>Para rodar o programa</h3>
	<ol type='1'>
		<li>Ir para a pasta que o projeto está(por exemplo, o meu projeto está em "C:\Users\alvarosps\git\textMining")</li>
			<ol type='1'>
				<li><strong><em>cd "C:\Users\alvarosps\git\textMining"</em></strong></li>
				<li><strong><em>dir</em></strong> (vai listar os arquivos que estão na pasta, para garantir, verifique se o arquivo manage.py está na pasta)</li>
				<li>Com o arquivo manage.py na pasta, digitar: <strong><em>python manage.py runserver</em></strong></li>
				<strong>*NÃO FECHAR ESSE TERMINAL</strong>
				<li>Agora, abrir o seu navegador, e entrar no link: <a href="localhost:8000">localhost:8000</a></li> 
			</ol>
	</ol>
</div>
