def censor(text, word):
	words = text.split(" ")
	for i in words:
		if i == word:
			newtext = text.replace(word, "*"*len(word))
	print newtext

censor("hey hey hey", "hey")