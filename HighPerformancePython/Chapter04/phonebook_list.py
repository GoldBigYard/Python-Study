phonebook = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555")
]


def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None


if __name__ == '__main__':
    print(f"John Doe's phone number is {find_phonenumber(phonebook, 'John Doe')}")
