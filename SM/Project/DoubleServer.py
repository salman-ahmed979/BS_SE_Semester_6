import numpy as np


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
        self.time_depart = float('inf')

        self.num_of_arrival=0
        self.num_of_depart=0
        self.event_number=0
        self.server_status_baker=0
        self.server_status_able=0
        self.depart_able= float('inf')
        self.depart_baker =  float('inf')
   
    def advance_time(self):
        self.event_number += 1
        t_event = min(self.time_arrival, self.time_depart)
        self.clock = t_event

        if self.time_arrival < self.time_depart:
            self.handle_arrival_event()
        elif self.time_arrival > self.time_depart:
            self.handle_departure_event()
        else:
            self.handle_arrival_event()
            self.handle_departure_event()
    
    def handle_arrival_event(self):
        self.number_in_sys += 1
        self.num_of_arrival += 1
        self.server_status = 1

        if self.number_in_sys <= 1:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
        
        self.interarrival_times.append(generate_interarrival_time())
        self.time_arrival = self.clock + self.interarrival_times[-1]
    
    def handle_departure_event(self):
        self.number_in_sys -= 1
        self.num_of_depart += 1

        if self.number_in_sys > 0:
            self.service_times.append(generate_service_time())
            self.time_depart = self.clock + self.service_times[-1]
        else:
            
            self.server_status = 0
            self.time_depart = float('inf')

    def get_state(self):
        return [self.event_number, self.clock, self.time_arrival, self.time_depart, self.num_of_arrival, self.num_of_depart, self.server_status]

s = Simulation()
data = []
while s.num_of_depart < 10:
    s.advance_time()
    data.append(s.get_state())

for i in range(data.__len__()):
    print(data[i], "\n")