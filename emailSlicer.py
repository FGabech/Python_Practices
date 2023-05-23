def main():
    print("Welcome to email slicer")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, com, extension) = domain.split(".")

    print("Username:", username)
    print("Domain:", domain)
    print(".Com:", com)
    print("Extension:", extension)

main()