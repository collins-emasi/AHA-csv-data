import numpy as np

from model import BodyAccX, BodyAccY, BodyAccZ, BodyGyroX, BodyGyroY, BodyGyroZ
from utils import Session


def query(label=None, head=None, tail=None):
    s = Session()

    if label:
        accx = s.query(BodyAccX).filter(BodyAccX.label == label).all()
        accy = s.query(BodyAccY).filter(BodyAccY.label == label).all()
        accz = s.query(BodyAccZ).filter(BodyAccZ.label == label).all()

        gyrox = s.query(BodyGyroX).filter(BodyGyroX.label == label).all()
        gyroy = s.query(BodyGyroY).filter(BodyGyroY.label == label).all()
        gyroz = s.query(BodyGyroZ).filter(BodyGyroZ.label == label).all()
    else:
        accx = s.query(BodyAccX).all()
        accy = s.query(BodyAccY).all()
        accz = s.query(BodyAccZ).all()

        gyrox = s.query(BodyGyroX).all()
        gyroy = s.query(BodyGyroY).all()
        gyroz = s.query(BodyGyroZ).all()

    s.close()

    if head:
        accx = accx[0:head]
        accy = accy[0:head]
        accz = accz[0:head]

        gyrox = gyrox[0:head]
        gyroy = gyroy[0:head]
        gyroz = gyroz[0:head]

    if tail:
        accx = accx[-1:-tail-1:-1]
        accy = accy[-1:-tail-1:-1]
        accz = accz[-1:-tail-1:-1]

        gyrox = gyrox[-1:-tail-1:-1]
        gyroz = gyroz[-1:-tail-1:-1]
        gyroy = gyroy[-1:-tail-1:-1]

    acc_data = {
        'x': accx,
        'y': accy,
        'z': accz,
    }
    gyro_data = {
        'x': gyrox,
        'y': gyroy,
        'z': gyroz,
    }

    return acc_data, gyro_data


def plot_acc_data(x, y, z, ax, label=None):
    ax.plot(x, 'r', label='acc in x-axis')
    ax.plot(y, 'g', label='acc in y-axis')
    ax.plot(z, 'b', label='acc in z-axis')
    ax.grid(True, which='both')
    ax.set_ylabel('Acceleration')
    ax.set_xlabel('Time Steps')
    ax.set_title(label)
    ax.legend()


def plot_gyro_data(x, y, z, ax, label=None):
    ax.plot(x, 'r', label='gyro in x-axis')
    ax.plot(y, 'g', label='gyro in y-axis')
    ax.plot(z, 'b', label='gyro in z-axis')
    ax.grid(True, which='both')
    ax.set_ylabel('Gyroscope')
    ax.set_xlabel('Time Steps')
    ax.set_title(label)
    ax.legend()


def get_xyz_ndarray(type_dict):
    x_list = type_dict.get('x')
    y_list = type_dict.get('y')
    z_list = type_dict.get('z')

    length = len(x_list)

    x_data = []
    y_data = []
    z_data = []

    for i in range(length):
        x_data.append({x_list[i].label: np.array(x_list[i].row_data)})
        y_data.append({y_list[i].label: np.array(y_list[i].row_data)})
        z_data.append({z_list[i].label: np.array(z_list[i].row_data)})

    return x_data, y_data, z_data, length
