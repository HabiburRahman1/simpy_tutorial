import simpy

env = simpy.Environment()

def car(env, name, bcs, driving_time, charge_duration):
    # Simulate driving to the BCS
    yield env.timeout(driving_time)

    # Request one of its charging spots
    print('%s arriving at %d' % (name, env.now))
    with bcs.request() as req:
        yield req

        # Charge the battery
        print('%s starting to charge at %s' % (name, env.now))
        yield env.timeout(charge_duration)
        print('%s leaving the bcs at %s' % (name, env.now))

# Create the BCS with 2 spots
bcs = simpy.Resource(env, capacity=2)

# Create 4 cars
for i in range(4):
    env.process(car(env, 'Car %d' % i, bcs, i*2, 5))

# Execute!
env.run()