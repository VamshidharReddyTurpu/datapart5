import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user ="vturpu",
      password="vturpu589",
      host ="127.0.0.1",
      port="3307",
      database="projecthome")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   # Execute database operations...

   my_cursor = cm_connection.cursor()

   player_query = ("SELECT customer_id,customer_name FROM customer")

   my_cursor.execute(player_query)

   # Display results
   for row in my_cursor.fetchall():
      print("{}  {}".format(row[0], row[1]))
   my_cursor.close()
   # cm_connection.close()

   # displaying particular record
   customer_cursor = cm_connection.cursor()
   customer_query = ("SELECT product_order.customer_name,customer.customer_name")
   customer_query += (" FROM product_order JOIN customer on product_order.customer_name=customer.customer_name")
   customer_query += (" WHERE product_order.customer_name = %s")

   rep_last = input("Enter customer_name ")

   rep_data = (rep_last,)  # Comma required for single value tuple
   customer_cursor.execute(customer_query, rep_data)
   for row in customer_cursor.fetchall():
      print("{} {}  ".format(row[0], row[1]))
      customer_cursor.close()
      print("This is example is more complex. It uses functions, dictionaries and conditionals")
      # This is example is more complex. It uses functions, dictionaries and conditionals.

      import mysql.connector
      from mysql.connector import errorcode


      def get_status():
         statuses = {1: "Oven and drain cleaners", 2: "Laundry powder", 3: "savlon"}
         for key in statuses:
            print("{}. {}".format(key, statuses[key]))
         status = int(input("Enter product name or 0 for all orders: "))
         if 0 < status <= 3:
            return statuses[status]
         else:
            return "all"


      # main program

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="vturpu",
            password="vturpu589",
            host="127.0.0.1",
            port="3307",
            database="projecthome")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         product_order = get_status()

         orders_cursor = cm_connection.cursor()
         orders_query = ("SELECT * ")
         orders_query += ("FROM product_order")

         if product_order == "all":
            print("\n**All Orders**")
            print("{} {} {} {} ".format("order_id", "customer_name", "product_name","delivery_date"))
            print("-" * 77)
            orders_cursor.execute(orders_query)
            for (order_id, customer_name, product_name,delivery_date) in orders_cursor:
               print("{} {} {}".format(order_id, customer_name, product_name,delivery_date), end="")
            # if shippedDate is None:
            #    print(" Not Shipped", end="")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate), end="")
            print(" {}".format(product_name))
         else:
            orders_query += (" WHERE product_name = %s")
            status_data = (product_order,)
            orders_cursor.execute(orders_query, status_data)
            print("\n**Status: {}**".format(product_order))
            print("{} {} {}".format("order_id", "customer_name", "product_name","delivery_date"))
            for (order_id, customer_name, product_name,delivery_date) in orders_cursor:
               print("{} {} {} {}\n".format(order_id, customer_name, product_name, delivery_date), end="", )
            # if shippedDate is None:
            #    print(" Not Shipped")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate))

         orders_cursor.close()
         cm_connection.close()



      # Insert an customer
      print(".....Insert an customer.....")
      import mysql.connector
      from mysql.connector import errorcode
      import random

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="vturpu",
            password="vturpu589",
            host="127.0.0.1",
            port="3307",
            database="projecthome")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         office_query = "SELECT customer_id,customer_name,product_name,delivery_date FROM customer"
         office_cursor = cm_connection.cursor()
         office_cursor.execute(office_query)
         for row in office_cursor.fetchall():
            print("{}. {} {} {}".format(row[0], row[1],row[2],row[3]))
         office_cursor.close()

         ci = input("Enter customer id ")
         cn = input("Enter customer name: ")
         pn = input("Enter product_name ")
         dd = input("Enter delivery_date ")

         employee_query = ("INSERT INTO customer"
                           "(customer_id,customer_name,product_name,delivery_date)"
                           "VALUES (%s, %s, %s, %s)")

         employee_data = (ci, cn, pn, dd)
         try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            cm_connection.commit()
            print("Added customer")
            employee_cursor.close()
         except mysql.connector.Error as err:
            print("\n not added")
            print("Error: {}".format(err))
      cm_connection.close()
print("......Update an customer.......")
# Update an customer
import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user="vturpu",
      password="vturpu589",
      host="127.0.0.1",
      port="3307",
      database="projecthome")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   employee_last = input("Enter customer_id ")
   column = input("Enter item to update (customer_id, customer_name, product_name, delivery_date) ")
   prompt = "Enter new value for {} ".format(column)
   value = input(prompt)

   employee_query = ("UPDATE customer "
                     "SET " + column + " =  %s "
                                       "WHERE customer_id = %s")
   employee_data = (value, employee_last)
   try:
      employee_cursor = cm_connection.cursor()
      employee_cursor.execute(employee_query, employee_data)
      cm_connection.commit()
      print("Updated employee")
      employee_cursor.close()
   except mysql.connector.Error as err:
      print("\nEmployee not updated")
      print("Error: {}".format(err))
      cm_connection.close()
#
#    # Delete an customer
   print("Delete an customer")
   import mysql.connector
   from mysql.connector import errorcode

   # connect to DB
   try:
      cm_connection = mysql.connector.connect(
         user="vturpu",
         password="vturpu589",
         host="127.0.0.1",
         port="3307",
         database="projecthome")

   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Invalid credentials")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database not found")
      else:
         print("Cannot connect to database:", err)

   else:
      employee_last = input("Enter customer id to delete ")

      employee_query = ("DELETE FROM customer "
                        "WHERE customer_id = %s")
      employee_data = (employee_last,)
      try:
         employee_cursor = cm_connection.cursor()
         employee_cursor.execute(employee_query, employee_data)
         cm_connection.commit()
         print("Deleted customer")
         employee_cursor.close()
      except mysql.connector.Error as err:
         print("\ncustomer not updated")
         print("Error: {}".format(err))
      cm_connection.close()

   print ("Sucess!")
   cm_connection.close()