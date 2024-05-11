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

        self.num_of_arrival = 0
        self.num_of_depart = 0
        self.event_number = 0

        # Servers Status
        self.server_status_baker = 0
        self.server_status_able = 0
        
        # Individual Able and Baker Departure
        self.depart_able = float('inf')
        self.depart_baker =  float('inf')

        # No. Users in Server
        self.number_in_able = 0
        self.number_in_baker = 0

    def advance_time(self):
        self.event_number += 1
        t_event = min(self.time_arrival, self.time_depart)
        self.clock = t_event

        if (self.time_arrival < self.depart_able and self.server_status_able == 0) or (self.time_arrival < self.depart_baker and self.server_status_baker == 0):
            # Priority to the Able
            if (self.time_arrival < self.depart_able and self.server_status_able == 0):
                self.server_status_able = 1
                self.number_in_sys += 1
                self.num_of_arrival += 1
                self.number_in_able += 1

                if self.number_in_able <= 1:
                    self.service_times.append(generate_service_time())
                    self.time_depart = self.clock + self.service_times[-1]
                    self.depart_able = self.time_depart

                # Calculate for other users    
                self.interarrival_times.append(generate_interarrival_time())
                self.time_arrival = self.clock + self.interarrival_times
            
            elif (self.time_arrival < self.depart_baker and self.server_status_baker == 0):
                self.server_status_able = 1
                self.number_in_sys += 1
                self.num_of_arrival += 1
                self.number_in_baker += 1

                if self.number_in_baker <= 1:
                    self.service_times.append(generate_service_time())
                    self.time_depart = self.clock + self.service_times[-1]
                    self.depart_baker = self.time_depart

                # Calculate for other users    
                self.interarrival_times.append(generate_interarrival_time())
                self.time_arrival = self.clock + self.interarrival_times

        elif self.time_arrival > self.depart_able:
            self.number_in_sys -= 1
            self.num_of_depart += 1
            self.number_in_able -= 1

            if self.number_in_sys > 0:
                self.service_times.append(generate_service_time())
                self.time_depart = self.clock + self.service_times[-1]
                self.depart_able = self.time_depart
            
            if self.number_in_able <= 0:
                self.server_status_able = 0
                self.depart_able = float('inf')
                # self.time_depart = float('inf')
            
        elif self.time_arrival > self.depart_baker:
            self.number_in_sys -= 1
            self.num_of_depart += 1
            self.number_in_baker -= 1

            if self.number_in_sys > 0:
                self.service_times.append(generate_service_time())
                self.time_depart = self.clock + self.service_times[-1]
                self.depart_baker = self.time_depart
            
            elif self.number_in_baker <= 0:
                self.server_status_baker = 0
                self.depart_baker = float('inf')
                self.time_depart = float('inf')