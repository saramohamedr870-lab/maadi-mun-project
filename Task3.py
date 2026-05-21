tasks=["doing excercises","studying","playing"]
print("1-add a task    2-show tasks    3-delete a task   4-exit")
userchoice=int(input("choose a number from 1 to 4"))
while userchoice !=4:
    if userchoice ==1:
       usertask=input("write the task you want to add")
       tasks.append(usertask)
    elif userchoice==2:
       print(tasks)
    elif userchoice==3:
        deltask=input("write the task you want to delete")
        tasks.remove(deltask)
    print("1-add a task    2-show tasks    3-delete a task   4-exit")
    userchoice=int(input("choose a number from 1 to 4"))
else:
    print("Exit")