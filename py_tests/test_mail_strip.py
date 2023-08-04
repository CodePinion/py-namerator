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


def test_smail_strip():

    for email in valid_email_formats:

        user_gen_class = generate.UserGen(email,0)

        print(user_gen_class.StripMail())



if __name__ == "__main__":
    test_smail_strip()
    print("Everything passed")

#random_numbers = [22, 23, 80, 2, 44, 5, 49, 46, 50, 21]
