from better_profanity import profanity

class profanity_class:
    def __init__(self , filepath=''):
        self.filepath = filepath
        self.filename = filepath + '.srt'
        self.old_srt_array = []
        self.new_srt_array = []

        '''reading srt file and analysing with profanity filter'''
    def filteration(self):
        with open(self.filename, "r") as myFile:
            filter_string = myFile.read()
        filtered_string = profanity.censor(filter_string)
        # print(filtered)

        f = open(self.filepath + 'new' + '.srt', "w+")
        f.write(filtered_string)
        f.close()

        '''converting text file to array of new and old srt file'''

        fileObj = open(self.filepath+'.srt', "r")
        old_srt_array = fileObj.read().splitlines()
        fileObj.close()
        print(old_srt_array)

        fileObj = open(self.filepath + 'new' + '.srt', "r")
        new_srt_array = fileObj.read().splitlines()
        fileObj.close()
        print(new_srt_array)
        # print(new_srt_array[10][-1:])

        return old_srt_array,new_srt_array

    #This is a comment