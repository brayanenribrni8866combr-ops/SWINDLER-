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
import shutil
import re
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
ARQUIVO_TICKETS = os.path.join(BASE_DIR, "swindler_tickets.json")
ARQUIVO_CONFIG = os.path.join(BASE_DIR, "swindler_config.json")



# =========================
# CAMADA VISUAL / CORPORATIVA
# =========================

NEGRITO = "\033[1m"
DIM = "\033[2m"
RESET_VISUAL = "\033[0m"

def titulo_secao(titulo, subtitulo=None):
    print()
    print(f"{VERMELHO_SANGUE}{'═' * 72}{RESET}")
    print(f"{NEGRITO}{CIANO}  {titulo.upper()}{RESET}")
    if subtitulo:
        print(f"{DIM}  {subtitulo}{RESET_VISUAL}")
    print(f"{VERMELHO_SANGUE}{'═' * 72}{RESET}")

def menu_item(numero, texto, destaque=False):
    cor = AMARELO_ALERTA if destaque else VERDE_BRILHANTE
    print(f"{cor}  {numero:>2}{RESET}  {NEGRITO if destaque else ''}{texto}{RESET_VISUAL}")

def painel_status(tag, valor):
    print(f"  {CIANO}{tag:<22}{RESET}: {valor}")

def banner_profissional():
    limpar_tela()
    print(f"{VERMELHO_SANGUE}{'█' * 72}{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}███████╗██╗    ██╗██╗███╗   ██╗██████╗ ██╗     ███████╗██████╗{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}██╔════╝██║    ██║██║████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}███████╗██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}╚════██║██║███╗██║██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}███████║╚███╔███╔╝██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║{RESET}")
    print(f"{VERMELHO_SANGUE}██{RESET}  {NEGRITO}{CIANO}╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝{RESET}")
    print(f"{VERMELHO_SANGUE}{'█' * 72}{RESET}")
    print(f"{AMARELO_ALERTA}{NEGRITO}             SWINDLER • CORPORATE SECURITY LAB{RESET}")
    print(f"{DIM}             LOCAL / EDUCATIONAL / CONTROLLED ENVIRONMENT{RESET_VISUAL}")
    print()

def util_informacoes_sistema():
    titulo_secao("Diagnóstico do sistema", "Informações somente de leitura")
    try:
        total, usado, livre = shutil.disk_usage(BASE_DIR)
        print(f"  Sistema        : {platform.system()} {platform.release()}")
        print(f"  Arquitetura    : {platform.machine()}")
        print(f"  Python         : {platform.python_version()}")
        print(f"  Hostname       : {socket.gethostname()}")
        print(f"  CPU            : {os.cpu_count() or 'N/D'} núcleos")
        print(f"  Diretório      : {BASE_DIR}")
        print(f"  Disco total    : {total // (1024**3)} GB")
        print(f"  Disco livre    : {livre // (1024**3)} GB")
    except OSError as erro:
        print(f"{VERMELHO_SANGUE}Falha no diagnóstico: {erro}{RESET}")
    pausar()

def util_estatisticas_texto():
    titulo_secao("Analisador de texto")
    texto = input("Cole o texto (uma linha): ")
    palavras = texto.split()
    print(f"\n  Caracteres     : {len(texto)}")
    print(f"  Sem espaços    : {len(''.join(texto.split()))}")
    print(f"  Palavras       : {len(palavras)}")
    print(f"  Linhas         : 1")
    print(f"  Maiúsculas     : {sum(c.isupper() for c in texto)}")
    print(f"  Minúsculas     : {sum(c.islower() for c in texto)}")
    pausar()

def util_hash_texto():
    titulo_secao("Hash múltiplo de texto")
    texto = input("Texto: ").encode("utf-8")
    print(f"  MD5     : {hashlib.md5(texto).hexdigest()}")
    print(f"  SHA1    : {hashlib.sha1(texto).hexdigest()}")
    print(f"  SHA256  : {hashlib.sha256(texto).hexdigest()}")
    print(f"  SHA512  : {hashlib.sha512(texto).hexdigest()}")
    pausar()

