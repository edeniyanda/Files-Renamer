import os

os.chdir(r"C:\Users\iyanda\Desktop\Eden\Tachyons\Advanced Python Series")


for file in os.listdir():
    f = os.path.splitext(file)
    file_name, file_extention = f
    file_name = file_name[0:(len(file_name) - 6)]
    file_name = (list(file_name))
    file_name = [i if i !="_" or i =="-" else " " for i in file_name]
    file_name = "".join(file_name)
    f_name= file_name.split("-")
    f_title = f_name[0]
    if f_title == "d":
        continue
    f_remains = f_name[1]
    f_remains = f_remains.split("#")
    f_index, f_heading = f_remains[1], f_remains[0]
    f_title = f_title.strip()
    f_index = f_index.strip().zfill(2)
    f_heading = f_heading.strip()
    
    new_name = f"{f_index} {f_title} - {f_heading}{file_extention}"
    
    os.rename(file, new_name)

print("Files Renamed Succesfully!")
    
    
        