def lastword(case):
	word = str(input())

	final_word = ''
	for  c in word:
		if not final_word:
			final_word = final_word + c
		elif c >= final_word[0]:
			final_word = c + final_word
		else:
			final_word = final_word + c

	print("Case #",case, ": ", final_word, sep='')


T = int(input())
for i in range(1,T+1):
    lastword(i)