def util_hex_aleatorio():
    titulo_secao("Gerador hexadecimal")
    try:
        tamanho = int(input("Quantidade de bytes [16]: ") or "16")
        tamanho = max(1, min(tamanho, 128))
    except ValueError:
        tamanho = 16
    print(f"\n  HEX: {secrets.token_hex(tamanho)}")
    pausar()

def util_timestamp():
    titulo_secao("Timestamp")
    agora = datetime.now()
    print(f"  Data local     : {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"  ISO 8601       : {agora.isoformat()}")
    print(f"  Unix timestamp : {int(agora.timestamp())}")
    pausar()

def util_base64_arquivo_local():
    titulo_secao("Base64 de arquivo local")
    caminho = input("Caminho do arquivo: ").strip()
    if not caminho:
        return
    caminho = os.path.abspath(caminho)
    if not os.path.isfile(caminho):
        print(f"{VERMELHO_SANGUE}Arquivo não encontrado.{RESET}")
        pausar()
        return
    try:
        with open(caminho, "rb") as arquivo:
            dados = base64.b64encode(arquivo.read()).decode("ascii")
        print(f"  Arquivo : {os.path.basename(caminho)}")
        print(f"  Base64  : {dados[:1000]}{'...' if len(dados) > 1000 else ''}")
        print(f"  Tamanho : {len(dados)} caracteres")
    except OSError as erro:
        print(f"{VERMELHO_SANGUE}Erro: {erro}{RESET}")
    pausar()

def util_porta_local():
    titulo_secao("Teste de porta local", "Restrito a 127.0.0.1")
    try:
        porta = int(input("Porta [80]: ") or "80")
        if not 1 <= porta <= 65535:
            raise ValueError
    except ValueError:
        print(f"{VERMELHO_SANGUE}Porta inválida.{RESET}")
        pausar()
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        resultado = sock.connect_ex(("127.0.0.1", porta))
        estado = "ABERTA / ACESSÍVEL" if resultado == 0 else "FECHADA / NÃO ACESSÍVEL"
        print(f"  127.0.0.1:{porta} -> {estado}")
    finally:
        sock.close()
    pausar()

def util_calculadora():
    titulo_secao("Calculadora")
    expressao = input("Expressão simples (ex.: 25*4+10): ").strip()
    # Calculadora deliberadamente limitada a números e operadores básicos.
    if not re.fullmatch(r"[0-9+\-*/(). %]+", expressao):
        print(f"{VERMELHO_SANGUE}Expressão contém caracteres não permitidos.{RESET}")
        pausar()
        return
    try:
        resultado = eval(expressao, {"__builtins__": {}}, {})
        print(f"  Resultado: {resultado}")
    except Exception:
        print(f"{VERMELHO_SANGUE}Não foi possível calcular.{RESET}")
    pausar()

def util_json_formatador():
    titulo_secao("Formatador JSON")
    bruto = input("JSON: ").strip()
    try:
        objeto = json.loads(bruto)
        print(json.dumps(objeto, indent=4, ensure_ascii=False))
    except json.JSONDecodeError as erro:
        print(f"{VERMELHO_SANGUE}JSON inválido: {erro}{RESET}")
    pausar()

def painel_utilidades():
    while True:
        banner_profissional()
        titulo_secao("Central de utilidades")
        menu_item(1, "Diagnóstico do sistema")
        menu_item(2, "Analisador de texto")
        menu_item(3, "Hash múltiplo")
        menu_item(4, "Gerar hexadecimal aleatório")
        menu_item(5, "Data / hora / timestamp")
        menu_item(6, "Base64 de arquivo local")
        menu_item(7, "Teste de porta localhost")
        menu_item(8, "Calculadora")
        menu_item(9, "Formatador JSON")
        menu_item(0, "Voltar", destaque=True)
        linha()
        opcao = input("utils@swindler:~# ").strip()
        if opcao in ("1", "01"): util_informacoes_sistema()
        elif opcao in ("2", "02"): util_estatisticas_texto()
        elif opcao in ("3", "03"): util_hash_texto()
        elif opcao in ("4", "04"): util_hex_aleatorio()
        elif opcao in ("5", "05"): util_timestamp()
        elif opcao in ("6", "06"): util_base64_arquivo_local()
        elif opcao in ("7", "07"): util_porta_local()
        elif opcao in ("8", "08"): util_calculadora()
        elif opcao in ("9", "09"): util_json_formatador()
        elif opcao in ("0", "00"): break
        else:
            print(f"{VERMELHO_SANGUE}Opção inválida.{RESET}")
            time.sleep(0.6)


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
    banner_profissional()


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


def criar_admin_inicial():
    usuarios = carregar_usuarios()
    if "admin" in usuarios:
        return

    limpar_tela()
    banner_hacker()
    print(f"{AMARELO_ALERTA}[ PRIMEIRA EXECUÇÃO ]{RESET}\n")
    print(f"{CIANO}Crie a senha da conta administrativa.{RESET}\n")

    while True:
        senha = input("Nova senha administrativa: ").strip()
        if len(senha) < 8:
            print(f"{VERMELHO_SANGUE}A senha precisa ter pelo menos 8 caracteres.{RESET}")
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
            "criado_em": datetime.now().isoformat()
        }
        salvar_usuarios(usuarios)
        registrar_log("Conta administrativa criada.")
        print(f"\n{VERDE_BRILHANTE}Administrador criado com sucesso.{RESET}")
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
        "status": "pendente",
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



