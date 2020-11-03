class Song:
    def __init__(self):
        self.lyrics = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree." \
                      "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    def showAll(self):
        res = [i for i in self.lyrics.split('.')]
        res.pop()
        return res

    def getVerse(self, num):
        if num > 12:
            raise ValueError("nie moze byc wiecej niz 12")
        elif num < 1:
            raise ValueError("nie moze byc mniej niz 1")
        else:
            return self.lyrics.split('.')[num - 1] + '.'

    def getVerses(self, num1, num2):
        if isinstance(num1, str) and isinstance(num2, int):
            raise ValueError("pierwszy parametr musi byc liczba")
        elif isinstance(num1, int) and isinstance(num2, str):
            raise ValueError("drugi paramter musi byc liczba")
        elif num1 < 1:
            raise ValueError("pierwszy parametr nie moze byc mniejszy od 1")
        else:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if (num1 - 1) <= i <= (num2 - 1)]