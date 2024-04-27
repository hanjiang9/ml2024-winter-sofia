def main():

    num = input("Please enter a positive integer")

    nums_str = input("Please enter " + num + " numbers one by one:")

    number = input("Please enter a number")

    index_print = "-1"
    for index, nums_char in enumerate(nums_str):
        if(int(nums_char) == int(number)):
            index_print = str(index);
            print("The index of " + number +" is:" + index_print)

    if(index_print == "-1"):
        print(index_print)
        
main()