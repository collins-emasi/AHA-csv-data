import csv
import os
from datetime import datetime as dt

from plot_utils import query

acc_data, gyro_data = query()

if len(acc_data['x']) == len(gyro_data['x']):
    for i in range(len(acc_data['x'])):
        # Getting filename
        acc_title = acc_data['x'][i].label
        gyro_title = gyro_data['x'][i].label

        now = dt.now()
        dt_string = now.strftime("%Y-%m-%dT%H.%M.%S")
        acc_file_name = acc_title + '_' + dt_string + '_' + 'accelerometer' + '.csv'
        gyr_file_name = gyro_title + '_' + dt_string + '_' + 'gyroscope' + '.csv'

        os.chdir("/home/collins/Desktop/MMRdataPipeline/data/acc")

        with open(acc_file_name, 'w', newline='') as a_file:
            writer = csv.writer(a_file)
            for j in range(len(acc_data['x'][i].row_data)):
                row = [acc_data['x'][i].row_data[j], acc_data['y'][i].row_data[j], acc_data['z'][i].row_data[j]]
                writer.writerow(row)

        os.chdir("/home/collins/Desktop/MMRdataPipeline/data/gyro")

        with open(gyr_file_name, 'w', newline='') as g_file:
            writer = csv.writer(g_file)
            for k in range(len(gyro_data['x'][i].row_data)):
                row = [gyro_data['x'][i].row_data[k], gyro_data['y'][i].row_data[k], gyro_data['z'][i].row_data[k]]
                writer.writerow(row)

else:
    print("Inconsistent values")
