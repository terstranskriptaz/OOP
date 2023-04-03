#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 03:31:30 2023

@author: ozgekilic
"""
'''

parent class

                        VehicleRent (parent class)
                            methodlar
                                displaystock
                                rent
                                    hourly
                                    daily
                                returnvehicle
            
            #child classes
            
            CarRent                                  BikeRent 
                discount method 
                
                
                                Customer #class
                                    requestVehicle
                                    returnvehicle
                                    
rent.py ve main.py yazilacak

'''

import datetime 

class RentVehicle:
    def __init__(self, stock):
        #stock=araba sayisi
        self.stock=stock 
        self.now = 0 #now parametresini bill/fatura hesaplarken kullanicaz
        
    def displaystock(self):
        '''
        display stock stoktaki arac sayisini return edecek metod

        '''
        print("{} Vehicle avaliavle to rent ".format(self.stock))
        return self.stock
    
    def rentHourly(self, n): #n arac sayisi
        '''
        rent hourly

        '''
        if n<= -0:
            print("Nuumber should be bigger than zero. ")
            return None
        elif n> self.stock:
            print("Sorry, we do not have enough stock. ")
            return None
        else:
            self.now = datetime.datetime.now()
            #datetime bir kütüphane ve bilgisayarin o anki zamanini alir
            #kütüphane olarak eklendi üste 
            print("Rented {} vehicle for hourly at {} hours".format(n, self.now.hour))
            #birinci parantez n ile, ikinci datetime ile doldurulacak
            self.stock -= n #stock sayisindan n sayisini cikarir
            return self.now #müsterinin araci geri getirdigi saat 
        
    def rentDaily(self, n):
        '''
        rent daily

        '''
        if n<= -0:
            print("Nuumber should be bigger than zero. ")
            return None
        elif n> self.stock:
            print("Sorry, we do not have enough stock. ")
            return None
        else:
            self.now = datetime.datetime.now()
            #datetime bir kütüphane ve bilgisayarin o anki zamanini alir
            #kütüphane olarak eklendi üste 
            print("Rented {} vehicle for daily at {} hours".format(n, self.now.hour)) #gün veya dakika da olabilirdi
            #birinci parantez n ile, ikinci datetime ile doldurulacak
            self.stock -= n #stock sayisindan n sayisini cikarir
            return self.now #müsterinin araci geri getirdigi saat 
        
    def returnvehicle(self, request, brand): #parent class
        '''
        return a bill
        fatura cikarma adimi 
    
        '''
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        rentalTime, rentalBasis, numofVehicle =request
        
        bill = 0
        
        if brand == "car": 
            if rentalTime and rentalBasis and numofVehicle :
                self.stock += numofVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis==1: #hourly
                    bill = rentalPeriod.second/3600 * car_h_price * numofVehicle #saniye bazli hesapladik
                    #second*3600 == 1 saat 
                elif rentalBasis == 2: #daily
                    bill =rentalPeriod.second/(3600*24) * car_d_price * numofVehicle
                if (2<= numofVehicle):
                    print("You have extra %20 discount...")
                    bill=bill*0.8
                print("Thank you for returning the car.")
                print("Price: $ {}".format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numofVehicle:
                self.stock += numofVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis==1: #hourly
                    bill = rentalPeriod.second/3600 * bike_h_price * numofVehicle #saniye bazli hesapladik
                    #second*3600 == 1 saat 
                elif rentalBasis == 2: #daily
                    bill =rentalPeriod.second/(3600*24)*bike_d_price*numofVehicle
                if (2<= numofVehicle):
                    print("You have extra %20 discount...")
                    bill=bill*0.8
                print("Thank you for returning the bike.")
                print("Price: $ {}".format(bill))            
                return bill
        else:
            print("You do not have vehicle to return ")
            return None
            
class CarRent(RentVehicle): #child class
    global discount_rate #bütün clss kullansin diye global kullanildi
    '''
    Python'da global değişkenler, tanımlandıkları fonksiyon dışındaki herhangi bir yerden erişilebilirler. 
    Global değişkenler, herhangi bir fonksiyon içinde değiştirilebilirler ancak bu değişikliklerin 
    fonksiyon dışındaki yere etkisi olacaktır. 
    '''
    discount_rate = 15
    def __init__(self, stock):
        super().__init__(stock)  #parent class daki init i cagirmak ve kullanmak icin 
        '''
        super() is used to reference the parent class. 
        The __init__() method is a special method in Python classes that is called when an object is created. 
        It initializes the object's attributes.

        By calling super().__init__(stock), the child class is calling the constructor of the parent class 
        and passing the argument stock to it. This allows the parent class to initialize its own attributes 
        before the child class's attributes are initialized. 
        '''
    def discount(self, b): #b = bill 
        bill = b - (b*discount_rate)/100
        return bill
class BikeRent(RentVehicle):

    def __init__(self, stock):
        super().__init__(stock)
           
        
#customer 
class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    def requestvehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent? ")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Please write a number.")
                return -1
            if bikes <1:
                print("Number of bikes hould be greater than zero.")
                return -1
            else:
                self.bikes = bikes
        elif brand == "car":
            cars = input("How many cars would you like to rent?")
            try:
                cars = int(cars)
            except ValueError:
                print("Please write a number.")
                return -1
            if cars <1:
                print(" The number of cars should be greater than zero.")
                return -1
            else:
                self.cars = cars
            return self.cars
        else:
            print("Request Vehicle Error...Sorry, it is you. ")

    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b,  self.bikes
            else:
                return 0,0,0
        elif brand == "car": 
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c,  self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle Error")
