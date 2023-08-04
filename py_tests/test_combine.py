import sys

sys.path.insert(1, './/Code')

import generate

valid_email_formats = [
    'example@example.com',
    'example123@example.com',
    'example_123@example.com',
    'example-123@example.com',
    'example.123@example.com',
    'example+123@example.com',
    'example@subdomain.example.com',
    'example@sub-domain.example.com',
    'example@sub_domain.example.com',
    'example@subdomain.sub-domain.example.com'
]

random_numbers = [22, 1, 80, 2, 44, 5, 49, 46, 50, 21]

def test_num_gen_combine():

    for i in range(len(valid_email_formats)):

        number_gen_class = generate.UserGen(valid_email_formats[i],random_numbers[i])

        print(number_gen_class.combine_mail_num())




if __name__ == "__main__":
    test_num_gen_combine()
    print("Everything passed")