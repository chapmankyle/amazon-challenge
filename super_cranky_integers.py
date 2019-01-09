#!/usr/bin/python3

# Super Cranky Integers - Amazon Challenge
# By Kyle Chapman (kyleichapman@gmail.com)
# 02/01/2019

def main():
	""" Main function """
	limit = 10 ** 6
	count = 0

	for i in range(11, limit):
		check = str(i)
		rev = int(check[::-1])
		cranky = False

		for j in range(1, len(check)):
			f = check[0:j]
			s = check[j:]
			mul = int(f) * int(s)

			if mul == rev:
				cranky = True
				print(f, 'x', s, '=', mul)
				break
		
		if cranky:
			count += i
	
	print(count)

if __name__ == "__main__":
	main()
