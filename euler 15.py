width = tuple(range(1,int(input('정사각형의 길이 입력:'))+2))

def sum_width():
    global width
    next_width = ()
    for num in range(1,len(width)+1):
        next_width+= sum(width[0:num]),
    width = next_width
    return width

print(list([1]*(len(width))))
for n in range(1,len(width)):
    print(width)
    sum_width() 
