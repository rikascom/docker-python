import os
if os.path.exists("Dockerfile"):
	os.remove("Dockerfile")

os.system("clear")
print("Current Docker Images\n")

os.system("docker images")
file = open("Dockerfile","a")

maintainer = input("\nEnter Author's Name: ")
if maintainer == "":
	exit()
if maintainer == ".":
	maintainer = "Sean Rikard"
	email = "smrikard@gmail.com"
elif maintainer != "":
	email = input("Enter Author's email address: ")
	file.write("\nMAINTAINER " + maintainer + " " + email + "\n\n")

baseimage = input("\nBase Image: ")
tagname = input("Tag: ")
file.write("FROM " + baseimage + ":" + tagname + "\n\n")

print("\nEnter Ports to Enable (One Port per Line, blank if none or to end.)")
print("Enter port only such as 80, or port with protocol, such as 80/tcp\n")
ports = ""
exposeports = "1"
while exposeports != "":
	exposeports = input("Port to Expose: ")
	if exposeports == "":
		break
	ports += (exposeports + " ")
if ports != "":
	file.write("EXPOSE " + ports + "\n\n")
	print("\n")

packages = "1"
packs = ""
print("Enter packages to install. One package per line. Blank if none or to end.")
while packages != "":
	packages = input("Packages: ")
	if packages == "":
		break
	packs += (packages + " ")
if packs != "":
	file.write("RUN apt-get update -y && apt-get install -y " + packs + "\n\n")

workingdir = input("\nEnter working directory (Blank for none): ")
if workingdir != "":
	file.write("WORKDIR " + workingdir + "\n\n")

sourcedir = input("\nSource Files Path (Blank for None): ")
if sourcedir != "":
	destdir = input("Destination Container Path: ")
	file.write("COPY " + sourcedir + " " + destdir + "\n\n")

imagename = input("\nName this Image (name:tag): ")

print("\n")

file.flush()
os.system("docker build -t " + imagename + " .")
# os.system("docker run -d -it --name " + " " + imagename)

# os.system("docker ps")
os.system("docker images")


