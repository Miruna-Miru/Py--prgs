#expendtirue calculation
tot=int(input("enter total amount : "))
tans=input("Have you travelled today? ")
y="yes"
if tans==y:
    tr=int(input("How much you spent for train? "))
    bu=int(input("How much you spent for bus? "))
    t_sum=tr+bu
    print(f"You have spent Rs{t_sum} for travelling")
else:
    print("No expenses on travel")
    t_sum=0
mans=input("Have you went to the market? ")
if mans==y:
    ve=int(input("How much you spent for vegetables? "))
    fr=int(input("How much you spent for fruits? "))
    m_sum=ve+fr
    print(f"You have spent Rs{m_sum} in the market")
# nans=input("Have you bought any non veg? ")
# if nans==y:
#         me=int(input("How much you spent for meat? "))
#         fi=int(input("how much you spent on fish? "))
#         m1_sum=m+me+fi
#         print(f"You have spent Rs{m_sum} in the market")
else:
    print("You have not spent money on the market")
    m_sum=0
sans=input("Have you went out for shopping? ")
if sans==y:
    dre=int(input("How much you spent for dress? "))
    je=int(input("How much you spent for jewels? "))
    s_sum=dre+je
    print(f"You have spent Rs{s_sum} for jewls and dress")
else:
    print("You have not spent money for jewels and dress")
    s_sum=0
hans=input("Do you eat anything outside? ")
if hans==y:
    be=int(input("How much the beverage coast? "))
    fo=int(input("how much you spent for your B'fast,lunch,dinner"))
    h_sum=be+fo
    print(f"You have spent Rs{h_sum} for food items")
else:
     print("You have not spent money for food")
     h_sum=0
spent=h_sum+s_sum+m_sum+t_sum
print("you have spent RS",spent)
rem=tot-spent
print(f"The balance is Rs{rem}")
    
    
    
    

    

