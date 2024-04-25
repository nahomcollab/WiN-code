def decimal_to_octal(decimal):
    def integer_part(decimal, after_point):
        if after_point == '0':
            octal = []
            decimal = int(decimal)
            while decimal != 0:
                remainder = decimal % 8
                octal.append(str(remainder))
                decimal //= 8
            return ''.join(octal[::-1])

    def fractional_part(decimal, after_point):
        octal2 = []
        for i in range(3):
            product = (int(after_point) / 10) * 8
            o_before_point = str(product).split('.')[0]
            o_after_point = str(product).split('.')[1]
            if int(o_before_point) < 8:
                octal2.append(o_before_point)
            else:
                break
        return ''.join(octal2)

    decimalS = str(decimal)
    before_point = decimalS.split('.')[0]
    after_point = decimalS.split('.')[1] if '.' in decimalS else '0'
    if after_point == '0':
        return integer_part(before_point, after_point)
    else:
        result1 = str(integer_part(before_point, after_point))
        result2 = str(fractional_part(before_point, after_point))
        return result1 + "." + result2


def odd_below(decimal):
    odds = []
    while decimal != 0:
        if int(decimal) % 2 != 0:
            odds.append(decimal)
        decimal -= 1
    return len(odds)


def main():
    decimal = float(input("Please enter the decimal: "))
    choice = input("Enter 'octal' to convert to octal and 'count' to count odd integers below the number ").lower()
    if choice == 'octal':
        print(f"The octal equivalent of {decimal} is {decimal_to_octal(decimal)}")
    elif choice == 'count':
        print(f"The number of +ve odd numbers below {decimal} is {odd_below(decimal)}")
    else:
        print("Please enter a valid operation")


if __name__ == "__main__":
    main()
