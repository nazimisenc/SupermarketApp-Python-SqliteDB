import sqlite3
import time

class Products():
    def __init__(self,brand,name,price,weight,expiration_date):
        self.brand = brand
        self.name = name
        self.price = price
        self.weight = weight
        self.expiration_date = expiration_date

    def __str__(self):
        return "Brand: {}\nName: {}\nPrice: {} TL\nWeight(g): {}g\nExpiration Date: {}\n".format(self.brand,self.name,self.price,self.weight,self.expiration_date)

class Product_List():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("SupermarketLib.db") #We created database here.
        self.cursor = self.connection.cursor()
        text = "Create Table if not exists Products (brand TEXT,name TEXT,price FLOAT,weight INT,expiration_date TEXT)"
        self.cursor.execute(text)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def show_all_products(self):
        text = "Select * From Products"
        self.cursor.execute(text)
        products = self.cursor.fetchall()
        if len(products) == 0:
            print("There are no products here...!\n")
        else:
            for i in products:
                show_products = Products(i[0],i[1],i[2],i[3],i[4])
                print(show_products)

    def add_product(self,product):
        text = "Insert into Products Values (?,?,?,?,?)"
        self.cursor.execute(text,(product.brand,product.name,product.price,product.weight,product.expiration_date))
        self.connection.commit()

    def del_product(self,product):
        text = "Select * From Products where name = ?"
        self.cursor.execute(text,(product,))
        productinf = self.cursor.fetchall()
        if len(productinf) == 0:
            print("This product already isnt here...!\n")
        else:
            text1 = "Delete from Products where name = ?"
            self.cursor.execute(text1,(product,))
            self.connection.commit()
            print("\nProduct deleted...!\n")

    def show_product_info(self,product):
        text = "Select * From Products where name = ?"
        self.cursor.execute(text,(product,))
        productinf = self.cursor.fetchall()
        if len(productinf) == 0:
            print("This product dosent find...!\n")
        else:
            products = Products(productinf[0][0],productinf[0][1],productinf[0][2],productinf[0][3],productinf[0][4])
            print(products)

    def update_product_price(self,name,new_price):
        text1 = "Select * From Products where name = ?"
        self.cursor.execute(text1,(name,))
        productinf = self.cursor.fetchall()
        if len(productinf) == 0:
            print("\nThis product doesnt find...!\n")
        else:
            text = "Update Products set price = ? where name = ?"
            self.cursor.execute(text,(new_price,name))
            self.connection.commit()
            print("\nUpdate Succssesfully Done...!\n")

    def total_product_number(self):
        text = "Select * From Products"
        self.cursor.execute(text)
        total_product = self.cursor.fetchall()
        x = len(total_product)
        print("Total Product in Supermarket Menu: ",x)
        print("")

product_list = Product_List()

print("""

***WELCOME TO THE SUPERMARKET MENU***

1.Show all products
2.Add Product
3.Del Product
4.Show one of the Products Info
5.Update one of the Products Price
6.Show Total Products Number
0.Quit Menu

""")

while True:
    choose = input("Number: ")

    if choose == "0":
        print("\nExiting the Supermarket Menu...!\n")
        time.sleep(1)
        print("Exit successfuly done...!")
        break

    elif choose == "1":
        print("")
        time.sleep(0.5)
        product_list.show_all_products()

    elif choose == "2":
        print("\nPlease add product here...!\n")

        try:
            brand = input("Brand: ")
            name = input("Name: ")
            price = float(input("Price: "))
            weight = input("Weight: ")
            ed = input("Expiration Date: ")
            new_product = Products(brand,name,price,weight,ed)
            print("\nProduct adding...!")
            time.sleep(0.5)
            product_list.add_product(new_product)
            print("Product added...!\n")
        except ValueError:
            print("\nPrice must be float not string...!\n")

    elif choose == "3":
        print("")
        print("Which product you want to delete...?\n")
        product = input("Product Name: ")
        product = product.upper()
        product_list.del_product(product)

    elif choose == "4":
        print("\nWhich product info you want to see...?\n")
        answer = input("Product Name: ")
        answer = answer.upper()
        print("")
        product_list.show_product_info(answer)

    elif choose == "5":
        print("")
        print("Which product price you want to update...?\n")
        try:
            answer1 = input("Product Name: ")
            answer1 = answer1.upper()
            answer2 = float(input("New Price: "))
            product_list.update_product_price(answer1,answer2)
        except ValueError:
            print("\nNew Price must be integer not string...!\n")

    elif choose == "6":
        print("")
        product_list.total_product_number()

    else:
        print("\nTry Again...!\n")
