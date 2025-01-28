#Write a python function, which create a dictionary
#for given number N, where keys are numbers from
#1 to N, and values are cubs of that numbers
def creat_cubes(N):
    cubes_dict = {}
    for i in range(1, N+1):
        cubes_dict[i] = i**3
    return cubes_dict
print(creat_cubes(5))