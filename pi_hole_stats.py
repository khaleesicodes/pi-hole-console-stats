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
pi_stats_table = AsciiTable(pi_stats_data)
pi_stats_table.inner_heading_row_border = False
pi_stats_table.inner_row_border = True
pi_stats_table.title = 'rasberry_pi_stats'

pi_hole_stats_data = [
    ['Ads_blocked', ADS_BLOCKED]
]
pi_hole_stats_table = AsciiTable(pi_hole_stats_data)
pi_hole_stats_table.inner_heading_row_border = False
pi_hole_stats_table.inner_row_border = True
pi_hole_stats_table.title = 'pi_hole_stats'

print(pi_stats_table.table)
print(pi_hole_stats_table.table)