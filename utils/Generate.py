import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Event

from utils.Callpy import CallPy

class Generate:
    def __init__(self, start, end, path):
        self.pool = ProcessPoolExecutor(max(4,os.cpu_count()))
        exit.event = Event()
        self.start = start
        self.end = end
        self.path = path

    def __call__(self):
        return list(self.pool.map(CallPy(self.path), range(self.start,self.end+1)))