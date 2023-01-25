"""https://www.filipeflop.com/blog/exportar-dados-para-google-sheets-atraves-da-raspberry-pi/
Primeiramente, faça login na sua conta Google
Uma vez logado, acesse a criação de um novo projeto no site de
bibliotecas de APIs do Google. Link:
https://console.developers.google.com/projectcreate

Na tela de criação do projeto, preencha o nome do projeto (no caso deste
post, será “TesteGoogleSheets”) e clique no botão “Criar”. Aguarde
alguns segundos enquanto o projeto é criado.

Você será automaticamente direcionado à tela de informações do seu
projeto. Na sessão “API”, clique sobre “Ir para a visão geral de APIs”.
Na tela que abrir, localize no lado esquerdo o botão “Biblioteca” e
clique nele.

Você será direcionado ao site da biblioteca de APIs Google. No campo de
busca, digite “Google Drive API” e clique sobre a primeira ocorrência
(chamada “Google Drive API”, com o símbolo do Google Drive).

Você serpa direcionado à tela de informações da API do Google Drive.
Clique no botão “Ativar” e aguarde alguns segundos até a ativação ser
concluída.

Após a ativação, você será direcionado para a tela de APIs e serviços de
seu projeto. Clicando novamente em “Bibliotecas”, procure pela API
“Google Sheets API”, clique sobre ela e a ative.

Após a ativação, você será direcionado para a tela de APIs e serviços de
seu projeto. Nela, localize o botão “Criar credenciais” no lado direito
da tela.

Na pergunta “Qual API você usa?”, selecione “Google Drive API”

Na pergunta “De onde você chamará a API?”, selecione “Servidor da web
(por exemplo, node.js, Tomcat)”

Na pergunta “Que dados você acessará?”, selecione “Dados do aplicativo”
Na pergunta “Você planeja usar essa API com o App Engine ou o Compute Engine?”, selecione “Não, nenhum” e clique no botão “Preciso de quais credenciais?”
Uma nova tela irá surgir. Nela, preencha o campo “Nome da conta de serviço” com o nome da conta de serviço da API que deseja. Nesse post, utilizei “ServicoTesteGoogleSheets” como nome de serviço.
Ainda na mesma tela, em “papel”, selecione “Projeto” e depois “Editor”
Em “Tipo de chave”, selecione “JSON” e clique no botão “Continuar”
Será feito automaticamente o download de um arquivo JSON contendo as credenciais para o acesso à API do Google pelo seu projeto. Mude o nome do arquivo para “credenciais.json” e salve-o em local seguro.
Envie o arquivo JSON para a Raspberry PI, no diretório em que ficará seu projeto. Para esse post, coloquei no diretório home do usuário padrão pi (/home/pi)
Vá até o Google Sheets (www.google.com/intl/pt-BR/sheets/about/) e crie uma nova planilha chamada “Planilha teste”. Esta será a planilha a qual a Raspberry PI enviará as informações.
Abra o arquivo JSON de credenciais obtido no passo 16 e busque pela informação “client_email”. Copie (sem as aspas) o e-mail que fica na frente desta informação.
Na planilha criada no passo 18, localize no lado superior direito o botão “Compartilhar” e clique nele. No campo de texto, insira o e-mail copiado no passo 19 e clique no botão “Enviar”. Aguarde alguns segundos para que o compartilhamento seja concluído."""
