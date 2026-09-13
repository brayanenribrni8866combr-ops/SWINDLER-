import os
import random
import string
import hashlib
import uuid
import base64
import time
import json
import secrets
import socket
import platform
import subprocess
from datetime import datetime, timedelta

from faker import Faker
from validate_docbr import (
    CPF, CNPJ, CNH, PIS, TituloEleitoral, Certidao
)

fake = Faker("pt_BR")

VERDE_BRILHANTE = "\033[1;32m"
VERDE_ESCURO = "\033[0;32m"
VERMELHO_SANGUE = "\033[1;31m"
CIANO = "\033[1;36m"
AMARELO_ALERTA = "\033[1;33m"
RESET = "\033[0m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_USUARIOS = os.path.join(BASE_DIR, "swindler_users.json")
ARQUIVO_LOG = os.path.join(BASE_DIR, "swindler.log")


def limpar_tela():
    os.system("clear" if os.name != "nt" else "cls")


def linha():
    print(f"{VERMELHO_SANGUE}" + "═" * 68 + f"{RESET}")


def animacao(texto="Inicializando SWINDLER", pontos=3, velocidade=0.18):
    print(f"{VERDE_BRILHANTE}{texto}", end="", flush=True)
    for _ in range(pontos):
        time.sleep(velocidade)
        print(".", end="", flush=True)
    print(RESET)


def carregando(texto="Processando"):
    print(f"{CIANO}{texto} ", end="", flush=True)
    for _ in range(4):
        print("█", end="", flush=True)
        time.sleep(0.10)
    print(f" {VERDE_BRILHANTE}OK{RESET}")


def pausar():
    input(f"\n{AMARELO_ALERTA}[ Pressione ENTER para continuar ]{RESET}")


def mostrar_hora():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{VERDE_ESCURO} [ SISTEMA ] {agora}{RESET}")


def registrar_log(mensagem):
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            arquivo.write(f"[{data}] {mensagem}\n")
    except OSError:
        pass


def banner_hacker():
    print(f"{VERMELHO_SANGUE}" + "☠ " * 34 + f"{RESET}")
    print(
        f"{VERMELHO_SANGUE}"
        "    ███████╗██╗    ██╗██╗███╗   ██╗██████╗ ██╗     ███████╗██████╗ \n"
        "    ██╔════╝██║    ██║██║████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗\n"
        "    ███████╗██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝\n"
        "    ╚════██║██║███╗██║██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗\n"
        "    ███████║╚███╔███╔╝██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║\n"
        "    ╚══════╝ ╚══╝╚══╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝"
        f"{RESET}"
    )
    print()
    print(f"{VERMELHO_SANGUE}              [ SWINDLER ]{RESET}")
    print(f"{AMARELO_ALERTA}       CYBERSECURITY / LAB TERMINAL{RESET}")
    print(f"{VERMELHO_SANGUE}" + "☠ " * 34 + f"{RESET}\n")


def hash_senha(senha, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    resultado = hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"),
        salt.encode("utf-8"), 120000
    )
    return salt, resultado.hex()


def verificar_senha(senha, salt, hash_salvo):
    _, novo_hash = hash_senha(senha, salt)
    return secrets.compare_digest(novo_hash, hash_salvo)


