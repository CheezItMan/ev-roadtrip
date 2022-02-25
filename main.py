import math

CHARGING_COST = 5.0
MEAL_COST = 20.0
TOTAL_DISTANCE = 1000
SPEED = 90
CHARGING_TIME = 60
MINUTES_PER_HOUR = 60
HOURS_PER_MEAL = 3

def ev_roadtrip_costs(vehicles):
    min_car = vehicles[0]
    for car in vehicles:
        car['total'] = car["rental_price"]
        number_stops = math.ceil(TOTAL_DISTANCE / car["range"])
        charging_total = number_stops * CHARGING_COST
        driving_time = TOTAL_DISTANCE / SPEED * MINUTES_PER_HOUR
        total_charging_time = CHARGING_TIME * MINUTES_PER_HOUR
        time_spent = driving_time + total_charging_time
        meal_cost = time_spent / (HOURS_PER_MEAL * MINUTES_PER_HOUR) * MEAL_COST
        
        car['total'] += charging_total + meal_cost

        if car['total'] < min_car['total']:
            min_car = car

    least_expensive_cars = []
    for car in vehicles:
        if car['total'] == min_car['total']:
            least_expensive_cars.append(car)

    if len(least_expensive_cars) == 0:
        return least_expensive_cars[0]['name']

    return [car['name'] for car in least_expensive_cars]


# Sample input
vehicles = [
    {
        "name": "Model 3",
        "range": 330,
        "rental_price": 800,
    },
    {
        "name": "Mach-E",
        "range": 250,
        "rental_price": 785,
    },
    {
        "name": "ë-C4",
        "range": 200,
        "rental_price": 780,
    },
    {
        "name": "Ioniq 5",
        "range": 280,
        "rental_price": 820,
    },
]

answer = ev_roadtrip_costs(vehicles)

print()
print()
print(answer)

