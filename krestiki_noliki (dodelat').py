pole=[]
proverca=[]
def test(pole):
    global pole
    if 

for i in range(3):
    a=[0, 0, 0]
    pole.append(a[::])
    proverca.append(a[::])
game =True
while game:
     n=list(input().split())
     ny=int(n[0])
     nx=int(n[1])
     if proverca[ny][nx]!= 1 :
         pole[ny][nx]='x'
         proverca[ny][nx]=1

     for row in a:
         if row == d:
             print('Победил игрок номер 1')
         elif row == g:
             print('Победил игрок номер 2')
     for col_num in range(3):
         col = []
         for i in range(3):
             col.append(a[i][col_num])
         if col == d:
             print('Победил игрок номер 1')
         elif col == g:
             print('Победил игрок номер 2')
     for col_num in range(3):
         col = a[col_num][col_num]
         if col == d:
             print('Победил игрок номер 1')
         elif col == g:
             print('Победил игрок номер 2')