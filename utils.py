import numpy as np 
from scipy.io import loadmat 

def mat_to_csv(file_path, save_path):
    data = loadmat(file_path)
    
    z3 = data['z3']
    
    np.save(save_path, {'z3': z3})
    
    print(f"Conversion completed! Files saved as {save_path}.")
    
def jonswap(Hs, w1, wm, gamma=1):
    U = []
    for w in w1:
        if w <= wm:
            zigma = 0.07
        else:
            zigma = 0.09
        term1 = (5 / 16) * (Hs ** 2) * (wm ** 4) * (w ** -5)
        term2 = np.exp(-1.25 * ((wm / w) ** 4))
        term3 = (1 - 0.287 * np.log(gamma))
        term4 = gamma ** (np.exp(-((w - wm) ** 2) / (2 * (zigma ** 2) * (wm ** 2))))
        U.append(term1 * term2 * term3 * term4)
    return np.array(U)

def set_parameters(time, Hs, Tp):
    parameter = {}
    
    parameter['Hs'] = Hs
    parameter['wm'] = 2 * np.pi / Tp
    dw = 2 * np.pi / time
    parameter['w0r'] = np.arange(0.01, 2.5, dw)
    
    return parameter

def generate_data(parameter, RAO, jonswap=jonswap):

    Hs = parameter['Hs']
    wm = parameter['wm']
    w0r = parameter['w0r']
    
    U = jonswap(Hs, w0r, wm)

    wave_ph = 2 * np.pi * np.random.rand(len(w0r))
    diff1 = np.diff(w0r, prepend=w0r[0])
    Aw = np.sqrt(2 * U * diff1)

    t = np.arange(0, 3600, 0.1)
    etal = np.array([np.sum(Aw * np.exp(1j * (w0r * t_ + wave_ph))) for t_ in t])
    
    wave_ph = 2 * np.pi * np.random.rand(len(w0r))
    heave_ts = np.array([np.sum(Aw * RAO * np.exp(1j * (w0r * t_ + wave_ph))) for t_ in t])
    
    return etal, heave_ts, t

def get_rao(filepath):
    RAO_dict = np.load(filepath, allow_pickle=True)
    return np.abs(RAO_dict.item()['z3'])

def create_sequences(data, time_steps=50, n=0):
    X, y = [], []
    for i in range(len(data) - time_steps - n):
        X.append(data[i:i+time_steps, 0])  
        y.append(data[i+time_steps + n, 1])  
    return np.array(X), np.array(y)