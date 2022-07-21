print("1：长方形计算")
print("2：圆形计算")
print("3：正方形计算")
print("4：梯形计算")
mode=input("选择模式：")
if mode=="1":
    a=input("请输入长方形的长：")
    b=input("请输入长方形的宽：")
    a=int(a)
    b=int(b)
    c=(a+b)*2
    s=c*k
    print("长方向的周长是：",c)
    print("长方形的面积是：",s)
elif mode=="2":
    print("-----圆计算器-----")
    print("选择你的模式")
    print("1：圆的面积")
    print("2：圆的周长")
    mode1=input("输入模式序号：")
    if mode1=="1":
        print("1：半径")
        print("2：直径")
        smode=input("输入模式序号：")
        if smode=="1":
            num1=input("输入半径：")
            pai=input("输入 Π 值：")
            ans=float(num1)*float(num1)*float(pai)
            ans1=float(num1)*float(num1)
            print("半径为",num1,"的圆的面积是：",ans,",",ans1,"Π")
        if smode=="2":
            num1=input("输入直径：")
            pai=input("输入 Π 值：")
            num2=float(num1)/2
            ans=float(num2)*float(num2)*float(pai)
            ans1=float(num2)*float(num2)
            print("直径为",num1,"的圆的面积是：",ans,",",ans1,"Π")
    if mode1=="2":
        print("1：半径")
        print("2：直径")
        cmode=input("输入模式序号：")
        if cmode=="1":
            num1=input("输入半径：")
            pai=input("输入 Π 值：")
            num2=float(num1)*2
            ans=float(num2)*float(pai)
            ans1=num2
            print("半径为",num1,"的圆的周长是：",ans,",",ans1,"Π")
        if cmode=="2":
            num1=input("输入直径：")
            pai=input("输入 Π 值：")
            ans=float(num1)*float(pai)
            ans1=float(num1)
            print("直径为",num1,"的圆的周长是：",ans,",",ans1,"Π")
elif mode=="3":
    a=input("正方形的边长是：")
    c=float(a)*4
    s=float(a)**2
    print("正方形的周长是：",c)
    print("正方形的面积是：",s)
elif mode=="4":
    a=input("输入梯形的上底：")
    b=input("输入梯形的下底：")
    h=input("输入梯形的高：")
    a=int(a)
    b=int(b)
    h=int(h)
    s=(a+b)*h/2
    print("梯形的面积是：",s)
