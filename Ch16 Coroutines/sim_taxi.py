import sys
import random
from collections import namedtuple
import queue
import argparse

DEFAULT_NUMBER_OF_TAXIS = 3
# DEFAULT_END_TIME = 80
DEFAULT_END_TIME = 180
SEARCH_DURATION = 4
TRIP_DURATION = 10
DEPARTURE_INTERVAL = 5

Event = namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time = 0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')

class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, prev_action = current_event
            print('taxi:', proc_id, proc_id*'   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + int(random.expovariate(1/TRIP_DURATION)) + 1
            # next_time = sim_time + 1
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))

def main():
    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(DEFAULT_NUMBER_OF_TAXIS)
    }
    sim = Simulator(taxis)
    sim.run(DEFAULT_END_TIME)

if __name__ == '__main__':
    main()
