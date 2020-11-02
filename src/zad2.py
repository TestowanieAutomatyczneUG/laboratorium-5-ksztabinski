class Roman:
    def __init__(self):
        self.nums = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L"
        }

    def roman(self, value):
        result = ""
        for val, num in sorted(self.nums.items(), reverse=True):
            while value >= val:
                result += num
                value -= val
        return result

