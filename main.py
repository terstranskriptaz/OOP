#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 01:42:17 2023

@author: ok
"""
#objeler olusturacagiz classlar icin ve bu objelerle definitionlari cagiracagiz 
from rent import CarRent, BikeRent, Customer

bike=BikeRent(100)
car=CarRent(10)
customer = Customer()

main_menu = True #while döngüsüne girince ilk main menü gelecek

while True:
    if main_menu:
        print("""***** Vehicle Rental Shop *****
              A. Bike Menü 
              B. Car Menü
              Q. Exit
              """)
              #A. = klavyede A ya basti
        main_menü = False
        choice=input("Enter choice:  ")
        
    if choice == "A" or choice == "a":
        print("""
              ***** BIKE MENÜ *****
              1.Display avaliable bikes
              2.Request a bike on hourly basis $ 5
              3.Request a bike on daily basis $ 84
              4.Return a bike
              5.Main Menü
              6. Exit
              """)
        choice = input ("Enter choice: ")
        try:
            choice =int(choice)
        except ValueError:
            print("It is not integer ")
            continue
        if choice == 1:
            bike.displaystock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "B" or choice == "b":
        
        print("""
              ****** CAR MENU*****
              1. Display available cars
              2. Request a car on hourly basis $ 10
              3. Request a car on daily basis $ 192
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            car.displaystock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "Q" or choice == "q":  
        break
    
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    print("Thank you for using the vehicle rental shop")
                
