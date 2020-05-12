filename = input("Enter name of a text file (e.g. test.txt): ")

contents = []

try:
    
    with open(filename) as infile:
        for line in infile:
            contents.append(line.rstrip("\n"))
            
    if len(contents) == 0:
        print("There is nothing to view in this file.")
    else:
        print("The file contains", len(contents), "lines.")
        linenumber = int(input("Type a line number to view (integer): "))
        print(linenumber, ":", contents[linenumber - 1])
        
except IOError as ioError:
    
    print(ioError)
    
except ValueError as valError:
    
    print(valError)
    
except IndexError as idxError:
    
    print(idxError)
