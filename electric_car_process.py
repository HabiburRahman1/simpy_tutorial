import simpy
env = simpy.Environment()

class Car(object):
    def __init__(self, env):
        self.env = env
        # Start the process everytime an instance is created
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            print('Start parking and charing at %d' % env.now)
            charge_duration = 5
            # We yield the process that process() returns
            # to wait for it to finish
            yield self.env.process(self.charge(charge_duration))

            # The charge process has finished and
            # we can start driving again
            print('Start driving at %d' % env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

car = Car(env)
env.run(until=15)
