with open("running-config.cfg") as document:
	access_list = {}
	for line in document:
		stripped_line = line.strip()
		if stripped_line.startswith("access-list"):
			access_list[stripped_line[0:11]] = stripped_line[11:]
			print(access_list)
