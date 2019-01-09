#!/usr/bin/python3

# Rising Numbers - Amazon Challenge
# By Kyle Chapman
# 02/01/2019

def main():
    """ Main function """
    limit = 10 ** 3
    count = 0
    index = 0

    for i in range(1, limit):
        if (i % 10 == 0):
            pass
        else:
            check = str(i)
            rising = True

            for j in range(1, len(check)):
                a = long(check[j])
                b = long(check[j-1])

                if a < b:
                    rising = False
                    break
            
            if rising:
                index += 1
                count += i
            
    print(count)

if __name__ == "__main__":
    main()