def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados if isinstance(dados, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def inicializar_sistema():
    """Executa a sequência visual de inicialização do SWINDLER."""
    limpar_tela()
    banner_hacker()
    mostrar_hora()
    print()
    animacao("Inicializando SWINDLER", pontos=3, velocidade=0.15)
    carregando("Carregando módulos")
    carregando("Verificando arquivos locais")
    carregando("Preparando ambiente")
    print(f"{VERDE_BRILHANTE}[✓] Sistema pronto.{RESET}")
    time.sleep(0.6)


def criar_admin_inicial():
    """Cria o administrador somente com uma chave de configuração externa."""
    usuarios = carregar_usuarios()

    if "admin" in usuarios:
        return

    chave_config = os.environ.get("SWINDLER_ADMIN_SETUP_KEY", "").strip()

    if not chave_config:
        print(f"{VERMELHO_SANGUE}[ERRO] Administrador não configurado.{RESET}")
        print(
            f"{AMARELO_ALERTA}"
            "A configuração inicial exige SWINDLER_ADMIN_SETUP_KEY."
            f"{RESET}"
        )
        return

    limpar_tela()
    banner_hacker()
    print(f"{AMARELO_ALERTA}[ CONFIGURAÇÃO ADMINISTRATIVA ]{RESET}\n")
    print(f"{CIANO}Chave de configuração necessária.{RESET}\n")

    chave = input("Chave de configuração: ").strip()

    if not secrets.compare_digest(chave, chave_config):
        registrar_log("Tentativa inválida de configuração administrativa.")
        print(f"{VERMELHO_SANGUE}Chave inválida. Configuração recusada.{RESET}")
        time.sleep(1)
        return

    while True:
        senha = input("Nova senha administrativa: ").strip()

        if len(senha) < 8:
            print(
                f"{VERMELHO_SANGUE}"
                "A senha precisa ter pelo menos 8 caracteres."
                f"{RESET}"
            )
            continue

        confirmacao = input("Confirme a senha: ").strip()

        if senha != confirmacao:
            print(f"{VERMELHO_SANGUE}As senhas não coincidem.{RESET}")
            continue

        salt, senha_hash = hash_senha(senha)

        usuarios["admin"] = {
            "tipo": "admin",
            "ativo": True,
            "salt": salt,
            "senha_hash": senha_hash,
            "criado_em": datetime.now().isoformat(),
        }

        salvar_usuarios(usuarios)
        registrar_log("Conta administrativa criada.")

        print(
            f"\n{VERDE_BRILHANTE}"
            "Administrador criado com sucesso."
            f"{RESET}"
        )
        time.sleep(1)
        break


def login_admin():
    usuarios = carregar_usuarios()
    if "admin" not in usuarios:
        return False

    print(f"{CIANO}--- LOGIN ADMINISTRATIVO ---{RESET}")
    senha = input("Senha administrativa: ")
    admin = usuarios["admin"]

    if not admin.get("ativo", False):
        print(f"{VERMELHO_SANGUE}Conta administrativa bloqueada.{RESET}")
        return False

    if verificar_senha(senha, admin["salt"], admin["senha_hash"]):
        registrar_log("Login administrativo realizado.")
        return True

    registrar_log("Falha de login administrativo.")
    print(f"{VERMELHO_SANGUE}Senha incorreta.{RESET}")
    time.sleep(1)
    return False


def admin_criar_cliente():
    usuarios = carregar_usuarios()
    print(f"{CIANO}--- CRIAR CLIENTE ---{RESET}")

    usuario = input("Nome do cliente: ").strip()
    if not usuario:
        print("Nome inválido.")
        return
    if usuario.lower() == "admin":
        print("Nome reservado.")
        return
    if usuario in usuarios:
        print(f"{AMARELO_ALERTA}Esse cliente já existe.{RESET}")
        return

    senha = input("Senha inicial do cliente: ").strip()
    if len(senha) < 6:
        print("A senha precisa ter pelo menos 6 caracteres.")
        return

    salt, senha_hash = hash_senha(senha)
    usuarios[usuario] = {
        "tipo": "cliente",
        "ativo": False,
        "salt": salt,
        "senha_hash": senha_hash,
        "criado_em": datetime.now().isoformat(),
        "ultimo_login": None
    }
    salvar_usuarios(usuarios)
    registrar_log(f"Cliente criado: {usuario}")
    print(f"{VERDE_BRILHANTE}Cliente '{usuario}' criado.{RESET}")


def admin_alterar_acesso():
    usuarios = carregar_usuarios()
    usuario = input("Cliente: ").strip()

    if usuario not in usuarios:
        print("Cliente não encontrado.")
        return
    if usuarios[usuario]["tipo"] != "cliente":
        print("Operação permitida apenas para clientes.")
        return

    atual = usuarios[usuario].get("ativo", False)
    usuarios[usuario]["ativo"] = not atual
    salvar_usuarios(usuarios)

    estado = "LIBERADO" if not atual else "BLOQUEADO"
    registrar_log(f"Acesso de {usuario}: {estado}")
    print(f"{VERDE_BRILHANTE}Acesso de {usuario}: {estado}{RESET}")


def admin_listar_clientes():
    usuarios = carregar_usuarios()
    print(f"{CIANO}--- CLIENTES ---{RESET}\n")

    encontrados = False
    for nome, dados in usuarios.items():
        if dados.get("tipo") != "cliente":
            continue
        encontrados = True
        status = (
            f"{VERDE_BRILHANTE}LIBERADO{RESET}"
            if dados.get("ativo")
            else f"{VERMELHO_SANGUE}BLOQUEADO{RESET}"
        )
        print(f"{VERDE_BRILHANTE}[>] {nome}{RESET} | {status}")

    if not encontrados:
        print("Nenhum cliente cadastrado.")


def admin_remover_cliente():
    usuarios = carregar_usuarios()
    usuario = input("Cliente para remover: ").strip()

    if usuario not in usuarios:
        print("Cliente não encontrado.")
        return
    if usuarios[usuario].get("tipo") != "cliente":
        print("Não é possível remover essa conta.")
        return

    del usuarios[usuario]
    salvar_usuarios(usuarios)
    registrar_log(f"Cliente removido: {usuario}")
    print(f"{VERDE_BRILHANTE}Cliente removido.{RESET}")


def painel_admin():
    while True:
        limpar_tela()
        banner_hacker()
        print(f"{VERMELHO_SANGUE}--- [ ÁREA ADMINISTRATIVA ] ---{RESET}\n")
        print(f"{VERDE_BRILHANTE}{1:02d}{RESET} Criar cliente")
        print(f"{VERDE_BRILHANTE}{2:02d}{RESET} Liberar/Bloquear cliente")
        print(f"{VERDE_BRILHANTE}{3:02d}{RESET} Listar clientes")
        print(f"{VERDE_BRILHANTE}{4:02d}{RESET} Remover cliente")
        print(f"{VERMELHO_SANGUE}{0:02d}{RESET} Voltar")
        linha()

        opcao = input("admin@swindler:~# ").strip()

        if opcao in ["1", "01"]:
            admin_criar_cliente()
            pausar()
        elif opcao in ["2", "02"]:
            admin_alterar_acesso()
            pausar()
        elif opcao in ["3", "03"]:
            admin_listar_clientes()
            pausar()
        elif opcao in ["4", "04"]:
            admin_remover_cliente()
            pausar()
        elif opcao in ["0", "00"]:
            break
        else:
            print("Opção inválida.")
            time.sleep(0.8)


def login_cliente():
    usuarios = carregar_usuarios()

    print(f"{CIANO}--- LOGIN CLIENTE ---{RESET}")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ")

    if usuario not in usuarios:
        print(f"{VERMELHO_SANGUE}Acesso negado.{RESET}")
        registrar_log(f"Tentativa de login inexistente: {usuario}")
        time.sleep(1)
        return False, None

    dados = usuarios[usuario]

    if dados.get("tipo") != "cliente":
        print("Essa conta não é de cliente.")
        return False, None

    if not dados.get("ativo", False):
        print(f"{VERMELHO_SANGUE}ACESSO NEGADO: cliente não autorizado.{RESET}")
        registrar_log(f"Cliente bloqueado tentou entrar: {usuario}")
        time.sleep(1)
        return False, None

    if not verificar_senha(senha, dados["salt"], dados["senha_hash"]):
        print(f"{VERMELHO_SANGUE}Senha incorreta.{RESET}")
        registrar_log(f"Senha incorreta para cliente: {usuario}")
        time.sleep(1)
        return False, None

    dados["ultimo_login"] = datetime.now().isoformat()
    salvar_usuarios(usuarios)
    registrar_log(f"Login autorizado: {usuario}")
    return True, usuario


def gerar_rg():
    return (
        f"{random.randint(10, 99)}."
        f"{random.randint(100, 999)}."
        f"{random.randint(100, 999)}-"
        f"{random.randint(0, 9)}"
    )


def gerar_cartao():
    bandeira = random.choice(["Visa", "Mastercard", "Amex", "Discover"])
    try:
        return fake.credit_card_full(
            card_type=bandeira.lower() if bandeira != "Amex" else "amex"
        )
    except Exception:
        return {
            "Cartão de teste": fake.credit_card_number(),
            "Validade": fake.credit_card_expire(),
            "Bandeira": bandeira
        }


def gerar_veiculo():
    marcas = [
        "Chevrolet", "Fiat", "Volkswagen", "Ford",
        "Toyota", "Honda", "BMW", "Audi", "Porsche"
    ]
    modelos = [
        "Onix", "Palio", "Gol", "Ka",
        "Corolla", "Civic", "320i", "A3", "911 Carrera"
    ]
    idx = random.randint(0, len(marcas) - 1)

    return {
        "Marca/Modelo": f"{marcas[idx]} {modelos[idx]}",
        "Ano/Modelo": f"{random.randint(2015, 2026)}/{random.randint(2016, 2026)}",
        "Placa Mercosul": fake.license_plate(),
        "Cor Predominante": fake.color_name().capitalize(),
        "Código Renavam": "".join(str(random.randint(0, 9)) for _ in range(11)),
        "Chassi VIN": "".join(
            random.choices(string.ascii_uppercase + string.digits, k=17)
        )
    }


def gerar_banco():
    bancos = [
        "001 - Banco do Brasil",
        "237 - Bradesco",
        "341 - Itaú Unibanco",
        "033 - Santander",
        "104 - Caixa Econômica",
        "260 - Nubank"
    ]

    return {
        "Banco Instituição": random.choice(bancos),
        "Agência Número": f"{random.randint(1000, 9999)}-{random.randint(0, 9)}",
        "Conta Corrente": f"{random.randint(10000, 99999)}-{random.randint(0, 9)}",
        "Tipo de Chave Pix": random.choice(
            ["CPF", "E-mail", "Celular", "Chave Aleatória"]
        ),
        "Saldo Inicial Simulado":
            f"R$ {random.randint(1000, 145000)},{random.randint(10, 99)}"
    }


def gerar_empresa():
    return {
        "Razão Social": fake.company(),
        "Nome Fantasia": fake.company_suffix() + " " + fake.catch_phrase(),
        "CNPJ Corporativo": CNPJ().generate(mask=True),
        "Inscrição Estadual": "".join(str(random.randint(0, 9)) for _ in range(9)),
        "Data de Abertura": (
            datetime.now() - timedelta(days=random.randint(365, 10000))
        ).strftime("%d/%m/%Y"),
        "Capital Social": f"R$ {random.randint(5000, 5000000)},00",
        "Logradouro Comercial": fake.address().replace("\n", ", ")
    }


def gerar_malware_target():
    sistemas = ["Windows 11", "Linux", "Android", "iOS"]

    return {
        "IPv4 Público Simulado": fake.ipv4_public(),
        "IPv6 Simulado": fake.ipv6(),
        "MAC Address Simulado": fake.mac_address(),
        "User-Agent": fake.user_agent(),
        "Sistema": random.choice(sistemas),
        "Portas Simuladas": ", ".join(
            str(p) for p in random.sample(
                [21, 22, 80, 443, 8080, 3306], k=4
            )
        )
    }


def mostrar_dados(dados):
    for chave, valor in dados.items():
        print(f"{VERDE_BRILHANTE} [>] {chave}:{RESET} {valor}")


def mostrar_resultado(nome, valido):
    if valido:
        print(f"{VERDE_BRILHANTE} [✓] {nome}: VÁLIDO!{RESET}")
    else:
        print(f"{VERMELHO_SANGUE} [✗] {nome}: INVÁLIDO!{RESET}")


def scanner_localhost():
    print(f"{CIANO}--- SCANNER DE PORTAS LOCAL ---{RESET}")
    print(f"{AMARELO_ALERTA}Alvo fixo: 127.0.0.1{RESET}\n")

    portas = [
        20, 21, 22, 23, 25, 53, 80, 110,
        135, 139, 143, 443, 445, 3306,
        5432, 6379, 8080, 8443
    ]

    abertas = []

    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.15)

        try:
            resultado = sock.connect_ex(("127.0.0.1", porta))
            if resultado == 0:
                abertas.append(porta)
                print(f"{VERDE_BRILHANTE}[OPEN] 127.0.0.1:{porta}{RESET}")
        except OSError:
            pass
        finally:
            sock.close()

    print()

    if abertas:
        print(
            f"{AMARELO_ALERTA}"
            f"Portas abertas: {', '.join(map(str, abertas))}"
            f"{RESET}"
        )
    else:
        print(
            f"{VERDE_BRILHANTE}"
            "Nenhuma porta da lista está aberta."
            f"{RESET}"
        )

    registrar_log(
        "Scanner localhost executado. "
        f"Abertas: {abertas}"
    )


