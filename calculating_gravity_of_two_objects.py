g = 6.673e-8
def calc_f(m1,m2,d):
    return((g*m1*m2)/d**2) # or return((g*m1*m2)/pow(d)) ---> def pow(d):
def main():
    m1 = float(input('Enter mass of object 1(g) : '))
    m2 = float(input('Enter mass of object 2(g) : '))
    d = float(input('Enter the distance between objects(cm) : '))
    print('f = ',calc_f(m1, m2, d))
main()


    
    