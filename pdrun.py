import os

os.system("clear")
os.system("docker images")

base = input("\nWhich Docker Base? ")
if base == "":
	exit()
basetag = input("\nTag: ")
if basetag != "":
	tag = (":" + basetag)

mountdir = input("\nDirectory to Mount (localdir:containerdir): ")
if mountdir != "":
	mount = ("-v " + mountdir + " ")
else:
	mount = ""

ports = ""
exposeports = "1"
print("\nEnter Ports to Expose, one set per line host:container. Enter blank if none or 'all' for all Ports.")
while exposeports != "":
	exposeports = input("\nPorts to Expose: ")
	if exposeports == "":
		break
	if exposeports == "all":
		ports = "-P "
		break
	ports += ("-p " + exposeports + " ")
name = input("\nEnter a name for container (Blank for none): ")

if name != "":
	nameout = ("--name " + name + " ")
else:
	nameout = ""

output = ("docker run -d -it " + mount + ports + nameout + base + tag)
#print(output)
os.system(output)
print("\n")
os.system("docker ps -a")
print("\n")
