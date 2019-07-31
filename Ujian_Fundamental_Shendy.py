#Soal 1

def caculate_years(principal,interest,tax,desired):
    year = 0
    for item in range(3):
        if principal < desired:
            principal = principal + (principal * interest/100) + tax
            year +=1
    return year
print(caculate_years(1000.00,0.05,0.18,1100.00))
# print(caculate_years(1000.00,0.05,0.18,1000.00))
# print(caculate_years(1000.00,0.17,0.05,2000.00))
# print(caculate_years(1000.00,0.07,0.6,5000.00))

#Soal 2

# def expandedForm(num):
num = '70304' # num '12'
if len(num) == 2:
    print(num[0]+'0'+ '+' + num[1])
elif len(num) == 5:
    print(num[0]+'0000'+ '+'+ num[2]+'00'+'+'+num[4])

 
#Soal 3

# def tower_builder(n_floors, block_size):

z=''
a=''
i=''
for item in range(3):
    for item1 in range(2):
        z += '*'
    z += '\n'
for item in range(3):
    for item1 in range(6):
        i += '*'
    i += '\n'
for item in range(3):
    for item1 in range(10):
        a += '*'
    a += '\n'
print(z+i+a)
        
