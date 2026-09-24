# Product CRUD Application
# Python and MySQL Connectivity

import mysql.connector


# Connect to MySQL
def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishnu@1723",
        database="company_db"
    )


# Add Product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    INSERT INTO products (product_name, price, quantity)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, price, quantity))
    connection.commit()

    print("Product added successfully.")

    cursor.close()
    connection.close()


# View Products
def view_products():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\n===== Products =====")

    for product in products:
        print(product)

    cursor.close()
    connection.close()


# Update Product
def update_product():
    product_id = int(input("Enter product ID: "))
    new_price = float(input("Enter new price: "))
    new_quantity = int(input("Enter new quantity: "))

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    UPDATE products
    SET price = %s, quantity = %s
    WHERE product_id = %s
    """

    cursor.execute(query, (new_price, new_quantity, product_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Product updated successfully.")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


# Delete Product
def delete_product():
    product_id = int(input("Enter product ID to delete: "))

    connection = connect_database()
    cursor = connection.cursor()

    query = "DELETE FROM products WHERE product_id = %s"

    cursor.execute(query, (product_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Product deleted successfully.")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


# Main Menu
def main():
    while True:
        print("\n===== Product Management System =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_product()

            elif choice == "2":
                view_products()

            elif choice == "3":
                update_product()

            elif choice == "4":
                delete_product()

            elif choice == "5":
                print("Thank you!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numbers.")

        except mysql.connector.Error as error:
            print("Database error:", error)


if __name__ == "__main__":
    main()
