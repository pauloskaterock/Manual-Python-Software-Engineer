# 🐍 Roteiro de Estudos: Automatize Tarefas Maçantes com Python

Este documento serve como guia e índice de progresso no estudo do livro "Automatize Tarefas Maçantes com Python".

---

## [cite_start]📚 Parte I: Básico da Programação Python [cite: 856]

O foco inicial é construir os fundamentos essenciais da linguagem.

### [cite_start]Capítulo 1: Básico sobre o Python [cite: 857]

- [ ] [cite_start]Fornecendo expressões no shell interativo [cite: 858]
- [ ] [cite_start]Tipos de dado (inteiro, ponto flutuante e string) [cite: 858]
- [ ] [cite_start]Variáveis e instruções de atribuição [cite: 859]
- [ ] Nosso Primeiro Programa (Dissecando e Comentários)
- [ ] Funções Essenciais: `print()`, `input()`, `len()`, `str()`, `int()`, `float()`

### [cite_start]Capítulo 2: Controle de Fluxo [cite: 861]

- [ ] Valores Booleanos e Operadores de Comparação
- [ ] Operadores Booleanos (`and`, `or`, `not`)
- [ ] Instruções Condicionais: `if`, `else`, `elif`
- [ ] Loops: `while` e `for`
- [ ] Funções de Controle: `break`, `continue`, `range()`, `sys.exit()`

### [cite_start]Capítulo 3: Funções [cite: 862]

- [ ] Definindo Funções (`def`) e Parâmetros
- [ ] Valores de Retorno (`return`) e o Valor `None`
- [ ] Escopo Local e Global (`global`)
- [ ] Tratamento de Exceções (`try` e `except`)
- [ ] Projeto Prático: Adivinhe o Número

### [cite_start]Capítulo 4: Listas [cite: 862]

- [ ] Tipo de Dado Lista (Índices e Slices)
- [ ] Métodos de Lista: `append()`, `insert()`, `remove()`, `sort()`
- [ ] Operadores `in` e `not in`
- [ ] Tipos Mutáveis (Listas) vs. Imutáveis (Tuplas)
- [ ] Funções `list()` e `tuple()`

### [cite_start]Capítulo 5: Dicionários e Estruturação de Dados [cite: 863]

- [ ] Tipo de Dado Dicionário (Chaves e Valores)
- [ ] Métodos: `keys()`, `values()`, `items()`, `get()`, `setdefault()`
- [ ] Modelando objetos do mundo real (Ex: Tabuleiro de Jogo da Velha)

### [cite_start]Capítulo 6: Manipulação de Strings [cite: 864]

- [ ] Indexação e Slicing de Strings
- [ ] Métodos Úteis: `upper()`, `lower()`, `startswith()`, `endswith()`
- [ ] Formatando Texto: `join()`, `split()`, `rjust()`, `ljust()`, `center()`, `strip()`
- [ ] Módulo `pyperclip` (Copiando e Colando)
- [ ] Projeto: Repositório de Senhas

---

## [cite_start]🚀 Parte II: Automatizando Tarefas [cite: 864]

Esta parte transforma seu conhecimento fundamental em habilidades de automação prática.

### [cite_start]Capítulo 7: Correspondência de Padrões com Expressões Regulares [cite: 864]

- [ ] Objetos Regex
- [ ] Padrões Comuns: Grupos, Pipe, Opcional (`?`), Zero ou Mais (`*`), Um ou Mais (`+`)
- [ ] Classes de Caracteres e `findall()`
- [ ] Substituindo Strings com `sub()`
- [ ] Projeto: Extrator de Números de Telefone e Emails

### [cite_start]Capítulo 8: Lendo e Escrevendo em Arquivos [cite: 866]

- [ ] Arquivos e Paths (Caminhos)
- [ ] Módulo `os` e `os.path` (Criando pastas, lidando com paths)
- [ ] Processo de Leitura/Escrita: `open()`, `read()`, `write()`
- [ ] Módulo `shelve` (Salvando variáveis)
- [ ] Projeto: Gerando Arquivos Aleatórios de Provas

### [cite_start]Capítulo 9: Organizando Arquivos [cite: 867]

