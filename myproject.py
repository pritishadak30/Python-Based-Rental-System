#Create a list of cars as dictionaries
cars = [
    {'cae_id':"C001", 'make':"Toyota", 'model':"Innova", 'year':2022, 'available': True},
    {'car_id':"C002", 'make':"Honda", 'model':"Innova", 'year':2022, 'available': True},
    {'cae_id':"C003", 'make':"Maruti", 'model':"Swift", 'year':2022, 'available': True}
]
#Create a list of customers as dictionaries
customers = [
    {'customer_id':"Cu001", 'name':"Adarsh Wahewall", 'rented_cars':[]},
    {'customer_id':"Cu002", 'name':"pritish", 'rented_cars':[]},
    {'customer_id':"Cu003", 'name':"prachee", 'rented_cars':[]}
]
#Create a list to store rentals as dictionaries
rentals = []
#Function to rent a car
def rent_car(customer, car):
    if car['available']:
        car['available'] = False
        customer['rented_cars'].append(car)
        return True
    return False
#Function to return a car
def return_car(customer, car):
    if car in customer['rented_cars']:
        car['available'] = True
        customer['rented_cars'].remove(car)
        return True
    return False
#Rent cars
rent_car(customers[0], cars[0])
rent_car(customers[1], cars[1])
rent_car(customers[2], cars[2])
#Diaplay rented cars for customers
print(f"{customers[0]['name']}'s Rented Cars:{[car['make']for car in customers[0]['rented_cars']]}")
print(f"{customers[1]['name']}'s Rented Cars:{[car['make']for car in customers[1]['rented_cars']]}")
print(f"{customers[2]['name']}'s Rented Cars:{[car['make']for car in customers[2]['rented_cars']]}")
#Return cars
return_car(customers[0], cars[0])
return_car(customers[2], cars[2])
#Diaplay Updated rented cars for customers
print(f"{customers[0]['name']}'s Updated Rented Cars:{[car['make']for car in customers[0]['rented_cars']]}")
print(f"{customers[1]['name']}'s updated Rented Cars:{[car['make']for car in customers[1]['rented_cars']]}")
print(f"{customers[2]['name']}'s updated Rented Cars:{[car['make']for car in customers[2]['rented_cars']]}")
# Create rentals and data to the list
rentals.append({'rental_id':"R001",'customer': customers[0],'car': cars[0],'rental_fee': 500.0})
rentals.append({'rental_id':"R002",'customer': customers[1],'car': cars[1],'rental_fee': 450.0})
rentals.append({'rental_id':"R003",'customer': customers[2],'car': cars[2],'rental_fee': 350.0})
#Display rental information
for rental in rentals:
    print(f"Rental ID: {rental['rental_id']}, Customer: {rental['customer']['name']}, car:{rental['car']['make']}, Rental Fee: INR{rental['rental_fee']}")
    