def informacoes_rede():
    print(f"{CIANO}--- INFORMAÇÕES REAIS DO SISTEMA/REDE ---{RESET}\n")

    try:
        hostname = socket.gethostname()

        try:
            ip_local = socket.gethostbyname(hostname)
        except socket.gaierror:
            ip_local = "Não identificado"

        dados = {
            "Hostname": hostname,
            "IP local": ip_local,
            "Sistema": platform.system(),
            "Versão": platform.version(),
            "Arquitetura": platform.machine(),
            "Processador": platform.processor()
        }

        mostrar_dados(dados)

    except Exception as erro:
        print(f"{VERMELHO_SANGUE}Erro: {erro}{RESET}")


def detectar_vpn():
    print(f"{CIANO}--- STATUS VPN ---{RESET}\n")

    interfaces = []

    if os.name == "nt":
        comandos = [["ipconfig"]]
    else:
        comandos = [["ip", "addr"], ["ifconfig"]]

    saida = ""

    for comando in comandos:
        try:
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                timeout=3
            )

            if resultado.returncode == 0:
                saida += resultado.stdout + "\n"

        except (FileNotFoundError, subprocess.SubprocessError):
            continue

    nomes_vpn = ["tun", "tap", "wg", "wireguard", "ppp", "vpn"]

    for item in saida.lower().splitlines():
        if any(nome in item for nome in nomes_vpn):
            interfaces.append(item.strip())

    if interfaces:
        print(
            f"{VERDE_BRILHANTE}"
            "[✓] Possível interface VPN detectada."
            f"{RESET}\n"
        )

        for interface in interfaces[:10]:
            print(f"{VERDE_BRILHANTE}[>] {interface}{RESET}")

    else:
        print(
            f"{AMARELO_ALERTA}"
            "[!] Nenhuma interface VPN foi detectada."
            f"{RESET}"
        )

    print(
        f"\n{CIANO}"
        "O SWINDLER não inventa uma conexão VPN."
        f"{RESET}"
    )
    print(
        "Para uma VPN real, conecte-se usando "
        "uma configuração legítima do seu provedor."
    )


