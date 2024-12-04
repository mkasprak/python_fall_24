def main():  # reads the file and increments a counter and adds the numbers to a total
    total = 0
    count = 0
    try:
        with open('sales.txt', 'r') as file:
            line = True
            while line:
                line = file.readline()
                line = line.strip()
                if line:  # this makes sure it doesnt try to pass an empty line as that makes the program blow up
                    print(f"${float(line):,.2f}")
                    count += 1  # increments counter
                    # below this adds the value to the total each time
                    total += float(line)
            average = total / count  # averages it for printing
            print(f"{count} sales.")
            print(f"${total:,.2f} in total sales.")
            print(f"${average:,.2f} average sales.")

    except IOError:
        print("An IOError has occurred. File not found.")

    except ValueError:
        # should catch and print bad lines
        print(f"{line} this entry is not a valid sales entry")

    except Exception as e:
        print("an error has occured {e}")  # should catch unknown errors


main()
