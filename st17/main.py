from st17.Menu import Menu
from st17.ListCommand import *

def main():
    m=Menu()
    l=[m.AddDishMenu,m.AddVipDishMenu,m.EditDishMenu,m.ClearDishMenu,m.ShowDishMenu,m.SafeDishMenu,m.LoadDishMenu]
    while (True):
        i=int(ShowList())
        if ((i>len(l)) or (i<0)):
            break
        MenuFunction(l[i])

if __name__ == "__main__":
    main()
