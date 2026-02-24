dusa = int(input("Enter Dusa's starting size: "))
notRun = True

while notRun:
    yobi = int(input("Enter Yobi's size: "))
    if yobi < dusa:
        dusa += yobi
    else:
        break
print(f"Dusa is size {dusa} when Dusa runs away")