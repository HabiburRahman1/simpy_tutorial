import simpy

env = simpy.Environment()

class Car(object):
    def __init__(self, env):
        self.env = env
        # Start the process every time an instance is created
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            print('Start parking and charging at %d' % env.now)
            charge_duration = 5
            # We yield the process that process() returns
            # to wait for it to finish
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                # When we received an interrupt, we stop charging and
                # switch to the "driving" state
                print('Was interrupted. Hope, the battery is full enough ...')

            # The charge process has finished and
            # we can start driving again
            print('Start driving at %d' % env.now)
            trip_duration = 2

            try:
                yield self.env.timeout(trip_duration)
            except simpy.Interrupt:
                # When we received an interrupt, we stop driving and
                # switch to the "charging" state
                print('Was interrupted. Please, wait while charing ...')

    def charge(self, duration):
        yield self.env.timeout(duration)

def driver(env, car):
    # Wait for 1 time unit before interrupting the car's action
    yield env.timeout(6)
    car.action.interrupt()

# Create an instance of the Car class
car = Car(env)

# Start the driver process
env.process(driver(env, car))


# Run the simulation until time 15
env.run(until=15)