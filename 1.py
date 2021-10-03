try:
    chislo = int (input ('Введите число: '))
    cifra = int (input ('Введите цифру: ')) 
except ValueError:
    print ('Ошибка')
else:

     n = 0

     while chislo > 0:
          m = chislo % 10
          if m == cifra: 
            n = n+1
            chislo = chislo // 10
          else:
            n = n+0
            chislo = chislo // 10
     else:
          print (n)