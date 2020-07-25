#!/usr/bin/python3

# Super Cranky Integers - Amazon Challenge
# By Kyle Chapman (kyleichapman@gmail.com)
# 02/01/2019

import time

def main():
	""" Main function """
	upper_limit = 10 ** 6
	lower_limit = 11
	count = 0

	start_time = time.time()
	for i in range(lower_limit, upper_limit):
		check = str(i)
		rev = int(check[::-1])
		cranky = False

		for j in range(1, len(check)):
			f = check[0:j]
			s = check[j:]
			mul = int(f) * int(s)

			if mul == rev:
				cranky = True
				break

		if cranky:
			count += i

	end_time = time.time()
	print(count)
	print(f"Took {end_time - start_time} seconds")

if __name__ == "__main__":
	main()
