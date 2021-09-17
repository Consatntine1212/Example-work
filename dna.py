import csv
import sys

# I used a lot of tutorials and guides from
# https://www.youtube.com/watch?v=5CEsJkKhS78&t=496s&ab_channel=KrisJordan
# https://realpython.com/lessons/reading-csvs-pythons-csv-module/
# https://www.geeksforgeeks.org/window-sliding-technique/
# https://www.geeksforgeeks.org/window-sliding-technique/
def main():
    #Checking if corect

    if len(sys.argv) != 3:
        sys.exit("usage : python dna.py Filename.csv Filename.txt")
    #opening ferst file and saving in in a string
    text_file = open(sys.argv[2], "r")
    dna_text = text_file.read()
    text_file.close()

    #Opening csv file and saving in in a dictionary
    database_file = open(sys.argv[1], "r")
    database_reader = csv.DictReader(database_file)
    #for row in database_reader:
    #   print(row)


    #make a list of sequences
    with open(sys.argv[1]) as csvFile:
        reader = csv.reader(csvFile)
        sequencis_list = next(reader)
    sequencis_list.pop(0)
    #print(sequencis_list[0])
    Final = {}
    for strand in sequencis_list:
         Final[strand] = get_max_of_strund( strand , dna_text )

    #print(Final)
    much = 0


    # Check for much and print resoult
    for row in database_reader:
        much = 0
        for strand in sequencis_list:
            if Final[strand] == int(row[strand]):
                much += 1

            if much == len(sequencis_list):
                # https://realpython.com/lessons/reading-csvs-pythons-csv-module/
                print(f"{row['name']}")
                database_file.close()
                exit()

    print("No match")
    database_file.close()
    exit()



# def to get the max for evry one string
# I used the Window Sliding Technique from https://www.geeksforgeeks.org/window-sliding-technique/
def get_max_of_strund( dna_strund , dna_sequence ):
    length = len(dna_sequence)
    i = 0
    jump = len(dna_strund)
    current_max = 0
    total_max = 0
    while i < length:
        window = dna_sequence[ i : i + jump ]
        if window == dna_strund:
            current_max +=1
            total_max = max( total_max , current_max)
            i += jump
        else:
            current_max = 0
            i += 1
    return(total_max)
main()





