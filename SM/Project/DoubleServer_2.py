import numpy as np
import matplotlib.pyplot as plt

MEAN_INTERARRIVAL_TIME = 1
MEAN_SERVICE_TIME = 0.1

def generate_service_time():
    return np.random.exponential(MEAN_SERVICE_TIME)

def generate_interarrival_time():
    return np.random.exponential(MEAN_INTERARRIVAL_TIME)

class Simulation:
    def __init__(self):
        self.number_in_sys = 0
        self.interarrival_times = []
        self.service_times = []

        # Initial InterArrival time of Customer-One
        self.interarrival_times.append(generate_interarrival_time())
        
        # Setting clock
        self.clock = 0.0

        # Setting arrival and departure time
        self.time_arrival = self.interarrival_times[-1]
        self.first_time_arrival = self.time_arrival

        self.time_depart = float('inf')

        self.num_of_arrival = 0
        self.num_of_depart = 0
        self.event_number = 0

        self.server_1_status = 0
        self.server_2_status = 0

        # Depart of individual servers
        self.depart_server_1 = float('inf')
        self.depart_server_2 =  float('inf')

        # No. Users in Server
        self.number_in_server_1 = 0
        self.number_in_server_2 = 0

    def advance_time(self):
        self.event_number += 1
        t_event = min(self.time_arrival, self.time_depart)
        self.clock = t_event
        

        if (self.depart_server_1 == float("inf") and self.depart_server_2 == float("inf")) or self.depart_server_1 == self.depart_server_2:
            if self.time_arrival < self.depart_server_1:
                self.handle_arrival_event_1()
            
            elif self.time_arrival > self.depart_server_1: 
                self.handle_departure_event_1()
            else:
                self.handle_arrival_event_1()
                self.handle_departure_event_1()
        
        elif self.depart_server_2 == float("inf") and self.time_arrival < self.depart_server_1:
            self.handle_arrival_event_2()

        elif self.depart_server_1 < self.depart_server_2 and self.depart_server_2 != float("inf"):
            if self.time_arrival < self.depart_server_1:
                self.handle_arrival_event_1()
            
            elif self.time_arrival > self.depart_server_1:
                self.handle_departure_event_1()
            else:
                self.handle_arrival_event_1()
                self.handle_departure_event_1()
        
        else:
            if self.time_arrival < self.depart_server_2:
                self.handle_arrival_event_2()
            
            elif self.time_arrival > self.depart_server_2:
                self.handle_departure_event_2()
            else:
                self.handle_arrival_event_2()
                self.handle_departure_event_2()

        if self.depart_server_1 == float("inf") and self.depart_server_2 == float("inf"):
            self.time_depart = float("inf")

    def handle_arrival_event_1(self):
        self.number_in_sys += 1
        self.num_of_arrival += 1
        self.number_in_server_1 += 1
        self.server_1_status = 1

        self.first_time_arrival = self.time_arrival
        
        if self.number_in_server_1 <= 1:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
            self.depart_server_1 = self.time_depart

        self.interarrival_times.append(generate_interarrival_time())
        self.time_arrival = self.clock + self.interarrival_times[-1]
    
    def handle_departure_event_1(self):
        self.number_in_sys -= 1
        self.number_in_server_1 -= 1
        self.num_of_depart += 1

        if self.number_in_server_1 > 0:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
            self.depart_server_1 = self.time_depart
        else:
            self.server_1_status = 0
            self.depart_server_1 = float("inf")
    
    def handle_arrival_event_2(self):
        self.number_in_sys += 1
        self.num_of_arrival += 1
        self.number_in_server_2 += 1
        self.server_2_status = 1
        self.first_time_arrival = self.time_arrival

        if self.number_in_server_2 <= 1:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
            self.depart_server_2 = self.time_depart

        self.interarrival_times.append(generate_interarrival_time())
        self.time_arrival = self.clock + self.interarrival_times[-1]
    
    def handle_departure_event_2(self):
        self.number_in_sys -= 1
        self.number_in_server_2 -= 1
        self.num_of_depart += 1

        if self.number_in_server_2 > 0:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
            self.depart_server_2 = self.time_depart
        else:
            self.server_2_status = 0
            self.depart_server_2 = float("inf")

    def get_state(self):
        return [self.event_number, self.clock, self.first_time_arrival, self.time_arrival, self.time_depart, self.num_of_arrival, self.num_of_depart, self.server_1_status, self.server_2_status]

    def showGraph(self):
        plt.hist(self.interarrival_times, bins = 20)
        plt.hist(self.service_times,bins=20)
        plt.show()


s = Simulation()
data = []

while s.num_of_depart < 2000:
    s.advance_time()
    data.append(s.get_state())

for i in range(data.__len__()):
    print(data[i], "\n")

stats={"mean_inter_arrival_time": np.mean(s.interarrival_times),
"mean_service_time": np.mean(s.service_times),
"server_busy_time": np.sum(s.service_times)-s.service_times.pop(-1),
"total_simulation_time": s.clock,
"total_customers_served": s.num_of_depart}

print('Simulation Report:')
print("{:<25} {:<15}".format("",""))
for k, v in stats.items():
    Value = v
    print("{:<25} {:<15}".format(k, Value))

s.showGraph()