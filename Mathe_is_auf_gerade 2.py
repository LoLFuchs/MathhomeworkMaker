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