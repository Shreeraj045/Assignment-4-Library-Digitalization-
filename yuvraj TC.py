from hash_table import *
from dynamic_hash_table import *


st = HashMap("Double", (40, 35, 17, 43))
# st.insert(('yuvraja','1'))
# # print(st.__str__())
# st.insert(('yuvrajaaa',"2"))
# print(st.__str__())
# st.insert(('yuvrajaaa',"4"))
# print(st.__str__())
# st.insert(('yuvraja','10'))
# print(st.__str__())
# st.insert(('yuvrajaaaa','10'))
# print(st.__str__())
# st.insert(('yuvrajaaaa','2'))
# print(st.__str__())


k = 'adventures'
print(st.get_slot(k))
print(st.get_step(k))





# print(st.__str__())
# print(st.get_slot('Yuvrajbbb'))
# print(st.polynomial_accumulation_hash("Z",1))


# import random
# lis = []
# for i in range(9):
#     lis.append(random.randint(10,99))
# print(lis)
#
# map1 = HashMap("Chain",(11,10))
# map1.insert(("Rahul","Dumbfuck"))
# map1.insert(("Hardik","Edlor"))
# map1.insert(("Yash","Clown"))
# map1.insert(("Yash","God?"))
# map1.insert(("Pulkit","Sir"))
# map1.insert(("Ayush","Tiger"))
# map1.insert(("Praveen","Power"))
# map1.insert(("Atharva","Don"))
# map1.insert(("Karthik","Rejati"))
# print(map1)
#
# map2 = HashSet("Chain",(11,10))
# map2.insert("Rahul")
# map2.insert("Hardik")
# map2.insert("Yash")
# map2.insert("Yash")
# map2.insert("Pulkit")
# map2.insert("Ayush")
# map2.insert("Praveen")
# map2.insert("Atharva")
# map2.insert("Karthik")
# print(map2)
#
# map1 = HashMap("Linear",(11,10))
# map1.insert(("Rahul","Dumbfuck"))
# map1.insert(("Hardik","Edlor"))
# map1.insert(("Yash","Clown"))
# map1.insert(("Yash","God?"))
# map1.insert(("Pulkit","Sir"))
# map1.insert(("Ayush","Tiger"))
# map1.insert(("Praveen","Power"))
# map1.insert(("Atharva","Don"))
# map1.insert(("Karthik","Rejati"))
# print(map1)
#
# map2 = HashSet("Linear",(11,10))
# map2.insert("Rahul")
# map2.insert("Hardik")
# map2.insert("Yash")
# map2.insert("Yash")
# map2.insert("Pulkit")
# map2.insert("Ayush")
# map2.insert("Praveen")
# map2.insert("Atharva")
# map2.insert("Karthik")
# print(map2)
#
# map1 = HashMap("Double",(11,13,7,10))
# map1.insert(("Rahul","Dumbfuck"))
# map1.insert(("Hardik","Edlor"))
# map1.insert(("Yash","Clown"))
# map1.insert(("Yash","God?"))
# map1.insert(("Pulkit","Sir"))
# map1.insert(("Ayush","Tiger"))
# map1.insert(("Praveen","Power"))
# map1.insert(("Atharva","Don"))
# map1.insert(("Karthik","Rejati"))
# print(map1)
#
# map2 = HashSet("Double",(11,13,7,10))
# map2.insert("Rahul")
# map2.insert("Hardik")
# map2.insert("Yash")
# map2.insert("Yash")
# map2.insert("Pulkit")
# map2.insert("Ayush")
# map2.insert("Praveen")
# map2.insert("Atharva")
# map2.insert("Karthik")
# print(map2)

# Output :-
# (Praveen,Power);(Atharva,Don)|(Rahul,Dumbfuck);(Hardik,Edlor)|<EMPTY>|<EMPTY>|<EMPTY>|(Yash,Clown);(Ayush,Tiger)|<EMPTY>|(Karthik,Rejati)|<EMPTY>|(Pulkit,Sir)
# Praveen;Atharva|Rahul;Hardik|<EMPTY>|<EMPTY>|<EMPTY>|Yash;Ayush|<EMPTY>|Karthik|<EMPTY>|Pulkit
# (Praveen,Power)|(Rahul,Dumbfuck)|(Hardik,Edlor)|(Atharva,Don)|<EMPTY>|(Yash,Clown)|(Ayush,Tiger)|(Karthik,Rejati)|<EMPTY>|(Pulkit,Sir)
# Praveen|Rahul|Hardik|Atharva|<EMPTY>|Yash|Ayush|Karthik|<EMPTY>|Pulkit
# (Praveen,Power)|(Rahul,Dumbfuck)|<EMPTY>|(Karthik,Rejati)|(Atharva,Don)|(Hardik,Edlor)|<EMPTY>|(Yash,Clown)|(Ayush,Tiger)|(Pulkit,Sir)
# Praveen|Rahul|<EMPTY>|Karthik|Atharva|Hardik|<EMPTY>|Yash|Ayush|Pulkit