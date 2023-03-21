def main():
    plate = input("vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isdigit():
        return False
    if not s.isalnum():
        return False
    if s[-1].isdigit():
        return False
    return True


if __name__ == "__main__":
    main()