from sim_taxi import taxi_process
taxi = taxi_process(ident=13, trips=2, start_time=0)
next(taxi)
taxi.send(_.time + 7)
taxi.send(_.time + 3)
taxi.send(_.time + 5)
taxi.send(_.time + 2)
taxi.send(_.time + 6)
taxi.send(_.time + 1)
from inspect import getgeneratorstate
getgeneratorstate(taxi)
