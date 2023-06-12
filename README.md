# MathhomeworkMaker
Its a pogram wich helped me do my math homework very simple


Code 1: 
We have a proportionality factor m and we need to check if y/x is equal to m. 

IF YES: print index + "right" 
IF NO: print index + "wrong"
```
m = 1/4

check_x = [4,-2,3,5]
check_y = [1,-2,1/12,5/4]
index = 0

while len(check_x) > index:
    if check_y[index] / check_x[index] == m:
        print( str(index + 1) + ". richtig")
    else:
        print( str(index + 1) + ". falsch")
    index += 1

print("...terminal expired...")
```

Code 2:
In this Code we need to tell what is m for each variable pair, and just print the Index and m
```
m = 0
check_x = [3,2,4,1,2,-4,4/5,5,-2,5]
check_y = [-7.5,20,-10,5,4/5,-20,8,2,-10,25]
index = 0

def check(x,y):
    return(y/x)

while len(check_x) > index:
    m = check(check_x[index], check_y[index])
    print(m) 
    index += 1
print("...terminal expired...")
```
