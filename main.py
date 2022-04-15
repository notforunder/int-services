import os
from pyfiglet import Figlet 
import requests
from prettytable import PrettyTable
import default_urls as us

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

bc = bcolors
clear = lambda: os.system('cls')
list = us.list

def url_append():
    print(bc.WARNING + '[!] Example: https://example.com' + bc.ENDC)
    url = input('Put URL: ')
    list.append(url)
    main()

def url_delete():
    print(bc.WARNING + '[!] Example: 0\n[!] Will delete first line and -1 will delete last line' + bc.ENDC)
    for i in list:
        print(i)
    choice = input('Choose line: ')
    del list[int(choice)]    
    main()

def service_table():
    print('Services')
    table = PrettyTable()
    table.field_names = [bc.BOLD + 'Service', 'Status_Code' + bc.ENDC]
    for i in list:
        try:
            status = str(requests.get(i))
            table.add_row([i + '\n--', bc.OKGREEN + 'Passed' + bc.ENDC + '\n--'])
        
        except requests.exceptions.ConnectionError:
            table.add_row([i + '\n--', bc.FAIL + 'Error' + bc.ENDC + '\n--'])
    print(table)


def __menu():
    print('[1] Append new service\n[2] Delete service\n[Q] Quit')
    choice = input('Enter: ')
    if choice == "1":
        print("Append")
        url_append()
    elif choice == "2":
        print("Deleting")
        url_delete()
    elif choice == "q" or "Q":
        exit


def main():
    clear()
    banner = Figlet(font='doom')
    print(banner.renderText('SERVICES'))
    service_table()
    print('\n by zirxayd')
    __menu()

if __name__ == '__main__':
    main() 
