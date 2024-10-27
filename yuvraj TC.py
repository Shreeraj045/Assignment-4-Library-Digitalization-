from hash_table import *
from dynamic_hash_table import *


st = DynamicHashSet("Double", (40, 35, 17, 37))
lis = "To Kill a Mockingbird addresses injustice and race through the eyes of young Scout Finch".split()
for i in lis:
    st.insert(i)
    print(i+" | inserted  -->",st)

# st.insert('yuvraja')
# print(st.__str__())
# st.insert('yuvrajaaa')
# print(st.__str__())
# st.insert('yuvrajaba')
# print(st.__str__())
# st.insert('yuvrajabc')
# print(st.__str__())
# st.insert('pramodaab')
# print(st.__str__())
# # st.insert('pramodaaaaaa')
# print(st.__str__())
# st.insert('pramodaaa')
# # print(st.__str__())
k = 'to'
print(st.get_slot(k))
print(st.get_step(k))


# st.insert('yuvraj')
# print(st.__str__())



# print(st.__str__())
# print(st.get_slot('Yuvrajbbb'))
# print(st.polynomial_accumulation_hash("Z",1))


# import random
# lis = []
# for i in range(9):
#     lis.append(random.randint(10,99))
# print(lis)