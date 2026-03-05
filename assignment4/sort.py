# a = list([])
# while(True):
#     tmp = input("Enter your number: ")
#     try:
#         tmp = int(tmp)
#     except:
#         break
#     a.append(tmp)

# a.sort(reverse=True)
# if(len(a) >= 5):
#     print(a[:5])
# else:
#     print("Amount of numbers don't have more than 5 numbers")


# Write a program that asks the user to enter numbers until they input an empty string to quit. 
# At the end, the program prints out the five greatest numbers sorted in descending order. 
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# làm thế nào để người dùng nhập từng lần cho tới khi họ enter(tức là chuỗi rỗng)
# mỗi lần người dùng nhập thì em thêm giá trị vừa nhập đó cho mảng nếu giá trị vừa nhập là rỗng thì break
# in ra 5 số lớn nhất từ lớn tới nhỏ 

#nguyên tố là số chia hết cho 1 và chính nó
# để viết được 1 chương trình kiểm tra số nguyên tố
# thì mình phải duyệt từng giá trị từ 2 tới n - 1 nếu nó chia hết cho 1 số nằm trong đó thì kết luận luôn là không phải snt
# nếu vòng for chạy được hết thì chính là số nguyên tố
# tạo 1 biến gán giá trị đúng sai, khởi tạo nó là đúng
# nếu chia hết thì giá trị của biến đó trở thành sai và break
# nếu vượt được vòng for và nó vẫn là giá trị đúng thì kết luận là số Prime number
# i chay tu [2, 3, 4, 5, 6, 8]
# n = 9
# tao 1 bien check = True
# if(n % i == 0) -> check = False + break
# sau khi chay xong for(duoi vong for) if(check == True) -> Prime number

#parameter
#Write a function that gets a list of integers as a parameter.
#The function returns the sum of all the numbers in the list. 
# For testing, write a main program where you create a list, call the function, and print out the value it returned.
def tinh_tong(arr:list):
    tong = 0
    for i in arr:
        tong += i
    return tong 

if __name__ == "__main__":
    arr = [1, 23, 3, 4]
    print(tinh_tong(arr))
