point_list = []
while True:
    student_point = list(map(int, input().split()))
    if student_point == [-1,-1,-1]:
        break
    point_list.append(student_point)
    if (student_point[0]==-1) or (student_point[1]==-1) or (sum(student_point[0:2]) < 30):
        print("F")
    elif (80 <= sum(student_point[0:2])):
        print("A")
    elif (65<=sum(student_point[0:2])) and (sum(student_point[0:2])<80):
        print("B")
    elif (50<=sum(student_point[0:2])) and (sum(student_point[0:2])<65):
        print("C")
    elif (30<=sum(student_point[0:2])) and (sum(student_point[0:2])<50):
        if (student_point[2]>=50):
            print("C")
        else:
            print("D")

