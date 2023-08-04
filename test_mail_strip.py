from generate import UserGen

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

        user_gen_class = UserGen(email,0)

        print(user_gen_class.StripMail())



if __name__ == "__main__":
    test_smail_strip()
    print("Everything passed")