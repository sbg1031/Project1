## 함수부
def add_func(n1,n2):
    return n1+n2

def sub_func(n1,n2):
    return n1-n2

def gob_func(n1,n2):
    return n1*n2

def na_func(n1,n2):
    return n1/n2

## 전역 변수부
num1,num2,result = 100,200,0

## 메인 코드부
result = add_func(num1,num2)
print( num1, '+', num2,'=', result)
       
result = sub_func(num1,num2)
print( num1, '-', num2,'=', result)

result = gob_func(num1,num2)
print( num1, '*', num2,'=', result)

result = na_func(num1,num2)
print( num1, '/', num2,'=', result)
       
       
