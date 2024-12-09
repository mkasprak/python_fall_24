# Assignment: Processing Files
# PE2 Module 4.3 Working with Real Files

"""
Open the file sales_totals in read mode (Download: sales_totals.txt Download sales_totals.txt)
Read in all the lines using a loop
Strip the newline symbol and convert each line to a float
Add each number to the running total
Count the number of lines
Format and display each number
Outside of the loop, format and display the total, the count, and the average
Do this using a main function 
Use try and except statements to handle file errors"""

# define main function


def main():
    try:
        # empty list to store sales totals
        sales_totals = []
        # variable for running total
        running_total = 0.0
        # variable for line count
        line_count = 0

        # open the file in read mode
        my_sales = open("sales_totals.txt", "r")

        # loop through each line in sales_totals.txt file
        for line in my_sales:

            # strip whitespace and convert to float
            sale = float(line.strip())
            # append to sales_total list

            sales_totals.append(sale)

            # compute running total and count lines total
            running_total += sale
            line_count += 1
            sale_avg = (running_total/line_count)

        # printed list of data in sales_totals.txt file
        print(f"\nData from sales_totals.txt in a List Format:\n\n{
              sales_totals}\n")

        print("Assignment Output:\n")
        # added commas and decimal place formatting to match sample output
        print(f"Total: {running_total:,.2f}\n")
        # doesn't need decimal place formatting did not use.
        print(f"Number of entries: {line_count}\n")
        # print(f"Average: {running_total/line_count:,.2f}\n") # added commas and decimal place formatting to match sample output #TODO should this be a variable it worked to print as is
        # commented above line and redid as this should be a variable even though it worked the other way too.
        print(f"Average: {sale_avg:,.2f}\n")

        # always close the file if you open the file
        my_sales.close()

    except Exception as e:
        # TODO am I suppose to do something with except IOError as well? Need to figure that out.
        print(f"An error occured: {e}")


# call the main function
main()
