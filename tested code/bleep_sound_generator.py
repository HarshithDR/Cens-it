import numpy as np
from scipy.io.wavfile import write

class bleep_sound_class:
    def __init__(self,time_difference,N_C_W_index,filepath):
        self.filepath = filepath
        self.N_C_W_index = N_C_W_index
        self.time_difference = time_difference
        self.sps = 44100
        self.freq_hz = 987.77
        self.duration = []
        self.vol = 1

    def bleep(self):
        for a in range(0,len(self.N_C_W_index)):
            self.duration = self.time_difference[a]/1000
            esm = np.arange(self.duration * self.sps)
            wf = np.sin(2 * np.pi * esm * self.freq_hz / self.sps)
            wf_quiet = wf * self.vol
            wf_int = np.int16(wf_quiet * 32767)
            write( self.filepath+ "\\audio2.wav", self.sps, wf_int)