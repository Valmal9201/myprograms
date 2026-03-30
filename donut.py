# My Solution
start = int(input("Number of donuts at beginning of day: "))
events = int(input("Number of events that affect the number of donuts: "))
i = 0
posNeg = ""
change = 0

while i < events:
    posNeg = input("Enter whether donuts were baked or sold (\"+\" = baked, \"-\" = sold: ")
    change = int(input("Enter number of donuts baked or sold: "))
    if (posNeg == "+"):
        start += change
    else:
        start -= change
    i += 1

print(f"The final number of dounts when the shop closes is {start}.")

#In Class Solution
donuts = int(input())
events = int(input())

event_ctr = 0
while event_ctr < events:
    event_type = input() # for +/-
    quantity = int(input())
    if event_type == "+":
        donuts += quantity
    elif event_type == "-":
        donuts -= quantity
    event_ctr += 1
# end while loop
print(donuts)