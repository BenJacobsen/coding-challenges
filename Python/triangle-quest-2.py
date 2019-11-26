for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum(map(lambda x: (x * pow(10, 2*i - (x+1))) + (x * pow(10, x-1)) if x!=i else x * pow(10, x-1), range(1, i+1))))
