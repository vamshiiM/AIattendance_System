# # # lists are used to store multiple items in single variable
# # name=["vam","mav","shi","ish"]
# # surname=["marri","mar","rri",]
# # print(len(name))
# # print(name)
# # print(name[0],name[2])
# # name.append("vamshi")
# # print(name)
# # name.extend(surname)
# # print(name)
# # #remove item from list
# # name.remove("rri")
# # print(name)
# # #removing the 2nd
# # name.pop(1)
# # print(name)
# # #clearing the contents of list
# # # name.clear()
# # # print(name)
# # # deleting the list
# # # del name
# # # print(name)# This will show error
# #
# # # printing the content of lists
# #
# # for i in range(len(name)):
# #     print(name[i])
# #
# # i=0
# # while i< len(name):
# #     print(name[i])
# #     i +=1
# #
# #
# #
# # #sorting the list alphabetcally
# #
# # name.sort()
# # print(name)
# #
# # # descending order
# # name.sort(reverse=True)
# # print(name)
# #
# # # reversing the order of list
# # name.reverse()
# # print(name)
# #
# # # copying the list
# # new=name.copy()
# # print(new)
# #
# # #joining two lists
# #
# # new_list=new + name
# # print(new_list)
# #
# # count=name.count("vamshi")
# # print(count)
# #
# # # inserting a value at place 1
# # name.insert(1,"apple")
# # print(name)
#
# list1={1,2,3,4,5,6,7}
# list2={2,3,6,7,8,9,10}
#
# def comp(l1,l2):
#   miss2=l1-l2
#   miss1=l2-l1
#
#   return miss2,miss1
#
#
#
# miss2,miss1=comp(list1,list2)
#
# print(miss2)
# print(miss1)
#
#
# li=(1,2,3,4,5,6,7,8,9)
#
# def eo(num):
#     e=0
#     o=0
#     for i in num:
#         if i%2==0 :
#             e +=1
#         else:
#             o+=1
#     return e,o
#
# even,odd=eo(li)
# print("NUMBER OF EVEN IS:",even)
# print("NUMBER FOR ODD IS",odd)
#
#
#
# for i in range(0,5):
#     print("*"*i)
#
# # reversing a list
#
# list=[1,2,3,4,5,6,7]
#
# def reverse(li,num):
#    if num<0 or num>len(list):
#        print("INVALID")
#
#    first=li[:num]
#    second=li[num:]
#
#    new_second=second[::-1]
#
#    return first+new_second
#
# print(f"THIS IS THE LIST",list)
# n=int(input("ENTER THE LOCATION:"))
# print(reverse(li,n))
#
# ### TUPLES ARE ALSO SIMILAR TO LISTS ,BUT THEY ARE UNCHANGEABLE
#
# # SO TO MAKE CHANGES IN THEM YOU HAVE TO CONVERT THE TUPLE INTO LIST
#
# t1=(1,2,3,4,5,6,7,8,9,10)
# l1=[1,2,3,4,5,6,7,8,9,10]
# print(t1)
# print(l1)
#
# #l2=list(t1)
# #print(l2)
#
# t2=tuple(l1)
# print(t2)

##DICTIONARIES##

#THEY ARE USED TO STORE DATA VALUES INTO KEY:VALUE PAIRS
example={'cars':"VOLVO",
         'price':"100000",
         'number':"AF234"
         }

print(example)
for i in example:
    print(i)

l2=[(1,2),(3,4),(5,6)]
t2=tuple(l2)
print(t2)



