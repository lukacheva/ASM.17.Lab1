from .ModelAgency import ModelAgency 

agency=ModelAgency()
menu = {"1":("Add model", agency.insertModel),
        "2":("Add Super model", agency.insertSuperModel),
        "3":("Edit", agency.edit),
        "4":("Delete", agency.delete),
        "5":("Show agency", agency.showModelAgency),
        "6":("Read agency from file", agency.read_file),
        "7":("Write agency to file", agency.write_file),
        "8":("Clear", agency.clean),
        "9":("Exit", None)}
def main():
    while True:
        print('')
        print('Menu:')
        for k in range(1,10):
            print(k,"-",menu[str(k)][0])
        x = input()
        if int(x)==9:
            break
        if int(x)>=1 and int(x)<9:
            menu[x][1]()
        else:
            print('Error! Choose other number')
        

if __name__ == "__main__":
    main()
    
