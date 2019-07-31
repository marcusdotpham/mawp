# https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python/2077944


import string

def capitalize(s):
	return string.capwords(s)

s = 'The quick brown fox jumped over the lazy dog.'
s_cap = capitalize(s)
print(s_cap)


def single_space(s):
	