#problem.1 #(X+2*Y)(2*X^2-Y^2+Z)
polynomials = input('Input the polynomials:')
polynomials_lstrip = polynomials.strip('(')#將括號拆開
polynomials_strip =polynomials_lstrip.strip( ')')#將括號拆開
y = polynomials_strip.replace('-','+-')#以'+-'取代'-'
x = y.split(')(')
for i in range(len(x)):
    x[i] = x[i].split('+')#以'+'作為分隔，並匯入list
for i in range(len(x)):#以下土法煉鋼，整理所有可能的組合。
    for j in range(len(x[i])):#以下將相乘之未知數以次方表示
        if x[i][j]=='-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
        if x[i][j]=='X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j]=='Z':
            x[i][j]=x[i][j].replace('Z','1*Z')
        if x[i][j]=='X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j]=='-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*YY')
        if x[i][j]=='X^2Y':
            x[i][j]=x[i][j].replace('X^2Y','1*XXY')
        if x[i][j]=='XY^2':
            x[i][j]=x[i][j].replace('XY^2','1*XYY')
        if x[i][j]=='Z^2':
            x[i][j]=x[i][j].replace('Z^2','1*ZZ')
for i in range(len(x)):
    for k in range(len(x[i])):
        x[i][k]=x[i][k].split('*')
    for idx1 in range(len(x[i][k])):
        if x[i][k][idx1]=='X^2':
            x[i][k][idx1]=x[i][k][idx1].replace('X^2','XX')
        if x[i][k][idx1]=='Y^2':
            x[i][k][idx1]=x[i][k][idx1].replace('Y^2','YY')
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j][0]=int(x[i][j][0])
polylist,coefficient=[],[]
for i in range(len(x[0])):
    for j in range(len(x[1])):
        coefficient.append(x[0][i][0]*x[1][j][0])
        polylist.append(x[0][i][1]+x[1][j][1])
for i in range(len(coefficient)):#整理未知數的係數
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 2:
        coefficient[i] = '+2'
    if coefficient[i] == 3:
        coefficient[i] = '+3'
    if coefficient[i] == -1:
        coefficient[i] = '-1'
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
    if coefficient[i] == 2:
        coefficient[i] = '+2'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
for i in range(len(polylist[:])):#以下將相乘之未知數以次方表示
    if polylist[i] == 'XXX':
        polylist[i]=polylist[i].replace('XXX','*X^3')
    if polylist[i] == 'XYY':
        polylist[i]=polylist[i].replace('XYY','*XY^2')
    if polylist[i] == 'YXX':
        polylist[i]=polylist[i].replace('YXX','*X^2Y')
    if polylist[i] == 'YYY':
        polylist[i]=polylist[i].replace('YYY','*Y^3')
    if polylist[i] == 'YZ':
        polylist[i]=polylist[i].replace('YZ','*YZ')
    if polylist[i] == 'XZ':
        polylist[i]=polylist[i].replace('XZ','*XZ')
    if polylist[i] == 'XXYY':
        polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
    if polylist[i] == 'XXXY':
        polylist[i]=polylist[i].replace('XXXY','*X^3Y')
    if polylist[i] == 'XZZ':
        polylist[i]=polylist[i].replace('XZZ','*XZ^2')
    if polylist[i] == 'YXYY':
        polylist[i]=polylist[i].replace('YXYY','*XY^3')
    if polylist[i] == 'YXXY':
        polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
    if polylist[i] == 'YZZ':
        polylist[i]=polylist[i].replace('YZZ','*YZZ')
    if polylist[i] == 'ZXXY':
        polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
    if polylist[i] == 'ZXYY':
        polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
    if polylist[i] == 'ZZZ':
        polylist[i]=polylist[i].replace('ZZZ','*Z^3')
if polylist[0] == polylist[4]:
    coefficient[0] = int(coefficient[0])+int(coefficient[4])
    del polylist[4]
    del coefficient[4]
for i in range(len(polylist)):#以下整理出answer。
    print(coefficient[i],polylist[i],sep='',end='')
#problem.2 #(2*X+3*Y+4*Z)(XY^2+X^2Y+Z^2)
polynomials = input('Input the polynomials:')
polynomials_lstrip = polynomials.strip('(')#將括號拆開
polynomials_strip =polynomials_lstrip.strip( ')')#將括號拆開
y = polynomials_strip.replace('-','+-')#以'+-'取代'-'
x = y.split(')(')
for k in range(len(x)):
    x[k] = x[k].split('+')
