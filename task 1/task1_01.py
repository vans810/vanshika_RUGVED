def triple_and(par1, par2, par3):
    if(par1==True and par2==True and par3==True):
        return True
    else:
        return False
par1=10<12
par2=12==12
par3='and'=='anf'
print(triple_and(par1,par2,par3))