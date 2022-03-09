r,c,word=input().split(' ',2)
r,c=map(int,[r,c])
length=r*c
word_list=list(word)

#将字母转换为二进制数字
word_number_list=list(range(len(word_list)))
half_bin=list(range(len(word_list)))
word_number_bin=list(range(len(word_list)))
for j in range(len(word_list)):
    if word_list[j]==' ':
        word_number_list[j]=0
    else:
        word_number_list[j]=ord(word_list[j])-64
    half_bin[j]=bin(word_number_list[j])[2:]
    word_number_bin[j]=half_bin[j].rjust(5,'0')

#将字符串list转换为int
j=0
word_int=list(range(5*len(word_list)))
for i in range(len(word_number_bin)):
    for x in word_number_bin[i]:
        word_int[j]=int(x)
        j+=1

#填充矩阵
d=[[0]*c for i in range(r)]
row_top=0
row_bottom=r-1
column_top=0
column_bottom=c-1
j=0
word_int = [i for i in range(500)]
while row_top < row_bottom and j<len(word_int) and column_top< column_bottom :
    # 向右移动，横坐标不变，纵坐标+1
    i = column_top
    while i < column_bottom and j<len(word_int):
      d[row_top][i] = word_int[j]
      i += 1
      j += 1
    # 向下移动，纵坐标不变，横坐标+1
    i = row_top
    while i < row_bottom and j<len(word_int):
      d[i][column_bottom] = word_int[j]
      i += 1
      j += 1
    # 向左移动，横坐标不变，纵坐标-1
    i = column_bottom
    while i > column_top and j<len(word_int):
      d[row_bottom][i] = word_int[j]
      i -= 1
      j += 1
    # 向上移动，纵坐标不变，横坐标-1
    i = row_bottom
    while i > row_top and j<len(word_int):
      d[i][column_top] = word_int[j]
      i -= 1
      j += 1
    column_top += 1
    row_top += 1
    column_bottom -= 1
    row_bottom -= 1
if row_top != row_bottom and j<len(word_int) and column_top== column_bottom :
    i = row_top
    while i <= row_bottom and j<len(word_int):
        d[i][column_bottom] = word_int[j]
        i += 1
        j += 1
elif row_top == row_bottom and j<len(word_int) and column_top != column_bottom :
    i = column_top
    while i <= column_bottom and j<len(word_int):
        d[row_top][i] = word_int[j]
        i += 1
        j += 1

#输出结果
for i in range(r):
    for o in range(c):
        print(d[i][o],end=' ')
    print('\n')