for i in range(len(x)):
    for j in range(len(x[i])):#以下將相乘之未知數以次方表示
        if x[i][j] == 'X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j] == '-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
        if x[i][j] == 'Z':
            x[i][j]=x[i][j].replace('Z','1*Z')
        if x[i][j] == 'X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j] == '-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*YY')
        if x[i][j] == 'X^2Y':
            x[i][j]=x[i][j].replace('X^2Y','1*XXY')
        if x[i][j] == 'XY^2':
            x[i][j]=x[i][j].replace('XY^2','1*XYY')
        if x[i][j] == 'Z^2':
            x[i][j]=x[i][j].replace('Z^2','1*ZZ')
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = x[i][j].split('*')#以'*'分隔資料
        for idx1 in range(len(x[i][j])):
            if x[i][j][idx1] == 'X^2':
                x[i][j][idx1]=x[i][j][idx1].replace('X^2','XX')
            if x[i][j][idx1] == 'Y^2':
                x[i][j][idx1]=x[i][j][idx1].replace('Y^2','YY')
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j][0] = int(x[i][j][0])
polylist,coefficient=[],[]
for i in range(len(x[0])):
    for j in range(len(x[1])):
        coefficient.append(x[0][i][0]*x[1][j][0])
        polylist.append(x[0][i][1]+x[1][j][1])
for i in range(len(coefficient)):#整理未知數的係數
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 2:
        coefficient[i] = '+2'
    if coefficient[i] == -1:
        coefficient[i] = '-1'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
    if coefficient[i] == 2:
        coefficient[i] = '+2'
    if coefficient[i] == 3:
        coefficient[i] = '+3'
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
for i in range(len(polylist[:])):#以下將相乘之未知數以次方表示
    if polylist[i] == 'XXX':
        polylist[i]=polylist[i].replace('XXX','*X^3')
    if polylist[i] == 'XYY':
        polylist[i]=polylist[i].replace('XYY','*XY^2')
    if polylist[i] == 'YXX':
        polylist[i]=polylist[i].replace('YXX','*X^2Y')
    if polylist[i] == 'YYY':
        polylist[i]=polylist[i].replace('YYY','*Y^3')
    if polylist[i] == 'XZ':
        polylist[i]=polylist[i].replace('XZ','*XZ')
    if polylist[i] == 'YZ':
        polylist[i]=polylist[i].replace('YZ','*YZ')
    if polylist[i] == 'XXYY':
        polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
    if polylist[i] == 'XXXY':
        polylist[i]=polylist[i].replace('XXXY','*X^3Y')
    if polylist[i] == 'XZZ':
        polylist[i]=polylist[i].replace('XZZ','*XZ^2')
    if polylist[i] == 'YXYY':
        polylist[i]=polylist[i].replace('YXYY','*XY^3')
    if polylist[i] == 'YXXY':
        polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
    if polylist[i] == 'ZXXY':
        polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
    if polylist[i] == 'YZZ':
        polylist[i]=polylist[i].replace('YZZ','*YZZ')
    if polylist[i] == 'ZXYY':
        polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
    if polylist[i] == 'ZZZ':
        polylist[i]=polylist[i].replace('ZZZ','*Z^3')
if polylist[0] == polylist[4]:
    coefficient[0] = int(coefficient[0])+int(coefficient[4])
    del polylist[4]
    del coefficient[4]
for i in range(len(polylist)):
    print(coefficient[i],polylist[i],sep='',end='')
#problem.3 #(A+2*B^2)(B+3*C^3)(2*A+B+C)
polynomials = input('Input the polynomial:')
polynomials_lstrip = polynomials.strip('(')#將括號拆開
polynomials_strip =polynomials_lstrip.strip( ')')#將括號拆開
y = polynomials_strip.replace('-','+-')#以'+-'取代'-'
x = y.split(')(')#以')('分隔資料
for idx in range(len(x)):
    x[idx] = x[idx].split('+')
for i in range(len(x)):
    for j in range(len(x[i])):#以下將相乘之未知數以次方表示
        if x[i][j] == 'X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j] == 'B':
            x[i][j]=x[i][j].replace('B','1*B')
        if x[i][j] == 'C':
            x[i][j]=x[i][j].replace('C','1*C')
        if x[i][j] == 'A':
            x[i][j]=x[i][j].replace('A','1*A')
        if x[i][j] == '-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
        if x[i][j] == 'Z':
            x[i][j]=x[i][j].replace('Z','1*Z')
        if x[i][j] == 'X':
            x[i][j]=x[i][j].replace('X','1*X')
        if x[i][j] == '-Y^2':
            x[i][j]=x[i][j].replace('-Y^2','-1*YY')
        if x[i][j] == 'XY^2':
            x[i][j]=x[i][j].replace('XY^2','1*XYY')
        if x[i][j] == 'X^2Y':
            x[i][j]=x[i][j].replace('X^2Y','1*XXY')
        if x[i][j] == 'Z^2':
            x[i][j]=x[i][j].replace('Z^2','1*ZZ')
        if x[i][j] == '2*B^2':
            x[i][j]=x[i][j].replace('2*B^2','2*BB')
        if x[i][j] == '3*C^3':
            x[i][j]=x[i][j].replace('3*C^3','3*CCC')
