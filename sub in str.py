def sub_co(string,sub):
    co=0
    #for i in range(0,len(string)):
        #if string[i:len(string)].startswith(sub):
    for i in range(len(string)-len(sub)+1):
        if (string[i:i+len(sub)] == sub):
            co+=1
    return co
string=input().strip()
sub=input().strip()
count=sub_co(string,sub)
print(count)