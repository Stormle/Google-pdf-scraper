def Writetofile(givenlist, path):
	text_file = open(path, "w")
	for i1 in givenlist:
		text_file.write(i1 + "\n")
	text_file.close()