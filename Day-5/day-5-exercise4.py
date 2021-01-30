# FizzBuzz Solution


for i in range(1, 101):
    stri = ""
    if (i % 3 == 0):
        stri += "Fizz"
    if(i % 5 == 0):
        stri += "Buzz"

    if(stri == ""):
        print(i)
    else:
        print(stri)
