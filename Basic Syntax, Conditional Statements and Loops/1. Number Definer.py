num = float(input())

if num == 0:
    print ('zero')
else:
    if num > 0:
        result = 'positive'
    else:
        result = 'negative'

    if 0 < abs(num) < 1:
        print(f'small {result}')
    elif abs(num)>1_000_000:
        print(f'large {result}')
    else:
        print(result)
