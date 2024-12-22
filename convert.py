def con(n):
    print(f"Distance in feet{n}")
    inc = n*12
    print(f"Inches : {inc}")
    yard = n/3
    print(f"Yard : {yard}")
    mile = n/5280
    print(f"mile : {mile}")
a = int(input("Enter feet:"))
con(a)