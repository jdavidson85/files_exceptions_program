print("This program will total and average numbers in your data file.")
filename = input("Enter the name of your data file: ")

try:
    file = open(filename, 'r')
    total = 0
    count = 0
    invalid = 0

    for line in file.readlines():
        line = line.rstrip("\n")
        count += 1

        try:
            i = float(line)
            total += i
            print(format(i, ",.2f"))

        except Exception:
            invalid += 1
            print(f"Line {count} with a value of {line} was invalid.")

    print("Total: " + format(total, "27,.2f"))
    print("Number of entries: ", format(count, "15,.0f"))
    print("Average: ", format((total/count), "25,.2f"))

except Exception:
    print("Unable to access the file: ", filename)
