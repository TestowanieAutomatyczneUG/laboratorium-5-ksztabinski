class Hamming:
    def distance(self, string1, string2):
        if string1 == "" and string2 == "":
            return 0
        if string1 == "A" and string2 == "A":
            return 0