def carregar_json_seguro(caminho, padrao):
    if not os.path.exists(caminho):
        return padrao
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    except (json.JSONDecodeError, OSError):
        return padrao


def salvar_json_seguro(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_tickets():
    return carregar_json_seguro(ARQUIVO_TICKETS, [])


def salvar_tickets(tickets):
    salvar_json_seguro(ARQUIVO_TICKETS, tickets)


def proximo_ticket_id(tickets):
    if not tickets:
        return 1
    return max(int(t.get("id", 0)) for t in tickets) + 1


def dashboard_admin():
    usuarios = carregar_usuarios()
    tickets = carregar_tickets()

    clientes = [u for u, d in usuarios.items() if d.get("tipo") == "cliente"]
    funcionarios = [u for u, d in usuarios.items() if d.get("tipo") == "funcionario"]
    pendentes = [u for u in clientes if usuarios[u].get("status", "aprovado") == "pendente"]
    ativos = [u for u in clientes if usuarios[u].get("ativo", False)]
    abertos = [t for t in tickets if t.get("status") != "encerrado"]

    print(f"{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CIANO}║                 SWINDLER CORPORATE DASHBOARD                    ║{RESET}")
    print(f"{CIANO}╠════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CIANO}║ Sistema.............. {VERDE_BRILHANTE}ONLINE{RESET}")
    print(f"{CIANO}║ Clientes............. {len(clientes):<5}  Aprovados ativos: {len(ativos):<5}       ║{RESET}")
    print(f"{CIANO}║ Funcionários......... {len(funcionarios):<5}  Pendências: {len(pendentes):<5}              ║{RESET}")
    print(f"{CIANO}║ Chamados em aberto... {len(abertos):<5}  Logs: {'ATIVO':<8}                 ║{RESET}")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")


def admin_cadastrar_funcionario():
    usuarios = carregar_usuarios()
    print(f"{CIANO}--- CADASTRAR FUNCIONÁRIO ---{RESET}")

    usuario = input("Usuário do funcionário: ").strip()
    if not usuario or usuario.lower() == "admin":
        print("Usuário inválido ou reservado.")
        return
    if usuario in usuarios:
        print("Esse usuário já existe.")
        return

    senha = input("Senha inicial: ").strip()
    if len(senha) < 6:
        print("A senha precisa ter pelo menos 6 caracteres.")
        return

    departamentos = ["ADMINISTRAÇÃO", "SUPORTE", "ATENDIMENTO", "SEGURANÇA", "MANUTENÇÃO"]
    print("Departamentos:", ", ".join(departamentos))
    departamento = input("Departamento: ").strip().upper()
    if departamento not in departamentos:
        print("Departamento inválido.")
        return

    salt, senha_hash = hash_senha(senha)
    usuarios[usuario] = {
        "tipo": "funcionario",
        "ativo": True,
        "salt": salt,
        "senha_hash": senha_hash,
        "departamento": departamento,
        "criado_em": datetime.now().isoformat(),
        "ultimo_login": None,
    }
    salvar_usuarios(usuarios)
    registrar_log(f"Funcionário criado: {usuario} ({departamento})")
    print(f"{VERDE_BRILHANTE}Funcionário criado com sucesso.{RESET}")


def admin_listar_funcionarios():
    usuarios = carregar_usuarios()
    print(f"{CIANO}--- FUNCIONÁRIOS ---{RESET}\n")
    encontrou = False

    for nome, dados in usuarios.items():
        if dados.get("tipo") != "funcionario":
            continue
        encontrou = True
        status = "ATIVO" if dados.get("ativo") else "BLOQUEADO"
        print(
            f"{VERDE_BRILHANTE}{nome}{RESET} | "
            f"{dados.get('departamento', 'N/D')} | {status}"
        )

    if not encontrou:
        print("Nenhum funcionário cadastrado.")


def admin_alterar_status_funcionario():
    usuarios = carregar_usuarios()
    usuario = input("Funcionário: ").strip()

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "funcionario":
        print("Funcionário não encontrado.")
        return

    dados["ativo"] = not dados.get("ativo", False)
    salvar_usuarios(usuarios)
    estado = "ATIVO" if dados["ativo"] else "BLOQUEADO"
    registrar_log(f"Funcionário {usuario}: {estado}")
    print(f"{VERDE_BRILHANTE}{usuario}: {estado}{RESET}")


def admin_remover_funcionario():
    usuarios = carregar_usuarios()
    usuario = input("Funcionário para remover: ").strip()

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "funcionario":
        print("Funcionário não encontrado.")
        return

    del usuarios[usuario]
    salvar_usuarios(usuarios)
    registrar_log(f"Funcionário removido: {usuario}")
    print(f"{VERDE_BRILHANTE}Funcionário removido.{RESET}")


def admin_aprovar_cliente():
    usuarios = carregar_usuarios()
    usuario = input("Cliente pendente: ").strip()

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "cliente":
        print("Cliente não encontrado.")
        return

    dados["status"] = "aprovado"
    dados["ativo"] = True
    salvar_usuarios(usuarios)
    registrar_log(f"Cliente aprovado: {usuario}")
    print(f"{VERDE_BRILHANTE}Cliente aprovado e liberado.{RESET}")


def admin_reprovar_cliente():
    usuarios = carregar_usuarios()
    usuario = input("Cliente para reprovar: ").strip()

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "cliente":
        print("Cliente não encontrado.")
        return

    dados["status"] = "reprovado"
    dados["ativo"] = False
    salvar_usuarios(usuarios)
    registrar_log(f"Cliente reprovado: {usuario}")
    print(f"{AMARELO_ALERTA}Cliente reprovado e bloqueado.{RESET}")


def admin_redefinir_senha_cliente():
    usuarios = carregar_usuarios()
    usuario = input("Cliente: ").strip()

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "cliente":
        print("Cliente não encontrado.")
        return

    nova = input("Nova senha: ").strip()
    if len(nova) < 6:
        print("A senha precisa ter pelo menos 6 caracteres.")
        return

    confirmacao = input("Confirme a nova senha: ").strip()
    if nova != confirmacao:
        print("As senhas não coincidem.")
        return

    salt, senha_hash = hash_senha(nova)
    dados["salt"] = salt
    dados["senha_hash"] = senha_hash
    salvar_usuarios(usuarios)
    registrar_log(f"Senha de cliente redefinida: {usuario}")
    print(f"{VERDE_BRILHANTE}Senha redefinida com sucesso.{RESET}")


def admin_alterar_senha():
    usuarios = carregar_usuarios()
    admin = usuarios.get("admin")

    if not admin:
        print("Conta administrativa inexistente.")
        return

    atual = input("Senha administrativa atual: ")
    if not verificar_senha(atual, admin["salt"], admin["senha_hash"]):
        registrar_log("Falha ao alterar senha administrativa.")
        print(f"{VERMELHO_SANGUE}Senha atual incorreta.{RESET}")
        return

    nova = input("Nova senha: ").strip()
    if len(nova) < 8:
        print("A nova senha precisa ter pelo menos 8 caracteres.")
        return

    confirmacao = input("Confirme a nova senha: ").strip()
    if nova != confirmacao:
        print("As senhas não coincidem.")
        return

    salt, senha_hash = hash_senha(nova)
    admin["salt"] = salt
    admin["senha_hash"] = senha_hash
    salvar_usuarios(usuarios)
    registrar_log("Senha administrativa alterada.")
    print(f"{VERDE_BRILHANTE}Senha administrativa alterada.{RESET}")


def criar_chamado(usuario):
    tickets = carregar_tickets()
    assunto = input("Assunto: ").strip()
    mensagem = input("Descreva o problema: ").strip()

    if not assunto or not mensagem:
        print("Assunto e mensagem são obrigatórios.")
        return

    ticket = {
        "id": proximo_ticket_id(tickets),
        "cliente": usuario,
        "assunto": assunto,
        "mensagem": mensagem,
        "status": "aberto",
        "responsavel": None,
        "resposta": None,
        "criado_em": datetime.now().isoformat(),
        "atualizado_em": datetime.now().isoformat(),
    }

    tickets.append(ticket)
    salvar_tickets(tickets)
    registrar_log(f"Chamado #{ticket['id']} aberto por {usuario}")
    print(f"{VERDE_BRILHANTE}Chamado #{ticket['id']} criado.{RESET}")


def cliente_meus_chamados(usuario):
    tickets = carregar_tickets()
    meus = [t for t in tickets if t.get("cliente") == usuario]

    print(f"{CIANO}--- MEUS CHAMADOS ---{RESET}\n")
    if not meus:
        print("Você não possui chamados.")
        return

    for t in meus:
        print(
            f"#{t['id']} | {t['assunto']} | "
            f"{t['status'].upper()} | Responsável: {t.get('responsavel') or 'Não atribuído'}"
        )
        if t.get("resposta"):
            print(f"  Resposta: {t['resposta']}")
        print()


def suporte_listar_chamados():
    tickets = carregar_tickets()
    print(f"{CIANO}--- CENTRAL DE SUPORTE ---{RESET}\n")

    if not tickets:
        print("Nenhum chamado registrado.")
        return

    for t in tickets:
        print(
            f"#{t['id']} | Cliente: {t['cliente']} | "
            f"{t['status'].upper()} | {t['assunto']} | "
            f"Responsável: {t.get('responsavel') or 'N/D'}"
        )


def suporte_atender_chamado(funcionario):
    tickets = carregar_tickets()
    try:
        numero = int(input("Número do chamado: ").strip())
    except ValueError:
        print("Número inválido.")
        return

    chamado = next((t for t in tickets if int(t.get("id", 0)) == numero), None)
    if not chamado:
        print("Chamado não encontrado.")
        return

    resposta = input("Resposta ao cliente: ").strip()
    if not resposta:
        print("A resposta não pode ficar vazia.")
        return

    chamado["responsavel"] = funcionario
    chamado["resposta"] = resposta
    chamado["status"] = "em_atendimento"
    chamado["atualizado_em"] = datetime.now().isoformat()
    salvar_tickets(tickets)
    registrar_log(f"Funcionário {funcionario} respondeu ao chamado #{numero}")
    print(f"{VERDE_BRILHANTE}Chamado atualizado.{RESET}")


def suporte_encerrar_chamado(funcionario):
    tickets = carregar_tickets()
    try:
        numero = int(input("Número do chamado: ").strip())
    except ValueError:
        print("Número inválido.")
        return

    chamado = next((t for t in tickets if int(t.get("id", 0)) == numero), None)
    if not chamado:
        print("Chamado não encontrado.")
        return

    chamado["responsavel"] = funcionario
    chamado["status"] = "encerrado"
    chamado["atualizado_em"] = datetime.now().isoformat()
    salvar_tickets(tickets)
    registrar_log(f"Funcionário {funcionario} encerrou o chamado #{numero}")
    print(f"{VERDE_BRILHANTE}Chamado encerrado.{RESET}")


def painel_suporte(funcionario):
    while True:
        limpar_tela()
        banner_hacker()
        print(f"{CIANO}--- CENTRAL DE SUPORTE | {funcionario} ---{RESET}\n")
        print(f"{VERDE_BRILHANTE}01{RESET} Ver chamados")
        print(f"{VERDE_BRILHANTE}02{RESET} Responder chamado")
        print(f"{VERDE_BRILHANTE}03{RESET} Encerrar chamado")
        print(f"{VERMELHO_SANGUE}00{RESET} Voltar")
        linha()

        opcao = input("suporte@swindler:~# ").strip()

        if opcao in ("1", "01"):
            suporte_listar_chamados()
            pausar()
        elif opcao in ("2", "02"):
            suporte_atender_chamado(funcionario)
            pausar()
        elif opcao in ("3", "03"):
            suporte_encerrar_chamado(funcionario)
            pausar()
        elif opcao in ("0", "00"):
            break
        else:
            print("Opção inválida.")
            time.sleep(0.8)


def painel_funcionario(usuario):
    usuarios = carregar_usuarios()
    departamento = usuarios.get(usuario, {}).get("departamento", "N/D")

    while True:
        limpar_tela()
        banner_hacker()
        mostrar_hora()
        print(f"{CIANO}--- [ PAINEL FUNCIONÁRIO ] ---{RESET}")
        print(f"Usuário: {usuario}")
        print(f"Departamento: {departamento}\n")

        print(f"{VERDE_BRILHANTE}01{RESET} Central de suporte")
        print(f"{VERDE_BRILHANTE}02{RESET} Meu status")
        print(f"{VERDE_BRILHANTE}03{RESET} Alterar minha senha")
        print(f"{VERMELHO_SANGUE}00{RESET} Encerrar sessão")
        linha()

        opcao = input("funcionario@swindler:~# ").strip()

        if opcao in ("1", "01"):
            painel_suporte(usuario)
        elif opcao in ("2", "02"):
            print(f"{VERDE_BRILHANTE}Conta ativa.{RESET}")
            print(f"Departamento: {departamento}")
            pausar()
        elif opcao in ("3", "03"):
            usuarios = carregar_usuarios()
            atual = input("Senha atual: ")
            dados = usuarios.get(usuario)
            if dados and verificar_senha(atual, dados["salt"], dados["senha_hash"]):
                nova = input("Nova senha: ").strip()
                if len(nova) >= 6 and nova == input("Confirme: ").strip():
                    salt, senha_hash = hash_senha(nova)
                    dados["salt"] = salt
                    dados["senha_hash"] = senha_hash
                    salvar_usuarios(usuarios)
                    registrar_log(f"Funcionário {usuario} alterou a própria senha.")
                    print("Senha alterada.")
                else:
                    print("Senha inválida ou confirmação diferente.")
            else:
                print("Senha atual incorreta.")
            pausar()
        elif opcao in ("0", "00"):
            registrar_log(f"Funcionário encerrou sessão: {usuario}")
            break
        else:
            print("Opção inválida.")
            time.sleep(0.8)


def login_funcionario():
    usuarios = carregar_usuarios()

    print(f"{CIANO}--- LOGIN FUNCIONÁRIO ---{RESET}")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ")

    dados = usuarios.get(usuario)
    if not dados or dados.get("tipo") != "funcionario":
        print(f"{VERMELHO_SANGUE}Acesso negado.{RESET}")
        return False, None

    if not dados.get("ativo", False):
        print(f"{VERMELHO_SANGUE}Funcionário bloqueado.{RESET}")
        return False, None

    if not verificar_senha(senha, dados["salt"], dados["senha_hash"]):
        print(f"{VERMELHO_SANGUE}Senha incorreta.{RESET}")
        registrar_log(f"Falha de login de funcionário: {usuario}")
        return False, None

    dados["ultimo_login"] = datetime.now().isoformat()
    salvar_usuarios(usuarios)
    registrar_log(f"Login de funcionário: {usuario}")
    return True, usuario


def admin_logs():
    print(f"{CIANO}--- AUDITORIA E LOGS ---{RESET}\n")
    if not os.path.exists(ARQUIVO_LOG):
        print("Nenhum log registrado.")
        return

    try:
        with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        for linha_log in linhas[-40:]:
            print(linha_log.rstrip())
    except OSError as erro:
        print(f"Erro ao ler logs: {erro}")


def admin_backup_banco():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = os.path.join(BASE_DIR, f"swindler_users_backup_{timestamp}.json")

    try:
        shutil.copy2(ARQUIVO_USUARIOS, destino)
        registrar_log(f"Backup do banco criado: {os.path.basename(destino)}")
        print(f"{VERDE_BRILHANTE}Backup criado: {os.path.basename(destino)}{RESET}")
    except (OSError, shutil.Error) as erro:
        print(f"{VERMELHO_SANGUE}Falha no backup: {erro}{RESET}")


def admin_manutencao():
    config = carregar_json_seguro(ARQUIVO_CONFIG, {"manutencao": False})
    estado = config.get("manutencao", False)

    print(f"{CIANO}--- MANUTENÇÃO DO SISTEMA ---{RESET}\n")
    print(f"Estado atual: {'ATIVO' if estado else 'DESATIVADO'}")
    print("01 Ativar/desativar manutenção")
    print("00 Voltar")

    opcao = input("manutencao@swindler:~# ").strip()
    if opcao in ("1", "01"):
        config["manutencao"] = not estado
        salvar_json_seguro(ARQUIVO_CONFIG, config)
        registrar_log(
            f"Modo manutenção: {'ATIVO' if config['manutencao'] else 'DESATIVADO'}"
        )
        print("Estado atualizado.")


def painel_gestao_clientes():
    while True:
        limpar_tela()
        banner_hacker()
        print(f"{CIANO}--- GESTÃO DE CLIENTES ---{RESET}\n")
        print("01 Solicitações pendentes")
        print("02 Aprovar cliente")
        print("03 Reprovar cliente")
        print("04 Liberar/bloquear cliente")
        print("05 Alterar senha do cliente")
        print("06 Excluir cliente")
        print("07 Listar clientes")
        print("00 Voltar")
        linha()

        opcao = input("clientes@swindler:~# ").strip()

        if opcao in ("1", "01"):
            usuarios = carregar_usuarios()
            pendentes = [
                n for n, d in usuarios.items()
                if d.get("tipo") == "cliente" and d.get("status") == "pendente"
            ]
            print("Pendentes:", ", ".join(pendentes) if pendentes else "nenhum")
            pausar()
        elif opcao in ("2", "02"):
            admin_aprovar_cliente()
            pausar()
        elif opcao in ("3", "03"):
            admin_reprovar_cliente()
            pausar()
        elif opcao in ("4", "04"):
            admin_alterar_acesso()
            pausar()
        elif opcao in ("5", "05"):
            admin_redefinir_senha_cliente()
            pausar()
        elif opcao in ("6", "06"):
            admin_remover_cliente()
            pausar()
        elif opcao in ("7", "07"):
            admin_listar_clientes()
            pausar()
        elif opcao in ("0", "00"):
            break
        else:
            print("Opção inválida.")
            time.sleep(0.8)


def painel_funcionarios_admin():
    while True:
        limpar_tela()
        banner_hacker()
        print(f"{CIANO}--- GESTÃO DE FUNCIONÁRIOS ---{RESET}\n")
        print("01 Cadastrar funcionário")
        print("02 Listar funcionários")
        print("03 Ativar/bloquear funcionário")
        print("04 Excluir funcionário")
        print("00 Voltar")
        linha()

        opcao = input("funcionarios@swindler:~# ").strip()

        if opcao in ("1", "01"):
            admin_cadastrar_funcionario()
            pausar()
        elif opcao in ("2", "02"):
            admin_listar_funcionarios()
            pausar()
        elif opcao in ("3", "03"):
            admin_alterar_status_funcionario()
            pausar()
        elif opcao in ("4", "04"):
            admin_remover_funcionario()
            pausar()
        elif opcao in ("0", "00"):
            break
        else:
            print("Opção inválida.")
            time.sleep(0.8)



def painel_admin():
    while True:
        banner_profissional()
        mostrar_hora()
        titulo_secao("Painel administrativo", "Acesso integral do administrador")
        usuarios = carregar_usuarios()
        clientes = sum(1 for d in usuarios.values() if d.get("tipo") == "cliente")
        funcionarios = sum(1 for d in usuarios.values() if d.get("tipo") == "funcionario")
        pendentes = sum(
            1 for d in usuarios.values()
            if d.get("tipo") == "cliente" and d.get("status") == "pendente"
        )
        painel_status("Clientes", clientes)
        painel_status("Funcionários", funcionarios)
        painel_status("Pendências", pendentes)
        print()
        menu_item(1, "Dashboard / visão geral")
        menu_item(2, "Gestão de funcionários")
        menu_item(3, "Gestão de clientes / aprovações")
        menu_item(4, "Central de suporte")
        menu_item(5, "Alterar senha administrativa")
        menu_item(6, "Auditoria e logs")
        menu_item(7, "Backup do banco")
        menu_item(8, "Manutenção do sistema")
        menu_item(9, "Laboratório SWINDLER — acesso integral")
        menu_item(10, "Central de utilidades avançadas")
        menu_item(0, "Encerrar sessão", destaque=True)
        linha()

        opcao = input("admin@swindler:~# ").strip()
        if opcao in ("1", "01"):
            limpar_tela()
            dashboard_admin()
            pausar()
        elif opcao in ("2", "02"):
            painel_funcionarios_admin()
        elif opcao in ("3", "03"):
            painel_gestao_clientes()
        elif opcao in ("4", "04"):
            painel_suporte("ADMIN")
        elif opcao in ("5", "05"):
            admin_alterar_senha()
            pausar()
        elif opcao in ("6", "06"):
            admin_logs()
            pausar()
        elif opcao in ("7", "07"):
            admin_backup_banco()
            pausar()
        elif opcao in ("8", "08"):
            admin_manutencao()
            pausar()
        elif opcao in ("9", "09"):
            painel_cliente("ADMIN")
        elif opcao in ("10", "010"):
            painel_utilidades()
        elif opcao in ("0", "00"):
            registrar_log("Administrador encerrou sessão.")
            break
        else:
            print(f"{VERMELHO_SANGUE}Opção inválida.{RESET}")
            time.sleep(0.6)


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
        print(f"{VERDE_BRILHANTE}{32:02d}{RESET} Central de suporte")

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

        elif opcao == "32":
            limpar_tela()
            banner_hacker()
            print(f"{CIANO}--- CENTRAL DE SUPORTE ---{RESET}\n")
            print("01 Abrir chamado")
            print("02 Meus chamados")
            print("00 Voltar")
            sub = input("suporte@swindler:~# ").strip()
            if sub in ("1", "01"):
                criar_chamado(usuario)
                pausar()
            elif sub in ("2", "02"):
                cliente_meus_chamados(usuario)
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
        banner_profissional()
        mostrar_hora()
        titulo_secao("Portal de acesso", "SWINDLER Corporate Security Lab")
        menu_item(1, "Acesso Administrativo")
        menu_item(2, "Acesso de Funcionário")
        menu_item(3, "Acesso de Cliente autorizado")
        menu_item(4, "Informações / diagnóstico local")
        menu_item(0, "Sair", destaque=True)
        linha()

        opcao = input("swindler@auth:~# ").strip()
        if opcao in ("1", "01"):
            if login_admin():
                painel_admin()
        elif opcao in ("2", "02"):
            autorizado, usuario = login_funcionario()
            if autorizado:
                painel_funcionario(usuario)
        elif opcao in ("3", "03"):
            autorizado, usuario = login_cliente()
            if autorizado:
                painel_cliente(usuario)
        elif opcao in ("4", "04"):
            util_informacoes_sistema()
        elif opcao in ("0", "00"):
            animacao("Encerrando SWINDLER", pontos=3)
            registrar_log("Programa encerrado.")
            print(f"{VERMELHO_SANGUE}\n[!] SISTEMA ENCERRADO.{RESET}\n")
            break
        else:
            print(f"{VERMELHO_SANGUE}Opção inválida.{RESET}")
            time.sleep(0.6)


def main():
    try:
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
