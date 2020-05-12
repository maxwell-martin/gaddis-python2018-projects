def get_month(mm):
    months = { "01":"January",
               "02":"February",
               "03":"March",
               "04":"April",
               "05":"May",
               "06":"June",
               "07":"July",
               "08":"August",
               "09":"September",
               "10":"October",
               "11":"November",
               "12":"December" }
    return months[mm]

str_date = input("Enter date in mm/dd/yyyy format: ")

date_list = str_date.split('/')

print(get_month(date_list[0]) + ", " + date_list[1] + " " + date_list[2])
               
