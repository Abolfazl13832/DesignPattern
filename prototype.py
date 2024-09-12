class Cinema:
    pass


class Movie:
    pass

class Time:
    pass

class Hall:
    def __init__(self, name, cinema, capacity):
        self.name = name 
        self.cinema = cinema
        self.capacity = capacity

class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None
        

class Sans:
    def __init__(self,cinema, movie, time, hall):
        self.cinema = cinema 
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        """Prototype all seats of selected hall"""
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))

if __name__ == "__main__":
    cinema = Cinema()
    movie = Movie()
    time = Time()
    hall = Hall("Hale_name",cinema,60)
    sans = Sans(cinema,movie,time,hall)

    print(len(sans.seats))
    print((sans.seats[8].number))
