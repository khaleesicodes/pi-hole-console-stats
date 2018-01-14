from terminaltables import AsciiTable
import subprocess

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


# fake Test Data
ADS_BLOCKED = "1000"


pi_stats_data = [
    ['IP Address', IP.strip()],
    ['CPU Load', CPU],
    ['Memory', MemUsage],
    ['Disk', Disk],
    ['Host', HOST.strip()]
]

pi_hole_stats_data = [
    ['Ads_blocked', ADS_BLOCKED]
]


def print_table(data, title):
    table = AsciiTable(data)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.title = title
    print(table.table)


print_table(pi_stats_data, "rasberry_pi_stats")
print(" ")
print(" ")
print_table(pi_hole_stats_data, "pi_hole_stats")