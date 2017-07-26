import csv

def create_record(number_of_rec):

    while number_of_rec:
        install_date = raw_input("Enter the Install Date: ")
        device_number = raw_input("Enter the Device Number: ")
        serv_address = raw_input("Enter the Service Address: ")
        serv_city = raw_input("Enter Service City : ")

        if install_date and device_number and serv_address and serv_city:
            record_list = [install_date, device_number, serv_address, serv_city]

            with open("C:\Path\to\File", "ab") as wf:
                 writer = csv.writer(wf)
                 writer.writerow(record_list)
        number_of_rec -= 1

def display_record(option):

    with open("C:\Path\to\File", "r") as rf:
        reader = csv.reader(rf)
        if option == 2:
            for row in reader:
                print "  ".join(row)
        elif option == 3:
            search_feild = raw_input("Search by Install Date, Device Number, Service Address,City,or State  :")
            for row in reader:
                if search_feild in row:
                    print "  ".join(row)


def main():
    print("1. Add to the file")
    print("2. Display all the data from the file")
    print("3. Search for particular data")
    print("0. To Exit")

    choice = True
    while choice:
        your_choice = input("Enter your choice:")
        if your_choice == 1:
            number_of_rec = input("Enter number of records you want to enter:")    
            create_record(number_of_rec)
        if your_choice == 2:
            display_record(2)
        if your_choice == 3:
            display_record(3)
        if your_choice == 0:
            choice = False

if __name__ == "__main__":
    main()    
