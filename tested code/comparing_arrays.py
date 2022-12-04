class compare_array:
    def __init__(self,a,b):
        self.old_srt_array = a
        self.new_srt_array = b
        self.N_C_W_index = []

    def compare(self):
        for a in range(0, len(self.old_srt_array)):
            if self.new_srt_array[a] == self.old_srt_array[a]:
                pass
            else:
                try:
                    int(self.old_srt_array[a - 1][-1:])
                    self.N_C_W_index.append(self.old_srt_array[a - 1])
                    # print(N_C_W_index)
                except:
                    self.N_C_W_index.append(self.old_srt_array[a - 2])
        return self.N_C_W_index
