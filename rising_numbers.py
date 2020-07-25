#!/usr/bin/python3
#
# Rising Numbers - Amazon Challenge
# By Kyle Chapman (kyleichapman@gmail.com)
# 02/01/2019

import time

def main():
	""" Main function """
	upper_limit = 10 ** 3
	lower_limit = 1
	count = 0
	index = 0

	start_time = time.time()
	indices = [i for i in range(lower_limit, upper_limit) if (i % 10 != 0)]

	for i in indices:
		check = str(i)
		rising = True

		for j in range(1, len(check)):
			a = int(check[j])
			b = int(check[j-1])

			if a < b:
				rising = False
				break

		if rising:
			index += 1
			count += i

	end_time = time.time()
	print(count)
	print(f"Took {end_time - start_time} seconds")

if __name__ == "__main__":
	main()
