def ask():
    pas = input('Enter the password: ')
def password():
    po=list(pas)
    num=[0,1,2,3,4,5,6,7,8,9]
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    schar=[!,@,%,^,&,*]
    print(po)
    for i in po:
        if i in po == num[i]:
            print("Password has been set successfylly")
        else:
            print('Enter the password again with this format Abc+!/@/#/$/%/^/&/*+123: ')
            ask()
pas = input('Enter the password: ')
password()