for i in range(len(x)):
    for k in range(len(x[i])):
        x[i][k] = x[i][k].split('*')
        for idx1 in range(len(x[i][k])):
            if x[i][k][idx1] == 'X^2':
                x[i][k][idx1]=x[i][k][idx1].replace('X^2','XX')
            if x[i][k][idx1] == 'Y^2':
                x[i][k][idx1]=x[i][k][idx1].replace('Y^2','YY')
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j][0] = int(x[i][j][0])
polylist,coefficient=[],[]
for i in range(len(x[0])):
    for j in range(len(x[1])):
        for k in range(len(x[2])):
            coefficient.append(x[0][i][0]*x[1][j][0]*x[2][k][0])
            polylist.append(x[0][i][1]+x[1][j][1]+x[2][k][1])
for i in range(len(coefficient)):#整理未知數的係數
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 2:
        coefficient[i] = '+2'
    if coefficient[i] == -1:
        coefficient[i] = '-1'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
    if coefficient[i] == 3:
        coefficient[i] = '+3'
    if coefficient[i] == 1:
        coefficient[i] = '+1'
    if coefficient[i] == 4:
        coefficient[i] = '+4'
    if coefficient[i] == 6:
        coefficient[i] = '+6'
    if coefficient[i] == 12:
        coefficient[i] = '+12'
for i in range(len(polylist[:])):#以下將相乘之未知數以次方表示
    if polylist[i] == 'XXX':
        polylist[i]=polylist[i].replace('XXX','*X^3')
    if polylist[i] == 'XYY':
        polylist[i]=polylist[i].replace('XYY','*XY^2')
    if polylist[i] == 'YXX':
        polylist[i]=polylist[i].replace('YXX','*X^2Y')
    if polylist[i] == 'YYY':
        polylist[i]=polylist[i].replace('YYY','*Y^3')
    if polylist[i] == 'XZ':
        polylist[i]=polylist[i].replace('XZ','*XZ')
    if polylist[i] == 'YZ':
        polylist[i]=polylist[i].replace('YZ','*YZ')
    if polylist[i] == 'XXXY':
        polylist[i]=polylist[i].replace('XXXY','*X^3Y')
    if polylist[i] == 'XXYY':
        polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
    if polylist[i] == 'XZZ':
        polylist[i]=polylist[i].replace('XZZ','*XZ^2')
    if polylist[i] == 'YXYY':
        polylist[i]=polylist[i].replace('YXYY','*XY^3')
    if polylist[i] == 'YXXY':
        polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
    if polylist[i] == 'YZZ':
        polylist[i]=polylist[i].replace('YZZ','*YZZ')
    if polylist[i] == 'ZXYY':
        polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
    if polylist[i] == 'ZXXY':
        polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
    if polylist[i] == 'ZZZ':
        polylist[i]=polylist[i].replace('ZZZ','*Z^3')
    if polylist[i] == 'BBCCCB':
        polylist[i]=polylist[i].replace('BBCCCB','*B^3C^3')
    if polylist[i] == 'BBCCCC':
        polylist[i]=polylist[i].replace('BBCCCC','*B^2C^4')
    if polylist[i] == 'BBCCCA':
        polylist[i]=polylist[i].replace('BBCCCA','*AB^2C^3')
    if polylist[i] == 'BBBC':
        polylist[i]=polylist[i].replace('BBBC','*B^3C')
    if polylist[i] == 'BBBB':
        polylist[i]=polylist[i].replace('BBBB','*B^4')
    if polylist[i] == 'BBBA':
        polylist[i]=polylist[i].replace('BBBA','*AB^3')
    if polylist[i] == 'ACCCC':
        polylist[i]=polylist[i].replace('ACCCC','*AC^4')
    if polylist[i] == 'ACCCB':
        polylist[i]=polylist[i].replace('ACCCB','*ABC^3')
    if polylist[i] == 'ACCCA':
        polylist[i]=polylist[i].replace('ACCCA','*A^2C^3')
    if polylist[i] == 'ABB':
        polylist[i]=polylist[i].replace('ABB','*AB^2')
    if polylist[i] == 'ABC':
        polylist[i]=polylist[i].replace('ABC','*ABC')
    if polylist[i] == 'ABA':
        polylist[i]=polylist[i].replace('ABA','*A^2B')
if polylist[0] == polylist[4]:
    coefficient[0] = int(coefficient[0])+int(coefficient[4])
    del polylist[4]
    del coefficient[4]
for i in range(len(polylist)):
    print(coefficient[i],polylist[i],sep='',end='')
