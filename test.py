def getInfo():
    var1= input("\nplease provide first numeric number: ")
    var2= input("please provide second: ")
    return var1,var2

def compute():
    go = True
    while go:
        var1,var2=getInfo()
        try:
            var3= int(var1)+int(var2)
            go = False #turn off if got correct input
        except ValueError as e:
            print("{}: \n\nyou did not provide a numeric num".format(e))
        except:
            print("\n\ninvalid input. program will close")
    print("{}+{} = {}".format(var1,var2,var3))


if __name__ == "__main__":
    compute()
