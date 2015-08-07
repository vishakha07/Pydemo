for a in [1,2,3,4,5]:
    print a

for l in 'python':
    print l

for values in [1,2,3]:
    print values

color=['magenta' ,'yellow', 'red']
for c in color:
        print c
    
temp =eval(raw_input("Enter temperature"))
while True:

        if temp>31 and temp<35:
            print 'summer day'
            break
        elif temp>35 and temp<40:
            print 'warm day'
            break
        elif temp>40 and temp<50:
            print 'high perfomance'
            break
        else:
            print 'invalid'
            break


