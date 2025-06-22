import argparse

def c_to_f(c):
    return(c*9/5)+32

def f_to_c(f):
    return(f-32)*5/9

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit.")
    grp=parser.add_mutually_exclusive_group(required=True)
    grp.add_argument("-c","--celsius",type=float,help="Temperature in Celsius")
    grp.add_argument("-f","--fahrenheit",type=float,help="Temperature in Fahrenheit")
    args=parser.parse_args()

    if args.celsius is not None:
        result=c_to_f(args.celsius)
        print(f"{args.celsius}°C={result:.2f}°F")
    else:
        result=f_to_c(args.fahrenheit)
        print(f"{args.fahrenheit}°F={result:.2f}°C")
