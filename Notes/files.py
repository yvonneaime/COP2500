# Yvonne Aime
# COP2500C
# July 24 2023
# File Notes 

# Opens a file for writing
file_out = open("sample.txt","w")

file_out.write("Hello")
file_out.write("Did I sing\n")

rain = int[1.5, 2,5 0, 4,1]
for day in range(len(rain)):
    file_out.write(str(day+1)+ "-"+str(rain[day]+"inches\n"))


# Closes the file``
file_out.close()

file_open = open("input_file.txt", "r")
line1 = file_open.readline()
line1 = line1.strip()
print(line1)

line2 = file_open.readline()
line2 = line2.strip()
print(line2)

line3 = file_open.readline().strip()
print(line3)                        

