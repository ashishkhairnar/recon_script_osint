#!/bin/python
import subprocess
import os
import socket
import sys

PATH = "/home/"

#PATH_INPUT = PATH + "input.txt"

PATH_OUTPUT = PATH + "output.txt"

print 'Enter all domains (press enter and ctrl-d to enter your input): '

domains_from_user_input = sys.stdin.readlines()
domains=[]

for line in domains_from_user_input:
   line = str(line).strip('\n')
   domains.append(line)


#for domains in domains_from_user:
#    ip_addresses.append(str(ip))
#    i=i+1

# Uncomment following block if you want to use file instead of std-in
'''
with open(PATH_INPUT, "r") as f:
    read_data = f.readlines()
    i = 0
    domains=[]
    for line in read_data:
        domains_list = read_data[i].strip('\n')
        domains.append(domains_list)
        i=i+1

   f.close()
'''

output = dict()

host_number = 0

for each_domain in domains:
    try:
        host_ip = socket.gethostbyname(each_domain)
        output[each_domain] = str(host_ip)
	host_number = host_number + 1
    except:
        output[each_domain] = "IP not resolvable"

ipaddress=[]
hosts = []

with open(PATH_OUTPUT, 'w') as file:
    file.write("Hosts Active: {}".format(host_number))
    file.write("\n\nHosts:\n\n")
    for key,value in output.items():
        if value!= "IP not resolvable":
            file.write(str(key + "\n"))
            ipaddress.append(value)
            console = str(key + value)


    file.write("\n\nHosts - IP Address:\n\n")
    for key,value in output.items():
        if value!= "IP not resolvable":
            file.write(str(key + "      -      " + value + "\n"))
            ipaddress.append(value)


    file.write("\n\nIP Address:\n\n")
    for key, value in output.items():
        if value != "IP not resolvable":
            file.write(str(value + "\n"))
            ipaddress.append(value)

    reverse_lookup_output_bash=[]
    whois_output_bash=[]

    for ip in  ipaddress:
        command_reverse = "echo \"" + ip + " - \" `dig +answer -x " + ip + "| grep \'SOA\|PTR\'`"
        command_whois =   "echo \"" + ip + " - \" `whois "          + ip + "| grep \'CIDR\|NetName\'`"

        command_output = subprocess.check_output(command_reverse, shell=True);
		command_output1 = subprocess.check_output(command_whois, shell=True);

        reverse_lookup_output_bash.append(command_output)
		whois_output_bash.append(command_output1)

    file.write("\n\n[+] REVERSE LOOKUP:\n\n")

    for line in reverse_lookup_output_bash:
        file.write(line)


    file.write("\n\n[+] WHOIS LOOKUP:\n\n")

    for line in whois_output_bash:
    	file.write(line)

    file.close()
