"""
Simulating a Super Market Aisle 

Let us say we want to decide how many ailes should be
functional in a new super market. Since it is a 
new shop, we dont have historic information. We simulate
and check out.


Mar-09-2016
Gopi Subramanian
"""


import simpy
import random
import time


time_spent_at_counter = []

class Counter(object):
    def __init__(self,env,no_counters,scan_time):
		self.env = env
		self.counters =  simpy.Resource(env, no_counters)
		self.item_scan_time = scan_time
    
    def checkout(self, customer, no_items):
    	yield self.env.timeout(no_items * self.item_scan_time)

def customer(env, name, counter, no_items):
    #total_customers+=1
    with counter.counters.request() as request:
        yield request
        enter = env.now
        yield env.process(counter.checkout(name, no_items))
        leaves = env.now
        #print '%s Enters at %.2f leaves counter at %.2f'%(name,enter,leaves)
        elapsed = leaves - enter
        time_spent_at_counter.append(elapsed)


def setup(env,no_counters, scan_time):
    counters = Counter(env, no_counters, scan_time)
    # Initial customers
    for i in range(10):
        no_items = random.randint(5,35)
        env.process(customer(env, 'Customer %d' % i, counters, no_items))
    hour = 0
    while True:
    	# Every hour
        yield env.timeout(random.randint(48,62))
        hour = hour + 1
        no_customers = random.randint(30,200)
        i += 1
        start = i
        for i in range(start,start+no_customers):
        	no_items = random.randint(5,35)
        	env.process(customer(env, 'Customer %d' % i, counters,no_items))
        print  'Hour %d, Number of Customers %d, %.3f Average minutes spent by a customer at counter ' \
        %(hour,no_customers,sum(time_spent_at_counter) / (1.0*len(time_spent_at_counter)))


No_counters            = 2
# Time it takes to scan an item
item_scan_time         = 0.3

env = simpy.Environment()
env.process(setup(env, No_counters, item_scan_time))

# Simulation in minutes
# 8 hours
env.run(until=480)
print  '%.3f Average minutes spent by a customer at counter ' \
%(sum(time_spent_at_counter) / (1.0*len(time_spent_at_counter)))