- [ ] Copiando, Movendo, Renomeando e Apagando Arquivos
- [ ] Módulo `send2trash` (Apagamento seguro)
- [ ] Percorrendo uma Árvore de Diretório (`os.walk`)
- [ ] Compactando/Descompactando com `zipfile`
- [ ] Projeto: Fazer Backup de uma Pasta Usando um Arquivo ZIP

### [cite_start]Capítulo 10: Debugging [cite: 868]

- [ ] Gerando Exceções (`raise`) e `tracebacks`
- [ ] Utilizando o Módulo `logging`
- [ ] Níveis de Logging (`DEBUG`, `INFO`, `WARNING`, etc.)
- [ ] Utilizando o Debugger do IDLE (Go, Step, Over, Out, Quit)

### [cite_start]Capítulo 11: Web Scraping [cite: 868]

- [ ] Módulo `webbrowser`
- [ ] Fazendo Download de Arquivos com `requests`
- [ ] [cite_start]Parse de HTML com `BeautifulSoup` (`select()`) [cite: 869]
- [ ] [cite_start]Controlando o Navegador com `Selenium` [cite: 869]
- [ ] Projeto: Downloading de todas as tirinhas XKCD

### [cite_start]Capítulo 12: Trabalhando com Documentos Excel [cite: 870]

- [ ] Módulo `openpyxl` (Instalação e Básico)
- [ ] Lendo Dados: Planilhas, Células, Linhas e Colunas
- [ ] Escrevendo Dados: Criando, Removendo e Escrevendo em Células
- [ ] Formatação (Estilo de Fonte, Fórmulas, Gráficos)

### [cite_start]Capítulo 13: Trabalhando com Documentos PDF e Word [cite: 871]

- [ ] Documentos PDF: Extraindo Texto e Descriptografando (Módulo `PyPDF2`)
- [ ] Criando e Combinando PDFs
- [ ] Documentos Word: Lendo e Escrevendo (`python-docx`)
- [ ] Estilizando Parágrafos e Objetos Run

### [cite_start]Capítulo 14: Trabalhando com Arquivos CSV e Dados JSON [cite: 872]

- [ ] Módulo `csv` (Objetos Reader e Writer)
- [ ] [cite_start]JSON: Lendo (`loads()`) e Escrevendo (`dumps()`) [cite: 872]
- [ ] Projeto: Acessando dados atuais de previsão do tempo (JSON e APIs)

### [cite_start]Capítulo 15: Monitorando Tempo, Agendando Tarefas e Iniciando Programas [cite: 872]

- [ ] Módulo `time` (`time.time()`, `time.sleep()`)
- [ ] Módulo `datetime` (Objetos `datetime` e `timedelta`)
- [ ] Multithreading (Básico)
- [ ] Iniciando Outros Programas a Partir do Python (`subprocess.Popen`)

### [cite_start]Capítulo 16: Enviando Emails e Mensagens de Texto [cite: 874]

- [ ] Módulo `smtplib` (SMTP): Enviando emails (Conexão, TLS, Login)
- [ ] Módulo `imapclient` (IMAP): Obtendo e apagando emails
- [ ] Enviando mensagens de texto com o `Twilio`

### [cite_start]Capítulo 17: Manipulando Imagens [cite: 875]

- [ ] Módulo `Pillow` (PIL)
- [ ] Básico sobre Imagens (RGBA, Coordenadas)
- [ ] Recortando, Redimensionando, Girando Imagens
- [ ] Desenhando Formas e Textos em Imagens

### [cite_start]Capítulo 18: Controlando o Teclado e o Mouse com Automação de GUI [cite: 876]

- [ ] Módulo `pyautogui` (Instalação e Básico)
- [ ] Movimento do Mouse (`moveTo()`, `moveRel()`, `position()`)
- [ ] Interação com o Mouse (Cliques, Arrastar, Rolagem)
- [ ] Automação de Teclado (`typewrite()`, Nomes de Teclas, Atalhos)
- [ ] Trabalhando com a Tela (Captura de Tela e Reconhecimento de Imagens)
- [ ] Projeto: Preenchimento Automático de Formulários
