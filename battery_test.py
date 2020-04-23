from fz35 import FZ35
from time import sleep
import csv

load = FZ35("COM8")

battery_current = 0.3

stop_ah = 0.3

file_name = "battery_discharge_{}A.csv".format(battery_current)

with open(file_name, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)

    print('starting battery test')
    load.set_current(battery_current)

    csv_writer.writerow(['A', 'V', 'Ah', 'min'])

    while 1:
        a, v, ah, t = load.get_measurement()
        csv_writer.writerow([a, v, ah, t])

        if v <= 2:
            print('low voltage, stopping test')
            break

        if ah >= stop_ah:
            print('maximum battery ah reached, stopping test')
            break

        if a == 0:
            print('current 0, stopping test')
            break