## Simple Task 1
# Load $x, y$ data from a file and plot it.

# set up plotting and load useful modules 
from TIGISIO import Task1
import sys

## Identify the file via the length of the file
#Get the address of the file
if len(sys.argv) > 1:
    # if the file number is more than one -> get the newest one
    dName = sys.argv[1]
else:
    #if there is only one file -> get the file 'plenty.data'
    dName = "data/plenty.data"
    
if __name__ == '__main__' :
## Motify the entrance of the Main function 
#  if the module is run directly, the code block run;
#  if the module is imported, the code block does not run. 
    #create empty two lists which will hold the data from the file and float-translated couterparts
    List = []    
    #Use the ReadData function to open the file via address and save the data in 'Data' list
    Data = Task1.ReadData(dName) 
    #Use the Split2Float function to split and translate the spring-format data into two-columns and float-format data 
    List = Task1.Split2Float(Data)
    #Use the Visual function to plot the result
    Task1.Visual(List)
    #print(Task1.ReadData.__doc__)

  