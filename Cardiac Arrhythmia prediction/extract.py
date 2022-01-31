from __future__ import print_function

import cPickle as pickle
import glob
import numpy as np
import os
import subprocess

WFDB = "/deep/group/med/tools/wfdb-10.5.24/build/bin/"
DATA = "/deep/group/med/mitdb"

def extract_wave(idx):
    rdsamp = os.path.join(WFDB, 'rdsamp')
    output = subprocess.check_output([rdsamp, '-r', idx], cwd=DATA)
    data = np.fromstring(output, dtype=np.int32, sep=' ')
    return data.reshape((-1, 3))
    

def extract_annotation(idx):
    rdann = os.path.join(WFDB, 'rdann')
    output = subprocess.check_output([rdann, '-r', idx, '-a', 'atr'], cwd=DATA)
    labels = (line.split() for line in output.strip().split("\n"))
    labels = [(l[0], int(l[1]), l[2], l[6] if len(l) == 7 else None)
                for l in labels]
    return labels
    

def extract(idx):
    data = extract_wave(idx)
    labels = extract_annotation(idx)
    return data, labels

def save(example, idx):
    np.save(os.path.join(DATA, idx), example[0])
    with open(os.path.join(DATA, "{}.pkl".format(idx)), 'w') as fid:
        pickle.dump(example[1], fid)
        

if __name__ == "__main__":
    files = glob.glob(os.path.join(DATA, "*.dat"))
    idxs = [os.path.basename(f).split(".")[0] for f in files]
    for idx in idxs:
        example = extract(idx)
        save(example, idx)
        print("Example {}".format(idx))
