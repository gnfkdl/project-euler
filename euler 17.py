words = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twelve',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}

def sum_of_words(x):
    sum = 0
    for n in range(1,x + 1):
        if n < 100 and n in words:
            sum += len(words[n])
            continue

        if n % 1000 == 0:                sum+= len(words[n // 1000]) + len(words[1000])

        if n % 1000!=0 and n >= 100:     sum+= len(words[(n % 1000) // 100]) + len(words[100]) + 3
        if n % 1000!=0 and n % 100 == 0: sum-= 3

        if n % 100 in words:             sum+= len(words[n % 100])
        else:                            sum+= len(words[((n % 100) // 10) * 10]) + len(words[n % 10])

    return sum

print(sum_of_words(1000))