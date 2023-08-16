def cal():
    opp=(input("enter opperator: "))
    f=int(input("enter a no: "))
    s=int(input("enter second no: "))
    if opp=="+":
        print(f+s)
    elif opp=='-':
        print(f-s)
    elif (opp=='/') and (s!=0):
        print(f/s)
    elif opp=='*':
        print(f*s)
    else:
        print("not supported")
cal()

def full_name(firstname,lastname,middlename=''):
    fullname=firstname+middlename+lastname
    return fullname
