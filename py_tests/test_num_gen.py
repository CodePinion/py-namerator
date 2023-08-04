import sys

sys.path.insert(1, './/Code')

import generate

random_numbers = [22, -1, 80, 2, 44, 5, 49, 46, 50, 21]

def test_num_gen():

    for max_num in random_numbers:

        number_gen_class = generate.UserGen('ex@gmail.com',max_num)

        print(number_gen_class.GenNumWithMax())



if __name__ == "__main__":
    test_num_gen()
    print("Everything passed")