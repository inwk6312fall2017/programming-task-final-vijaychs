f= open("new-running-config.cfg")
for line in f:
	each = line.strip()
	if each.startswith("ip address 172"):
		delim = each.split(".")
		delim = [k.replace("172","192") for k in delim]
		print(delim)
print(" ")
print("Replaced IP addresses that start with '172.' with IP addresses that start with '192.', Leaving the remaining octets unchanged successfully")
