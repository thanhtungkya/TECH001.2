course_code = input()

def check_course_code(course_code:str)->bool:
    count = 0
    for c in course_code:
        if(c.isupper()):
            count += 1
    if(count >= 2):
        return True
    else:
        return False

if __name__ == "__main__":
    if(check_course_code(course_code)):
        print("True")
    else:
        print("False")