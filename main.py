import os
import sys
import requests
import threading
from prettytable import PrettyTable

class Services():
    def __init__(self, input_file):
        self.input_file = input_file

    def get_urls(self):
        with open(self.input_file, "r") as f:
            return f.read().splitlines()

    def table_data(self):
        urls = self.get_urls()
        table = PrettyTable(["URL", "Status Code"])
        for url in urls:
            try:
                response = requests.get(url)
                table.add_row([url, response.status_code])
            except requests.exceptions.ConnectionError:
                table.add_row([url, "Connection Error"])
        return table

    def refresh_table(self, interval):
        timer = threading.Event()
        while True:
            os.system("clear")
            print(self.table_data())
            timer.wait(interval)
            self.table_data()


def main():
    services = Services(sys.argv[1])
    output = services.refresh_table(2) # 2 seconds refresh
    print(output)

if __name__ == '__main__':
    main() 