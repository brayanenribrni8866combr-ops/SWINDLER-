🐇 SWINDLER

🔐 Security & Data Laboratory — Terminal Toolkit

«SWINDLER é um toolkit de terminal desenvolvido para estudos, testes locais e demonstrações de segurança, validação de dados e automação em ambiente controlado.»

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

📌 Sobre o projeto

O SWINDLER foi criado como um painel de terminal com interface inspirada em ferramentas de cybersecurity.

O projeto reúne diferentes recursos em um único menu, incluindo:

- geração de dados sintéticos;
- validação de documentos;
- ferramentas de codificação;
- geração e análise de senhas;
- informações do ambiente de rede;
- detecção de interface VPN;
- scanner restrito ao próprio dispositivo;
- autenticação administrativa;
- controle de acesso de clientes;
- geração de tokens para laboratório;
- registro de atividades.

O objetivo é proporcionar um ambiente prático para aprendizado, testes e demonstrações, mantendo as funções de rede restritas ao ambiente local.

---

⚠️ Aviso importante

O SWINDLER deve ser utilizado somente em sistemas, dispositivos e redes que você possui ou possui autorização para testar.

As funções de geração de documentos, identidades, cartões, contas, veículos e outros dados são sintéticas/de teste e não devem ser utilizadas para fraude, falsificação, obtenção de serviços ou representação de uma pessoa real.

O scanner de rede incluído no projeto é restrito ao endereço:

127.0.0.1

O projeto não foi desenvolvido para invasão de sistemas de terceiros, roubo de credenciais, interceptação de códigos de autenticação ou acesso não autorizado.

---

✨ Recursos

🔐 Controle de acesso

O SWINDLER possui um sistema local de usuários com:

- conta administrativa;
- criação de clientes;
- ativação/desativação de acesso;
- remoção de clientes;
- alteração da senha administrativa;
- armazenamento protegido por hash;
- registro de eventos;
- bloqueio de usuários sem autorização.

As credenciais ficam armazenadas localmente e arquivos sensíveis são ignorados pelo Git através do ".gitignore".

---

🧰 31 funções disponíveis

👤 Dados sintéticos

"{01}" Identidade completa de teste

Gera um conjunto de informações sintéticas para utilização em testes locais.

"{02}" CPF de teste

Gera um CPF destinado a testes.

"{03}" RG simulado

Gera informações de RG fictícias.

"{04}" CNPJ de teste

Gera um CNPJ para utilização em ambiente de testes.

"{05}" CNH de teste

Gera uma identificação de CNH sintética.

"{06}" PIS/PASEP de teste

Gera dados sintéticos para testes de validação.

"{07}" Título de eleitor de teste

Gera dados fictícios para testes.

"{08}" Certidão de teste

Gera informações sintéticas de certidão.

"{09}" Empresa sintética

Cria informações fictícias de uma empresa.

"{10}" Cartão de teste

Gera dados de cartão destinados exclusivamente a testes.

"{11}" Veículo / RENAVAM / Chassi simulados

Gera informações fictícias de veículos.

"{12}" Conta bancária simulada

Gera dados bancários sintéticos para testes.

---

🔑 Segurança e criptografia

"{13}" Gerar senha

Cria uma senha aleatória para testes.

"{14}" Text-to-Hash

Transforma um texto em hash utilizando SHA-256.

"{15}" Base64 Encode

Codifica texto utilizando Base64.

"{16}" Base64 Decode

Decodifica conteúdo Base64.

"{17}" UUID v4

Gera identificadores UUID versão 4.

---

🌐 Ambiente de rede

"{18}" Ambiente de rede simulado

Cria informações de rede sintéticas para demonstrações e testes.

"{19}" Lorem Ipsum

Gera texto de preenchimento.

"{26}" Scanner localhost

Executa uma verificação de portas exclusivamente no próprio dispositivo:

127.0.0.1

"{27}" Informações de rede

Exibe informações disponíveis sobre o ambiente de rede local.

"{30}" Status VPN

Verifica interfaces relacionadas a VPN no dispositivo.

«O programa não afirma que uma VPN está ativa apenas porque uma interface existe. A função serve para identificar o estado observado no ambiente local.»

---

🧪 Validação

"{20}" Validar CPF

Verifica a validade matemática de um CPF.

"{21}" Validar CNPJ

Verifica a validade de um CNPJ.

"{22}" Validar CNH

Executa validações relacionadas à CNH.

"{23}" Validar PIS

Valida um número PIS/PASEP.

"{24}" Validar Título

Executa validação do título de eleitor.

"{25}" Validar Certidão

Executa verificações relacionadas aos dados de certidão utilizados pelo laboratório.

---

🛡️ Recursos adicionais

"{28}" Gerar senha segura

Gera uma senha com maior complexidade para testes de segurança.

"{29}" Analisar senha

Analisa características de uma senha e apresenta uma avaliação de força.

"{31}" Token de laboratório

Gera um token aleatório destinado a testes locais.

