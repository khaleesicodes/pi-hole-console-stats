from terminaltables import AsciiTable
import subprocess
import time
import json
import requests
import os

api_url = 'http://localhost/admin/api.php'

def print_table(data, title):
    table = AsciiTable(data)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.title = title
    print(table.table)

while True:

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-disp$
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell=True)
    cmd = "hostname"
    HOST = subprocess.check_output(cmd, shell=True)
    cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    cmd = "free -m | awk 'NR==2{printf \"%s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True)
    cmd = "df -h | awk '$NF==\"/\"{printf \"%d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell=True)

    # Pi Hole data!

    r = requests.get(api_url)
    data = json.loads(r.text)
    DOMAINS = data['unique_domains']
    ADS_BLOCKED = data['ads_blocked_today']
    CLIENTS = data['unique_clients']

    pi_stats_data = [
        ['IP Address', IP.strip()],
        ['CPU Load', CPU],
        ['Memory', MemUsage],
        ['Disk', Disk],
        ['Host', HOST.strip()]
    ]

    pi_hole_stats_data = [
        ['Ads_blocked', ADS_BLOCKED],
        ['Clients', CLIENTS],
        ['Domains', DOMAINS]
    ]

    # clear screen
    os.system('clear')

    print_table(pi_stats_data, "rasberry_pi_stats")
    print(" ")
    print(" ")
    print_table(pi_hole_stats_data, "pi_hole_stats")