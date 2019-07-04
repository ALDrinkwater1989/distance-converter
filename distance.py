def convertor():
    conversion = 0.62137119
    
    
    km = input("enter distance in Kilometers:  ")
    kilo = float(km)
    print("The distance in Kilometers is: {0} KM".format(km))
   
    miles = float(km) * conversion
    print("{0} KM in miles is {1}".format(km,miles))
    MPD = miles_per_day(miles)
    print("number of miles per day is {0}".format(MPD))
   
    
    
    
 
  




def miles_per_day(miles):
    mile = miles / 7
    mi = float("{0: .2f}".format(mile))
    
    return mi


def main():
    convertor()


main ()
