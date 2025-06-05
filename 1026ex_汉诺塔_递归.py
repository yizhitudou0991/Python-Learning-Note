def hanoi(n,x,y,z):
    if n ==1:
        print(x,'->',z) # 如果只有一层，直接将金片从x移动到z
    else:
        hanoi(n-1,x,z,y) # 把x上的n-1个金片移动到y
        print(x,'->',z) # 把最底下的金片从x移动到z
        hanoi(n-1,y,x,z) # 把y上的n-1个金片移动到z上

n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'A','B','C')