name =  input (" Enter Your Name : \n\t")

sp_count = name.count(" ")
name_toal = int (len(name) - sp_count) 

print (f"yor name {name} have {sp_count} Space and have {name_toal} Digits")