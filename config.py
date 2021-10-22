import sys

os = 0.5
if sys.platform != "darwin":
    os = 1

# RESOURCE
res = 'res_msi'

# REFRESH
max_round_login = 10
max_round_check_element = 60

### DELAY
delay_all_process = 300

### SIZE
size_w = 515
size_h = 330
pos_w = 470
pos_h = 330
chrome = [(0,0),
    (1,0),(2,0),(3,0),
    (0,1),(1,1),(2,1),(3,1),
    (0,2),(1,2),(2,2),(3,2),
    (0,3),(1,3),(2,3),(3,3),
]

chrome_mac = [
    [0,50,1000,750],
    [880,50,1000,750],
    [1880,50,1000,750],
    [0,800,1000,750],
    [880,800,1000,750],
    [1880,800,1000,750],
]