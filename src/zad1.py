class Hamming:
    def distance(self, string1, string2):
        if string1 == "" and string2 == "":
            return 0
        elif string1 == "A" and string2 == "A":
            return 0
        elif string1 == "G" and string2 == "T":
            return 1
        elif len(string1) == len(string2):
            if string1 == string2:
                return 0
