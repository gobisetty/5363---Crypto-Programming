#Name: Sai Rahul Gobisetty
#Program3
import argparse
import sys
import fractions
import graph

def CheckPoints(a,b,x1,y1,x2,y2):
	if ((pow(y1,2)==pow(x1,3)+a*x1+b) and (pow(y2,2)==pow(x2,3)+a*x2+b)):
		print("Points are on curve")
		m=FindPoint(a,b,x1,y1,x2,y2)
		#print(m)
		return m
	else:
	    return 0
		
def FindPoint(a,b,x1,y1,x2,y2):
    if(y1!=y2):
        m=(y2-y1)/(x2-x1)
        #print(m)
    else:
        m = ((3*(x1**2))+a)/(2*y1)
   
    return m

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()
	
    a=float(args.a)
    b=float(args.b)
    x1=float(args.x1)
    y1=float(args.y1)
    x2=float(args.x2)
    y2=float(args.y2)
    
    m=CheckPoints(a,b,x1,y1,x2,y2)
    if(m==0):
        print("Points are not on curve")
    else:
        x3=pow(m,2)-x1-x2
        y3=(m)*(x3-x2)+y2
        graph.ViewGraph(a,b,x1,y1,x2,y2,x3,y3,m)
        x=fractions.Fraction(x3).limit_denominator(1000)
        y=fractions.Fraction(y3).limit_denominator(1000)
        print("Third points is")
        print("x3=",x,"y3=",y)
	
if __name__ == '__main__':
    main()