def gerar_senha_segura():
    tamanho_input = input("Tamanho da senha [padrão 24]: ").strip()

    try:
        tamanho = int(tamanho_input) if tamanho_input else 24
    except ValueError:
        tamanho = 24

    tamanho = max(12, min(tamanho, 128))

    caracteres = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()-_=+"
    )

    senha = "".join(
        secrets.choice(caracteres)
        for _ in range(tamanho)
    )

    print(f"\n{VERDE_BRILHANTE}[>] SENHA SEGURA: {senha}{RESET}")


def verificar_forca_senha():
    senha = input("Senha para análise: ")
    pontos = 0
    avisos = []

    if len(senha) >= 12:
        pontos += 2
    elif len(senha) >= 8:
        pontos += 1
    else:
        avisos.append("Use pelo menos 12 caracteres.")

    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        avisos.append("Adicione letras maiúsculas.")

    if any(c.islower() for c in senha):
        pontos += 1
    else:
        avisos.append("Adicione letras minúsculas.")

    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        avisos.append("Adicione números.")

    if any(c in string.punctuation for c in senha):
        pontos += 1
    else:
        avisos.append("Adicione símbolos.")

    if pontos >= 6:
        nivel = "MUITO FORTE"
    elif pontos >= 4:
        nivel = "FORTE"
    elif pontos >= 3:
        nivel = "MÉDIA"
    else:
        nivel = "FRACA"

    print(f"\n{VERDE_BRILHANTE}[>] NÍVEL: {nivel}{RESET}")

    if avisos:
        print(f"\n{AMARELO_ALERTA}Recomendações:{RESET}")
        for aviso in avisos:
            print(f"- {aviso}")


