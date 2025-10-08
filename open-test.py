import csv
import os
import locale
import time
from time import sleep
from colors import bcolors  

products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)

def list_products(products):
    for idx, product in enumerate(products, start=1):
        print(f"{idx} {product['name']} {product['price']}")




def load_data(filename): 
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
   
def view_product(products, idx):
    for i, product in enumerate(products):
        if i == idx:
            return product
    return None

def Save_data(products, filepath):
    
    sleep(0.1)

    try:
        with open(filepath, 'w', newline='') as file:
            fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)

    except Exception as error_code:
        print("Fel", error_code)
    return f"OK"

def menu():
    print("1. Visa produkt och dess beskrivningar")
    print("2. Ta bort produkt")
    print("3. Lägg till produkt")
    print("4. Avsluta")
    choice = int(input("Välj ett alternativ: "))

    if choice == 1:
        os.system('cls')
        idx = int(input("Välj produkt (nummer): ")) - 1
        product = view_product(products, idx)  
        if product:
            print(f"Produkt: {product['name']} | {product['desc']} | {format_currency(product['price'])} | {product['quantity']} st i lager")
        else:
            print("Produkten hittades inte.")
    elif choice == 2:
        try:
            os.system('cls')
            idx = int(input(f"""{bcolors.RED} Välj produkt (nummer) som du vill ta bort: {bcolors.DEFAULT}""")) - 1
            if idx < 0 or idx >= len(products):
                print("Ogiltigt produktnummer.")
                return
            product = view_product(products, idx)  
            if product:
                products.remove(product)
                print("produkten är borttagen")
                Save_data(products, 'db_products.csv')
            else:
                print("Produkten hittades inte.")
        except(ValueError, IndexError):
            print("Ogiltigt produktnummer.")
    elif choice == 3:
        os.system('cls')
        print(f"""{bcolors.YELLOW}Vilken produkt vill du lägga till?{bcolors.DEFAULT}""")
        name = input("Namn: ")
        desc = input("Beskrivning: ")   
        price = float(input("Pris: "))
        quantity = int(input("Antal i lager: "))
        products.append({
            "id": len(products) + 1,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        })
        Save_data(products, 'db_products.csv')
        print("Sparar produkt...")
        
    elif choice == 4:
        os.system('cls')
        Save_data(products, 'db_products.csv')
        print("Sparar listan innan avslut...")
        sleep(2)
        print("Avslutar programmet...")
        exit()

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

load_data('db_products.csv')

 
os.system('cls')


#for  idx, product in enumerate(products):
 #   print(f"{product['id']}: {product['name']} - {format_currency(product['price'])} ({product['quantity']} st i lager)")

#for i, product in enumerate(products, start=1):
 #   print(f"{i:<4} {product['id']:<5}{product['name']:<20} {format_currency(product['price']):<10} ({product['quantity']} st i lager)")


while True:
    
   
    
    list_products(products)
    menu()
    
    
            
    #list_products(products)
    #idx = int(input("Välj produkt (nummer): "))
    
              
    #product = view_product(products, idx)
    #print(f"product: {product['name']} | {product['desc']} | {format_currency(product['price'])} | {product['quantity']} st i lager")
    #input()
    #break





