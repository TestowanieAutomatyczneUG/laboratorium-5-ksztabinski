class Hamming:
    def distance(self, string1, string2):
        if len(string1) == len(string2):
            if string1 == string2:
                return 0
            else:
                counter = 0
                for i in range(0, len(string1)):
                    if string1[i] != string2[i]:
                        counter += 1
                return counter
        elif len(string1) > len(string2) and (len(string1) >= 1 and len(string2) >= 1):
            raise ValueError("str1 is longer than str2")
        elif len(string1) < len(string2) and (len(string1) >= 1 and len(string2) >= 1):
            raise ValueError("str2 is longer than str1")
        elif len(string1) == 0 and len(string2) >= 1:
            raise ValueError("str1 cannot be empty")