def gerar_token_laboratorio():
    token = secrets.token_urlsafe(32)

    print(f"{VERDE_BRILHANTE}[>] TOKEN DE LABORATÓRIO:{RESET}")
    print(token)
    print(
        f"\n{AMARELO_ALERTA}"
        "Token gerado localmente para testes."
        f"{RESET}"
    )


def painel_cliente(usuario):
    registrar_log(f"Cliente entrou no painel: {usuario}")

    while True:
        limpar_tela()
        banner_hacker()
        mostrar_hora()

        print(
            f"{CIANO}"
            f"--- [ PAINEL CLIENTE: {usuario} ] ---"
            f"{RESET}\n"
        )

        print(f"{CIANO}--- [ IDENTIDADES SINTÉTICAS ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{1:02d}{RESET} Identidade completa de teste")
        print(f"{VERDE_BRILHANTE}{2:02d}{RESET} CPF de teste")
        print(f"{VERDE_BRILHANTE}{3:02d}{RESET} RG simulado")
        print(f"{VERDE_BRILHANTE}{4:02d}{RESET} CNPJ de teste")
        print(f"{VERDE_BRILHANTE}{5:02d}{RESET} CNH de teste")
        print(f"{VERDE_BRILHANTE}{6:02d}{RESET} PIS/PASEP de teste")
        print(f"{VERDE_BRILHANTE}{7:02d}{RESET} Título de eleitor de teste")
        print(f"{VERDE_BRILHANTE}{8:02d}{RESET} Certidão de teste")
        print(f"{VERDE_BRILHANTE}{9:02d}{RESET} Empresa sintética")

        print()
        print(f"{CIANO}--- [ FINANCEIRO & BENS — TESTE ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{10:02d}{RESET} Cartão de teste")
        print(f"{VERDE_BRILHANTE}{11:02d}{RESET} Veículo / Renavam / Chassi simulados")
        print(f"{VERDE_BRILHANTE}{12:02d}{RESET} Conta bancária simulada")

        print()
        print(f"{CIANO}--- [ CRIPTOGRAFIA & CYBERSEC ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{13:02d}{RESET} Gerar senha")
        print(f"{VERDE_BRILHANTE}{14:02d}{RESET} Text-to-Hash")
        print(f"{VERDE_BRILHANTE}{15:02d}{RESET} Base64 Encode")
        print(f"{VERDE_BRILHANTE}{16:02d}{RESET} Base64 Decode")
        print(f"{VERDE_BRILHANTE}{17:02d}{RESET} UUID v4")
        print(f"{VERDE_BRILHANTE}{18:02d}{RESET} Ambiente de rede simulado")
        print(f"{VERDE_BRILHANTE}{19:02d}{RESET} Texto Lorem Ipsum")

        print()
        print(f"{CIANO}--- [ VALIDATION ENGINES ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{20:02d}{RESET} Validar CPF")
        print(f"{VERDE_BRILHANTE}{21:02d}{RESET} Validar CNPJ")
        print(f"{VERDE_BRILHANTE}{22:02d}{RESET} Validar CNH")
        print(f"{VERDE_BRILHANTE}{23:02d}{RESET} Validar PIS")
        print(f"{VERDE_BRILHANTE}{24:02d}{RESET} Validar Título")
        print(f"{VERDE_BRILHANTE}{25:02d}{RESET} Validar Certidão")

        print()
        print(f"{CIANO}--- [ CYBERSECURITY LAB ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{26:02d}{RESET} Scanner localhost")
        print(f"{VERDE_BRILHANTE}{27:02d}{RESET} Informações de rede")
        print(f"{VERDE_BRILHANTE}{28:02d}{RESET} Gerar senha segura")
        print(f"{VERDE_BRILHANTE}{29:02d}{RESET} Analisar senha")
        print(f"{VERDE_BRILHANTE}{30:02d}{RESET} Status VPN")
        print(f"{VERDE_BRILHANTE}{31:02d}{RESET} Token de laboratório")

        print()
        print(f"{VERMELHO_SANGUE}{{00}} ENCERRAR SESSÃO{RESET}")
        linha()

        opcao = input(
            f"{VERDE_BRILHANTE}"
            f"{usuario}@swindler:~# "
            f"{RESET}"
        ).strip()

        if opcao in ["1", "01"]:
            carregando("Gerando identidade sintética")
            p = fake.profile()
            print(f"[>] Nome: {p['name']}")
            print(f"[>] CPF de teste: {CPF().generate(mask=True)}")
            print(f"[>] RG simulado: {gerar_rg()}")
            print(f"[>] Nascimento: {p['birthdate'].strftime('%d/%m/%Y')}")
            print(f"[>] Email: {p['mail']}")
            print(f"[>] Telefone: {fake.cellphone_number()}")
            print(f"[>] Endereço: {p['address'].replace(chr(10), ', ')}")
            pausar()

        elif opcao in ["2", "02"]:
            carregando("Gerando CPF de teste")
            print(f"[>] CPF: {CPF().generate(mask=True)}")
            pausar()

        elif opcao in ["3", "03"]:
            print(f"[>] RG SIMULADO: {gerar_rg()}")
            pausar()

        elif opcao in ["4", "04"]:
            print(f"[>] CNPJ DE TESTE: {CNPJ().generate(mask=True)}")
            pausar()

        elif opcao in ["5", "05"]:
            print(f"[>] CNH DE TESTE: {CNH().generate()}")
            pausar()

        elif opcao in ["6", "06"]:
            print(f"[>] PIS DE TESTE: {PIS().generate(mask=True)}")
            pausar()

        elif opcao in ["7", "07"]:
            print(f"[>] TÍTULO DE TESTE: {TituloEleitoral().generate(mask=True)}")
            pausar()

        elif opcao in ["8", "08"]:
            print(f"[>] CERTIDÃO DE TESTE: {Certidao().generate(mask=True)}")
            pausar()

        elif opcao in ["9", "09"]:
            mostrar_dados(gerar_empresa())
            pausar()

        elif opcao == "10":
            print(f"{AMARELO_ALERTA}[!] DADOS SOMENTE PARA TESTE{RESET}\n")
            resultado = gerar_cartao()
            if isinstance(resultado, dict):
                mostrar_dados(resultado)
            else:
                print(resultado)
            pausar()

        elif opcao == "11":
            mostrar_dados(gerar_veiculo())
            pausar()

        elif opcao == "12":
            print(f"{AMARELO_ALERTA}[!] CONTA TOTALMENTE SIMULADA{RESET}\n")
            mostrar_dados(gerar_banco())
            pausar()

        elif opcao == "13":
            gerar_senha_segura()
            pausar()

        elif opcao == "14":
            texto = input("String para hash: ")
            print(f"[>] MD5: {hashlib.md5(texto.encode()).hexdigest()}")
            print(f"[>] SHA256: {hashlib.sha256(texto.encode()).hexdigest()}")
            print(f"[>] SHA512: {hashlib.sha512(texto.encode()).hexdigest()}")
            pausar()

        elif opcao == "15":
            texto = input("Texto: ")
            resultado = base64.b64encode(texto.encode()).decode()
            print(f"[>] BASE64: {resultado}")
            pausar()

        elif opcao == "16":
            texto = input("Base64: ")
            try:
                resultado = base64.b64decode(texto, validate=True).decode()
                print(f"[>] ORIGINAL: {resultado}")
            except (ValueError, UnicodeDecodeError):
                print(f"{VERMELHO_SANGUE}Base64 inválido.{RESET}")
            pausar()

        elif opcao == "17":
            print(f"[>] UUIDv4: {uuid.uuid4()}")
            pausar()

        elif opcao == "18":
            print(f"{AMARELO_ALERTA}[!] AMBIENTE SIMULADO{RESET}\n")
            mostrar_dados(gerar_malware_target())
            pausar()

        elif opcao == "19":
            print(fake.text(max_nb_chars=600))
            pausar()

        elif opcao == "20":
            doc = input("CPF: ")
            mostrar_resultado("CPF", CPF().validate(doc))
            pausar()

        elif opcao == "21":
            doc = input("CNPJ: ")
            mostrar_resultado("CNPJ", CNPJ().validate(doc))
            pausar()

        elif opcao == "22":
            doc = input("CNH: ")
            mostrar_resultado("CNH", CNH().validate(doc))
            pausar()

        elif opcao == "23":
            doc = input("PIS: ")
            mostrar_resultado("PIS", PIS().validate(doc))
            pausar()

        elif opcao == "24":
            doc = input("Título: ")
            mostrar_resultado("Título", TituloEleitoral().validate(doc))
            pausar()

        elif opcao == "25":
            doc = input("Certidão: ")
            mostrar_resultado("Certidão", Certidao().validate(doc))
            pausar()

        elif opcao == "26":
            scanner_localhost()
            pausar()

        elif opcao == "27":
            informacoes_rede()
            pausar()

        elif opcao == "28":
            gerar_senha_segura()
            pausar()

        elif opcao == "29":
            verificar_forca_senha()
            pausar()

        elif opcao == "30":
            detectar_vpn()
            pausar()

        elif opcao == "31":
            gerar_token_laboratorio()
            pausar()

        elif opcao in ["0", "00"]:
            registrar_log(f"Cliente encerrou sessão: {usuario}")
            break

        else:
            print(f"{VERMELHO_SANGUE}Opção inválida.{RESET}")
            time.sleep(0.8)

    registrar_log(f"Cliente saiu do painel: {usuario}")