---

📱 Compatibilidade

O SWINDLER foi desenvolvido pensando principalmente em:

- Android + Termux
- Linux
- Python 3

Também pode funcionar em outros ambientes compatíveis com Python, dependendo das bibliotecas utilizadas.

---

🚀 Instalação

1. Instale o Python

No Termux:

pkg update
pkg upgrade
pkg install python git

Verifique:

python --version

---

2. Clone o projeto

git clone https://github.com/brayanenribrni8866combr-ops/SWINDLER-.git

Entre na pasta:

cd SWINDLER-

---

3. Instale as dependências

pip install faker validate-docbr

---

4. Execute

python main.py

---

🖥️ Exemplo de execução

███████╗██╗    ██╗██╗███╗   ██╗██████╗ ██╗     ███████╗██████╗
██╔════╝██║    ██║██║████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗
███████╗██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝
╚════██║██║███╗██║██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗
███████║╚███╔███╔╝██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║
╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝

                    SWINDLER
             SECURITY LABORATORY

---

📸 Screenshots

As imagens abaixo podem ser adicionadas posteriormente:

screenshots/
├── login.png
├── admin-panel.png
├── client-panel.png
├── generator.png
└── network.png

Depois, no README:

## 📸 Screenshots

### Login

![Login](screenshots/login.png)

### Painel administrativo

![Admin](screenshots/admin-panel.png)

### Painel do cliente

![Cliente](screenshots/client-panel.png)

### Ferramentas

![Ferramentas](screenshots/generator.png)

---

📂 Estrutura do projeto

SWINDLER/
│
├── main.py
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── login.png
│   ├── admin-panel.png
│   ├── client-panel.png
│   └── network.png
│
└── arquivos locais/
    ├── swindler_users.json
    └── swindler.log

Os arquivos contendo usuários e logs locais não devem ser publicados no GitHub.

---

🔒 Proteção de arquivos sensíveis

O projeto utiliza ".gitignore" para evitar o envio de arquivos locais contendo informações de autenticação e logs:

swindler_users.json
swindler_users_backup.json
swindler.log
__pycache__/
*.pyc

Isso é importante principalmente quando o projeto é utilizado em um repositório público.

---

🧠 Tecnologias utilizadas

O projeto utiliza principalmente:

- Python
- JSON
- hashlib
- secrets
- UUID
- Base64
- socket
- subprocess
- logging
- Faker
- validate-docbr

---

🧪 Filosofia do projeto

O SWINDLER foi desenvolvido com três objetivos principais:

1. Aprendizado

Permitir que iniciantes experimentem conceitos de:

- Python;
- terminal;
- autenticação;
- hashes;
- validação;
- redes;
- geração de dados;
- automação.

2. Laboratório

Criar um ambiente controlado para experimentar ferramentas sem depender de sistemas externos.

3. Demonstração

Apresentar diferentes conceitos de cybersecurity através de uma interface única de terminal.

---

🔐 Segurança

O projeto procura seguir o princípio:

«Teste somente aquilo que você tem autorização para testar.»

Recursos de rede são mantidos em escopo local sempre que possível.

Não utilize o SWINDLER para:

- acessar contas de terceiros;
- roubar credenciais;
- interceptar códigos de autenticação;
- atacar servidores;
- realizar fraude;
- falsificar documentos;
- obter serviços utilizando dados falsos;
- contornar sistemas de segurança;
- executar atividades sem autorização.

---

🛠️ Desenvolvimento

Para contribuir:

git clone https://github.com/brayanenribrni8866combr-ops/SWINDLER-.git
cd SWINDLER-

Crie uma alteração:

git add .
git commit -m "Descrição da alteração"

Envie:

git push

---

📌 Roadmap

Possíveis melhorias futuras:

- [ ] Interface de terminal ainda mais avançada
- [ ] Sistema de configuração
- [ ] Mais ferramentas de análise local
- [ ] Exportação de relatórios
- [ ] Sistema de logs aprimorado
- [ ] Testes automatizados
- [ ] Documentação técnica
- [ ] Mais ferramentas de laboratório
- [ ] Melhor gerenciamento de usuários
- [ ] Dashboard de estatísticas

---

👨‍💻 Autor

Rilex

Projeto desenvolvido para estudos, experimentação e aprendizado em programação e cybersecurity.

---

⭐ Apoie o projeto

Se o SWINDLER for útil para seus estudos:

⭐ Dê uma estrela no repositório.

🐛 Relate problemas através das Issues.

💡 Sugira melhorias.

🔀 Contribua com melhorias compatíveis com a proposta educacional do projeto.

---

📜 Licença

Este projeto é destinado a fins educacionais, experimentais e de laboratório.

Ao utilizar o SWINDLER, você é responsável por garantir que possui autorização para realizar qualquer teste executado através da ferramenta.

---

🐇 SWINDLER

Security Laboratory • Data Testing • Python • Terminal

«Learn. Test. Build. Secure.»
