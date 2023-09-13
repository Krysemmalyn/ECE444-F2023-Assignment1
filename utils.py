class utils:
    def reversed(input_num):
        if type(input_num) is not int:
            raise TypeError("Not Integer")
        reversed_num = 0
        while input_num!=0:
            digit = input_num%10
            reversed_num = reversed_num*10+digit
            input_num//=10
        print("Reversed number: " + str(reversed_num))
        return reversed_num
    
    def formatter(input_num):
        if type(input_num) is not int:
            raise TypeError("Not Integer")
        binary=bin(input_num)
        octal=oct(input_num)
        print(binary)
        print(octal)
        return binary, octal
