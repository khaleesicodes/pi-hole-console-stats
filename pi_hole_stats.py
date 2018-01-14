from terminaltables import AsciiTable

# fake Test Data
IP_ADDRESS = "192.168.x.x"
CPU_LOAD = "x %"
MEMORY = "30/100 MB"
ADS_BLOCKED = "1000"


pi_stats_data = [
    ['IP Address', IP_ADDRESS],
    ['CPU Load', CPU_LOAD],
    ['Memory', MEMORY]
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