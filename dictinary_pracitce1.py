# program to retreive the score a player made using dict
x = dict()  # or x = {} empty dict
print('how may Player: ',end='') # end will prevent the print to go to next line.
n= int(input())
for i in range(n):
    print('Enter the player %d: '%i,end='')
    k = input()
    print('enter the value: ',end='')
    v = int(input())
    x.update({k:v})
for pname in x.keys(): #retreiving the player names
    print(pname)
print('Enter Player name: ', end='')
name = input()
runs = x.get(name,-1) # -1 is required in-case if we don't key it will display -1.
if runs == -1:
    print('Player not found')
else:
    print('{} made {}'.format(name,runs))




