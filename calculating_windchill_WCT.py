def calc_w(t,v):
    return(33-((10*(v**0.5)-v+10.5)*(33-t)/22))
def main():
    t = int(input('Enter temprature(c): '))
    v = int(input('Enter velocity(m/s): '))
    print('W = ',calc_w(t,v))
    
main()
