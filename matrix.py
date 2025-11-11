#function for matrix multiplication
def multiply_matrices(A,B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range (len(B)):
                result[i][j]+= A[i][k]*B[k][j]
    return result

#define joint positionms(homogenous coordinates: [x,y,z,1])
joints = [
    [0,0,0,1],#base
    [2,0,0,1],#joint 1
    [4,1,0,1],#joint 2
    [6,1,0,1]#enf effector
]
print("Original joint coordinates:")
for row in joints:
    print(row)

#transformation matrix = rotate 90 degrees around in z axis + translate
theta = 90*3.14159/180 # converts degrees to radians(1,2,0)
cos_t = round(3.14159/2 -(3.14159/2 - 0),5) # approx cos 90 = 0
cos_t = 0
sin_t = 1
transformation_matrix = [
    [cos_t, -sin_t,0,1],
    [sin_t, cos_t,0,2],
    [0,0,1,0],
    [0,0,0,1]
]
print("\n Transformation matrix: ")
for row in transformation_matrix:
    print(row)
#apply transformation: joints x transformation^T
#(We'll transpose transformation_matrix for correct multiplication)
transposed_T = [[transformation_matrix[j][i] for j in range(4)] for i in range(4)]
new_joints = multiply_matrices(joints,transposed_T)
print("\n New Joint Coodrinates after transformation: ")
for row in new_joints:
    print(row)