#Soal 1

def find_short(s):
    kata = s.split()
    # print(kata)
    a = -1
    for kata1 in kata:
        if len(kata1) < a or a == -1:
            a = len(kata1)
    return a

print(find_short("Many people get up early in the morning"))
print(find_short("Every office would getting newest monitor"))
print(find_short("Create new file after this morning"))

#Soal 2

def persistence(x):
    total = x
    start = 0
    while (total >= 10):
        i = total
        j = str(i)
        total1 = 1

        for item in range (len(j)):
            total1 *= int(j[item])
        start += 1
        total = total1
    return print(start)
persistence(39)
persistence(999)
persistence(4)



#Soal 3

def multiplication_table(row,col):
    x=[]
    for item in range(1,row+1):
        y=''
        for item1 in range(1,col+1):
            z=0
            z+=item*item1
            x.append(z)
            y+=str(z) + ' '
        print(y)
multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)

#Soal 4

def alphabet_position(text):
    
    huruf = {
    "a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10",
    "k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19",
    "t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26",
    "'":"",".":"","?":''
    }
    kalimat = text.lower().replace(' ','')
    hasil = ''
    
    for item in kalimat:
        hasil += str(huruf[item])+' '
    print(hasil)

alphabet_position("The sunset sets at twelve o'clock.")
alphabet_position("It's never too late to try.")
alphabet_position("Have you done your homework?")

# Soal bonus
# def is_prime(num):
