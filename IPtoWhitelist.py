# This is a Python program that takes IP addresses as input, and outputs their respective IP whitelisting rule
# format : SetEnvIF X-Forwarded-For \b35\.62\.96\.52 AllowIP$

import sys

def IPtoWhitelist(ip):

    ip_split = ip.split('.')
    ip_split = list(map(int, ip_split))

    rule = "SetEnvIF X-Forwarded-For \\b{}\.{}\.{}\.{} AllowIP$".format(ip_split[0],ip_split[1],ip_split[2],ip_split[3])
    print(rule)

cmd_args = sys.argv
cmd_args.remove("IPtoWhitelist.py")
len_cmd_args = len(sys.argv)

count = 0
while count < len_cmd_args:
    IPtoWhitelist(cmd_args[count])
    count += 1
