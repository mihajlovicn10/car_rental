import datetime
import tkinter as tk
from tkinter import ttk, messagebox

#Graphical User Interface

class CarRentalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Car Rental System")
        self.geometry("800x600")
        
        self.cars = []
        self.customers = []  
        
        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self)
        
        car_menu = tk.Menu(menubar, tearoff=0)
        car_menu.add_command(label="Add Car", command=self.add_car)
        car_menu.add_command(label="View Cars", command=self.view_cars)
        menubar.add_cascade(label="Cars", menu=car_menu)
        
        customer_menu = tk.Menu(menubar, tearoff=0)
        customer_menu.add_command(label="Add Customer", command=self.add_customer)
        customer_menu.add_command(label="View Customers", command=self.view_customers)
        menubar.add_cascade(label="Customers", menu=customer_menu)
        
        rental_menu = tk.Menu(menubar, tearoff=0)
        rental_menu.add_command(label="Rent Car", command=self.rent_car)
        rental_menu.add_command(label="Return Car", command=self.return_car)
        rental_menu.add_command(label="View Rentals", command=self.view_rentals)
        menubar.add_cascade(label="Rentals", menu=rental_menu)
        
        self.config(menu=menubar)
    
    def add_car(self):
        AddCarWindow(self)
    
    def view_cars(self):
        ViewCarsWindow(self)
    
    def add_customer(self):
        AddCustomerWindow(self)
    
    def view_customers(self):
        ViewCustomersWindow(self)
    
    def rent_car(self):
        AddRentalWindow(self)
    
    def return_car(self):
        ReturnCarWindow(self)
    
    def view_rentals(self):
        ViewRentalsWindow(self)

class AddCarWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add a Car")
        self.geometry("400x300")
        
        self.parent = parent
        
        tk.Label(self, text="Car ID").grid(row=0, column=0, padx=10, pady=10)
        self.car_id_entry = tk.Entry(self)
        self.car_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Make").grid(row=1, column=0, padx=10, pady=10)
        self.make_entry = tk.Entry(self)
        self.make_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Model").grid(row=2, column=0, padx=10, pady=10)
        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Year").grid(row=3, column=0, padx=10, pady=10)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Price per Day").grid(row=4, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Button(self, text="Add Car", command=self.add_car).grid(row=5, column=0, columnspan=2, pady=20)
    
    def add_car(self):
        car_id = self.car_id_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        price_per_day = self.price_entry.get()
        
        if car_id and make and model and year and price_per_day:
            try:
                year = int(year)
                price_per_day = float(price_per_day)
                
                car = Car(car_id, make, model, year, price_per_day)
                self.parent.cars.append(car)
                
                messagebox.showinfo("Success", "Car added successfully!")
                self.destroy()
            except ValueError:
                messagebox.showerror("Error", "Year must be an integer and Price per Day must be a float.")
        else:
            messagebox.showerror("Error", "All fields are required.")

class ViewCarsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View Cars")
        self.geometry("600x400")
        
        self.parent = parent
        
        columns = ("car_id", "make", "model", "year", "price_per_day")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("car_id", text="Car ID")
        self.tree.heading("make", text="Make")
        self.tree.heading("model", text="Model")
        self.tree.heading("year", text="Year")
        self.tree.heading("price_per_day", text="Price per Day")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_cars()
    
    def load_cars(self):
        for car in self.parent.cars:
            self.tree.insert("", tk.END, values=(car.car_id, car.make, car.model, car.year, car.price_per_day))

class AddCustomerWindow(tk.Toplevel): 
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Customer")
        self.geometry("400x300")
        
        self.parent = parent
        
        tk.Label(self, text="Customer ID").grid(row=0, column=0, padx=10, pady=10)
        self.customer_id_entry = tk.Entry(self)
        self.customer_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Email").grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Phone Number").grid(row=3, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Button(self, text="Add Customer", command=self.add_customer).grid(row=4, column=0, columnspan=2, pady=20)

        
    def add_customer(self): 
        customer_id = self.customer_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_entry.get()
        
        if customer_id and name and email and phone_number:
            customer = Customer(customer_id, name, email, phone_number)
            self.parent.customers.append(customer)
            
            messagebox.showinfo("Success", "Customer added successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

class ViewCustomersWindow(tk.Toplevel):
    def __init__(self, parent): 
        super().__init__(parent) 
        
        self.title("View all Customers")
        self.geometry("600x400")
        
        self.parent = parent 
        
        columns = ("customer_id", "name", "email", "phone_number")
        
        self.tree = ttk.Treeview(self, columns=columns,show="headings")
        self.tree.heading("customer_id", text="Customer ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone_number", text="Phone number")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_customers() 
        
    def load_customers(self): 
        for customer in self.parent.customers: 
             self.tree.insert("", tk.END, values=(customer.customer_id, customer.name, customer.email, customer.phone_number ))
        
    
class AddRentalWindow(tk.Toplevel):
    def __init__(self, parent): 
        super().__init__(parent)
        self.title("Rent Car")
        self.geometry("400x300")
        
        self.parent = parent 
        
        tk.Label(self, text="Select Car").grid(row=0, column=0, padx=10, pady=10)
        self.car_combobox = ttk.Combobox(self)
        self.car_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.car_combobox['values'] = [f"{car.car_id} - {car.make} {car.model}" for car in parent.cars if car.is_available]

        tk.Label(self, text="Select Customer").grid(row=1, column=0, padx=10, pady=10)
        self.customer_combobox = ttk.Combobox(self)
        self.customer_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.customer_combobox['values'] = [f"{customer.customer_id} - {customer.name}" for customer in parent.customers]
        
        tk.Label(self, text="Start Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=10)
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self, text="End Date (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=10)
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Button(self, text="Rent Car", command=self.rent_car).grid(row=4, column=0, columnspan=2, pady=20)
    
    def rent_car(self):
        selected_car = self.car_combobox.get()
        selected_customer = self.customer_combobox.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        
        if selected_car and selected_customer and start_date and end_date:
            car_id = int(selected_car.split(" - ")[0])
            customer_id = int(selected_customer.split(" - ")[0])
            
            try:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
                
                car = next((car for car in self.parent.cars if car.car_id == car_id), None)
                customer = next((customer for customer in self.parent.customers if customer.customer_id == customer_id), None)
                
                if car and customer and car.is_available:
                    rental = Rental(len(self.parent.rentals) + 1, car, customer, start_date, end_date)
                    self.parent.rentals.append(rental)
                    car.rent_car()
                    customer.rent_car(car)
                    
                    messagebox.showinfo("Success", "Car rented successfully!")
                    self.destroy()
                else:
                    messagebox.showerror("Error", "Car or Customer not found, or Car is not available.")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        else:
            messagebox.showerror("Error", "All fields are required.")
            
class ViewRentalsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View Rentals")
        self.geometry("600x400")
        
        self.parent = parent
        
        columns = ("rental_id", "car_info", "customer_info", "rental_date", "return_date", "total_cost")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("rental_id", text="Rental ID")
        self.tree.heading("car_info", text="Car")
        self.tree.heading("customer_info", text="Customer")
        self.tree.heading("rental_date", text="Rental Date")
        self.tree.heading("return_date", text="Return Date")
        self.tree.heading("total_cost", text="Total Cost")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_rentals()
    
    def load_rentals(self):
        for rental in self.parent.rentals:
            car_info = f"{rental.car.make} {rental.car.model}"
            customer_info = rental.customer.name
            rental_date = rental.rental_date.strftime("%Y-%m-%d")
            return_date = rental.return_date.strftime("%Y-%m-%d") if rental.return_date else "N/A"
            total_cost = f"${rental.total_cost:.2f}"
            self.tree.insert("", tk.END, values=(rental.rental_id, car_info, customer_info, rental_date, return_date, total_cost))
            
class ReturnCarWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Return Car")
        self.geometry("400x300")
        
        self.parent = parent
        
        tk.Label(self, text="Select Car").grid(row=0, column=0, padx=10, pady=10)
        self.car_combobox = ttk.Combobox(self)
        self.car_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.car_combobox['values'] = [f"{rental.car.car_id} - {rental.car.make} {rental.car.model}" for rental in parent.rentals if rental.return_date is None]

        tk.Label(self, text="Select Customer").grid(row=1, column=0, padx=10, pady=10)
        self.customer_combobox = ttk.Combobox(self)
        self.customer_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.customer_combobox['values'] = [f"{rental.customer.customer_id} - {rental.customer.name}" for rental in parent.rentals if rental.return_date is None]
        
        tk.Button(self, text="Return Car", command=self.return_car).grid(row=2, column=0, columnspan=2, pady=20)
    
    def return_car(self):
        selected_car = self.car_combobox.get().split(" - ")[0]
        selected_customer = self.customer_combobox.get().split(" - ")[0]
        
        if selected_car and selected_customer:
            car_id = int(selected_car)
            customer_id = int(selected_customer)
            
            self.parent.return_car(car_id, customer_id)
            
            messagebox.showinfo("Success", "Car returned successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Please select a car and a customer.")
     
#Application Engine 


class Car:
    def __init__(self, car_id, make, model, year, price_per_day):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.is_available = True
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model} (ID: {self.car_id}) - ${self.price_per_day}/day")
    
    def rent_car(self):
        if self.is_available:
            self.is_available = False
            print(f"Car {self.car_id} has been rented.")
        else:
            print(f"Car {self.car_id} is not available.")
    
    def return_car(self):
        self.is_available = True
        print(f"Car {self.car_id} has been returned.")

class Customer:
    def __init__(self, customer_id, name, email, phone_number, rental_history=None):
        if rental_history is None:
            rental_history = []
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.rental_history = rental_history
    
    def rent_car(self, car):
        if car.is_available:
            car.rent_car()
            self.rental_history.append(car)
        else:
            print(f"Car {car.car_id} is not available for rent.")
    
    def return_car(self, car):
        if car in self.rental_history:
            car.return_car()
            self.rental_history.remove(car)
        else:
            print(f"Car {car.car_id} was not rented by {self.name}.")

class Rental:
    def __init__(self, rental_id, car, customer, rental_date, return_date):
        self.rental_id = rental_id
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date
        self.total_cost = self.calculate_cost()
    
    def calculate_cost(self):
        if self.return_date is None: 
            return 0
        rental_days = (self.return_date - self.rental_date).days
        return rental_days * self.car.price_per_day
    
    def display_rental_info(self):
        print(f"Rental ID: {self.rental_id}, Car: {self.car.make} {self.car.model}, Customer: {self.customer.name}, Total Cost: ${self.total_cost}")

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def remove_car(self, car_id):
        self.cars = [car for car in self.cars if car.car_id != car_id]
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def rent_car(self, car_id, customer_id):
        car = next((car for car in self.cars if car.car_id == car_id), None)
        customer = next((customer for customer in self.customers if customer.customer_id == customer_id), None)
        if car and customer and car.is_available:
            car.rent_car()
            customer.rent_car(car)
            rental = Rental(len(self.rentals) + 1, car, customer, datetime.datetime.now(), None)
            self.rentals.append(rental)
        else:
            print("Car or Customer not found, or Car is not available.")
    
    def return_car(self, car_id, customer_id):
        car = next((car for car in self.cars if car.car_id == car_id), None)
        customer = next((customer for customer in self.customers if customer.customer_id == customer_id), None)
        if car and customer and car in customer.rental_history:
            car.return_car()
            customer.return_car(car)
            rental = next((rental for rental in self.rentals if rental.car.car_id == car_id and rental.customer.customer_id == customer_id and rental.return_date is None), None)
            if rental:
                rental.return_date = datetime.datetime.now()
                rental.total_cost = rental.calculate_cost()
    
    def display_all_cars(self):
        for car in self.cars:
            car.display_info()
    
    def display_available_cars(self):
        for car in self.cars:
            if car.is_available:
                car.display_info()
                
                
if __name__ == "__main__":
    app = CarRentalApp()
    app.mainloop()              