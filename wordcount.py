def word_count(file):
	""" Takes a file and print how many time each space-separated word occurs in file"""

	word_counts = {}
	all_the_words = []
	text_to_count = open(file)

	for line in text_to_count:
		line = line.rstrip()
		words = line.split(" ")
		all_the_words.extend(words)

	for word in all_the_words:
		word_counts[word] = word_counts.get(word, 0) + 1


	for word in word_counts:
		print(word, word_counts[word])

word_count("twain.txt")