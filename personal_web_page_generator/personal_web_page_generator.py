name = input("Enter your name: ")

webpage = open(name + ".html", "w")

description = input("Describe yourself: ")

webpage.write("<html>\n<head>\n</head>\n<body>\n\t<center>\n")
webpage.write("\t\t<h1>" + name + "</h1>\n\t<center>\n\t<hr />\n\t")
webpage.write(description + "\n\t<hr />\n</body>\n</html>")

webpage.close()
