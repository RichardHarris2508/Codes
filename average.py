def extract(numbers):
    print('----------------------------------------------------------------------');
    numbers += ','
    num = ''
    sum = 0
    terms = 0
    for i in numbers:
        #print(i)
        if i != ',':
            num += i
        else:
            print(num,'  |  ', end=' ')
            sum += int(num)
            num=''
            terms += 1
    print('\n----------------------------------------------------------------------')
    print(sum,"  |  ",terms)
    return sum/(terms)

print(extract(input('Enter all numbers\t')))