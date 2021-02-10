# FIZZBUZ!
# For multiples of three print “Fizz” instead of the number and for
# the multiples of five print “Buzz”. For numbers which are multiples of
# both three and five print “FizzBuzz”

i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("{} {}".format(i, "FizzBuzz!"))
        i = i + 1
    else:
        if i % 3 == 0:
            print("{} {}".format(i, "Fizz"))
            i = i + 1
        else:
            if i % 5 == 0:
                print("{} {}".format(i, "Buzz"))
                i = i + 1
            else:
                print(i)
                i = i + 1
