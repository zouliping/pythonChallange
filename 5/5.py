import pickle,StringIO

f = open(r'F://6/python challange/5.txt','r')
x = pickle.load(f)

for sublist in x:
    str = ''
    for (a,b) in sublist:
        str += a*b
    print str