def menu_principal():
    while True:
        limpar_tela()
        banner_hacker()
        mostrar_hora()

        print()
        print(f"{CIANO}--- [ CONTROLE DE ACESSO ] ---{RESET}")
        print(f"{VERDE_BRILHANTE}{{01}}{RESET} Login Administrativo")
        print(f"{VERDE_BRILHANTE}{{02}}{RESET} Login Cliente")
        print(f"{VERMELHO_SANGUE}{{00}}{RESET} Sair")
        linha()

        opcao = input(
            f"{VERDE_BRILHANTE}"
            "swindler@auth:~# "
            f"{RESET}"
        ).strip()

        if opcao in ["1", "01"]:
            limpar_tela()
            banner_hacker()
            if login_admin():
                time.sleep(0.5)
                painel_admin()

        elif opcao in ["2", "02"]:
            limpar_tela()
            banner_hacker()
            autorizado, usuario = login_cliente()
            if autorizado:
                time.sleep(0.5)
                painel_cliente(usuario)

        elif opcao in ["0", "00"]:
            animacao("Encerrando SWINDLER", pontos=3)
            registrar_log("Programa encerrado.")
            print(
                f"{VERMELHO_SANGUE}"
                "\n[!] SISTEMA ENCERRADO."
                f"{RESET}\n"
            )
            break

        else:
            print(f"{VERMELHO_SANGUE}Opção inválida.{RESET}")
            time.sleep(0.8)


def main():
    try:
        inicializar_sistema()
        criar_admin_inicial()
        menu_principal()
    except KeyboardInterrupt:
        print(
            f"\n{VERMELHO_SANGUE}"
            "[!] Execução interrompida."
            f"{RESET}"
        )
    except Exception as erro:
        print(
            f"\n{VERMELHO_SANGUE}"
            f"[ERRO] {erro}"
            f"{RESET}"
        )
        registrar_log(f"Erro não tratado: {erro}")


if __name__ == "__main__":
    main()
