import simpy

# Create a simulation environment
env = simpy.Environment()

# Define a process for a car
def car(env):
    while True:
        # The car starts parking and prints the current simulation time
        print('Start parking %d' % env.now)

        # Define the duration of parking
        parking_duration = 5

        # The car waits for the specified duration of parking time
        yield env.timeout(parking_duration)

        # The car is done parking and starts driving, printing the current simulation time
        print('Start driving at %d' % env.now)

        # Define the duration of the trip
        trip_duration = 2

        # The car waits for the specified duration of the trip time
        yield env.timeout(trip_duration)

# Add the car process to the simulation environment
env.process(car(env))

# Run the simulation until the specified time (15 in this case)
env.run(until=15)

