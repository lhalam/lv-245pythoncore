day = int(input("Vedit dey years:   "))
if 0 <= day <= 365:
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    print (week[day%7])