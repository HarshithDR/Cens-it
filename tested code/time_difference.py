class time_diff_class:
    def __init__(self,ncw_index):
        self.first_time_hr = []
        self.first_time_min = []
        self.first_time_sec = []
        self.first_time_millisec = []

        self.second_time_hr = []
        self.second_time_min = []
        self.second_time_sec = []
        self.second_time_millisec = []

        self.time_difference = []

        self.N_C_W_index = ncw_index

    def difference(self):
        for b in range(0, len(self.N_C_W_index)):
            # print(N_C_W_index[b][0:2])
            self.first_time_hr.append(int(self.N_C_W_index[b][0:2]))
            self.first_time_min.append(int(self.N_C_W_index[b][3:5]))
            self.first_time_sec.append(int(self.N_C_W_index[b][6:8]))
            self.first_time_millisec.append(int(self.N_C_W_index[b][9:12]))

            self.second_time_hr.append(int(self.N_C_W_index[b][17:19]))
            self.second_time_min.append(int(self.N_C_W_index[b][20:22]))
            self.second_time_sec.append(int(self.N_C_W_index[b][23:25]))
            self.second_time_millisec.append(int(self.N_C_W_index[b][26:]))

            difference = ((self.second_time_hr[b] * 3600000) + (self.second_time_min[b] * 60000) + (self.second_time_sec[b] * 1000) +
                          self.second_time_millisec[b]) - \
                         ((self.first_time_hr[b] * 3600000) + (self.first_time_min[b] * 60000) + (self.first_time_sec[b] * 1000) +
                          self.first_time_millisec[b])
            self.time_difference.append(difference)

        # print(time_difference)
        return self.time_difference