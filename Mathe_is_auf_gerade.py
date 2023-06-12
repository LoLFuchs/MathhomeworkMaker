
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