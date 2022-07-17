from dis import dis

phonebook = {
    "John Doe": "555-555-5555",
    "Albert Einstein": "212-555-5555"
}

def a():
    b = {"A": "ABCD"}
    c = ["a", "b"]
    return b["A"] + c[1]


if __name__ == '__main__':
    dis(a)
    print(f"John Doe's phone number is {phonebook['John Doe']}")
