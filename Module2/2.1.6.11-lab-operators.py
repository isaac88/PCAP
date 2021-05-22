hora = int(input("Start time (hours): "))
min = int(input("Start minute (minutes): "))
dura = int(input("Event duration (minutes): "))
min = min + dura # find the total minutes
hora = hora + min // 60 # find the number of hours hidden in the minutes and update the hours
min = min % 60 # correct the minutes to be in a range of (0..59)
hora = hora % 24 # correct the hours to be in a range of (0..23)
print(hora, ":", min, sep='')