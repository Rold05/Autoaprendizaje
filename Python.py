Fs = float(input("Write the first score: "))
Ss = float(input("Write the Second score: "))
Ts = float(input("Write the Thirth score: "))

avarage = (Fs + Ss + Ts) / 3

if avarage <= 10 and avarage >= 9.0:
    print(f"Your avarage is: {avarage}")
    print("Excelent work!!")
elif avarage < 9.0 and avarage >= 6.0:
    print(f"Your avarage is: {avarage}")
    print("Approve")
elif avarage < 6.0:
    print(f"Your avarage is: {avarage}")
    print("Fail")
else:
    print("Invalid score entered.")
