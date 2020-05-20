import subprocess, requests, optparse, time

parser = optparse.OptionParser()
parser.add_option("-d", dest='domain', help='Add domain')
parser.add_option("-o", dest='output', help='output name')
values, arguments = parser.parse_args()
domain = values.domain
output = values.output
print(' __          __  ____    _    _____ _      _          _____         __   ___  ')
print(' \ \        / / |  _ \  | |  |_   _| |    | |        |  __ \       /_ | / _ \ ')
print('  \ \  /\  / /__| |_) | | | __ | | | |    | |     ___| |__) | __   _| || | | |')
print('   \ \/  \/ / _ \  _ <  | |/ / | | | |    | |    / _ \  _  /  \ \ / / || | | |')
print('    \  /\  /  __/ |_) | |   < _| |_| |____| |___|  __/ | \ \   \ V /| || |_| |')
print('     \/  \/ \___|____/  |_|\_\_____|______|______\___|_|  \_\   \_/ |_(_)___/ ')
print('------------------------------------------------------------------------------')
time.sleep(1.5)
print('                             #BY- Faiyaz_Ahmad                                ')
time.sleep(1.5)
print("\n[+] PROCESS STARTED")
save = open(f'http{output}', 'w')

def scanner(dom, result):
    while True:
        try:
            subprocess.check_output(f'sublist3r', shell=True)
        except subprocess.CalledProcessError:
            print("SUBLIST3R NOT FOUND, LET ME INSTALL IT")
            subprocess.call("apt install sublist3r", shell=True)
            continue
        else:
            subprocess.call(f'sublist3r -d {dom} -o {result} -v', shell=True)
            break


def web_finder(val):
    with open(val, "r") as websites:
        for items in websites:
            items = items.strip()
            if items[0:8] != 'http://' or item[0:8] != 'http://':
                items = 'http://' + items
                try:
                    response = requests.get(items, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})
                except requests.exceptions.ConnectionError:
                        pass
                else:
                    if response.status_code == 200 or response.status_code == 301 or response.status_code ==302 or response.status_code == 401:
                        print(f'"{items}" seems to be live.\n')
                        save.write(f'"{items}" IS LIVE!\n')
                        save.write("------------------------------\n")




scanner(domain, output)


web_finder(output)

quit(f"Output saved as 'http{output}'")
