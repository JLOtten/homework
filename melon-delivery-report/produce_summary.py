from concurrent.futures import process


def process_melon_delivery_report(daily_file):
    """This processes the melon delivery report by daily file"""
    the_file = open(daily_file) #this opens the daily file and saves it to a variable
    for line in the_file: #iterates through each line in the file
        line = line.rstrip() #removes extra spaces at the end of a line
        words = line.split('|')#this splits each line into a 3 part list (melon, count, amount)

        melon = words[0] #calls word at index 0, saves it to variable
        count = words[1]#calls word at index 1, saves it to variable
        amount = words[2]#calls word at index 2, saves it to variable

        print(f"Delivered {count} {melon}s for total of ${amount}")#f string that prints a sentence listing three variables
    the_file.close() #closes file


print("Day 1")
process_melon_delivery_report("um-deliveries-day-1.txt") #calling the function 3 times, passing different file for each day

print("Day 2")
process_melon_delivery_report("um-deliveries-day-2.txt")

print("Day 3")
process_melon_delivery_report("um-deliveries-day-3.txt")

