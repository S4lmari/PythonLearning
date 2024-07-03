k = int(input('kol-vo kotlet na skovorodku '))
m = int(input("minut jarki "))
n = int(input('kolvo kotlet '))

p = n // k # Количество подходов жарки 
if p < 1:
    t = m * 2 * 1 # умножаю на 1 так как при кол-ве котлет меньшем чем помещяется на сковородку будет меньше дробь меньше 1 что позволяет жарить в 1 заход
    print ("Время жарки: ", t)
else:
    t = m * 2 * p
    print("Время жарки: ", t)
