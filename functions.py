def create_output(slides):
	file = open("out.txt","w") 
	n = len(slides)
	file.write(n)
	for i in slides:
		file.write(i)
	return 0
