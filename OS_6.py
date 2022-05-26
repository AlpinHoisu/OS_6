import numpy as np
import string

def search(segm, n):
    
    i = [-1 for j in range(n)]
    j = 0
    
    while j < n:
        k = j
        r = True
        while r:
            i[j] = np.random.randint(20)
            if (segm[i[j],0] == 0):
                r = False
                
        while k < n-1:
            if (segm[i[k]+1,0] == 0)and(i[k] < 19):
                i[k+1] = i[k]+1
                k += 1
            else:
                break

        j = k+1
        
    return i

segm = np.zeros((20, 2), dtype=int)
disk = np.zeros((20, 2), dtype=int)
    
q = 0
i = 0
v = 0
ch = 0

print('\n1. Добавить задачу\n2. Удалить задачу\n3. Состояние памяти\n4. Выход\n')

while ch != 4:
    ch = int(input('\nВыбор: '))
    
    if ch == 1:
        q = int(input('Размер(Кбайт): '))
        
        if v + q > 64:
            print ('Переполнение памяти')
        else:
        
            if q < 17:
                l = search(segm, 1)
                segm[l[0]] = [ord(string.ascii_letters[i]), q]
                v += q

            elif q < 33:
                l = search(segm, 2)
                segm[l[0]] = [ord(string.ascii_letters[i]), q//2]
                disk[l[0]] = [ord(string.ascii_letters[i]), q//2+q%2]
                v += q//2


            elif q < 49:
                l = search(segm, 3)
                segm[l[0]] = [ord(string.ascii_letters[i]), q//3]
                disk[l[0]] = [ord(string.ascii_letters[i]), q//3]
                disk[l[1]] = [ord(string.ascii_letters[i]), q//3+q%3]
                v += q//3

            else:
                l = search(segm, 4)
                segm[l[0]] = [ord(string.ascii_letters[i]), q//4]
                disk[l[0]] = [ord(string.ascii_letters[i]), q//4]
                disk[l[1]] = [ord(string.ascii_letters[i]), q//4]
                disk[l[2]] = [ord(string.ascii_letters[i]), q//4+q%4]
                v += q//4
                
            i += 1
            
    if ch == 2:
        q = input('Задача: ')
        
        for j in range(20):
            
            if segm[j, 0] == ord(q):
                v -= segm[j, 1]
                segm[j] = [0, 0]
                
    if ch == 3:
        print('Оперативная память')
        for j in range(20):
            if segm[j, 0] != 0:
                print(chr(segm[j, 0]),' - ', segm[j, 1])
        print('Диск')        
        for j in range(20):
            if disk[j, 0] != 0:
                print(chr(disk[j, 0]),' - ', disk[j, 1])