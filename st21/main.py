from st21.car_park import car_park
from st21.modul_show_run import *

def main():
    cp=car_park()
    cpf={"add_car":cp.add_car,
         "add_truck":cp.add_truck,
         "edit":cp.edit,
         "clear":cp.clear,
         "show":cp.show,
         "safe":cp.safe,
         "load":cp.load}
    sm=show_menu()
    while(True):
        if (str(sm)=="exit"):
                break
        else:
            try:
                run_f_car_park(cpf[str(sm)])
                sm=show_menu()
            except:
                sm=show_menu()

if __name__ == "__main__":
    main()
