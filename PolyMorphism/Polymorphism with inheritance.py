class Bird:

    def intro(self):
        print('There are many type of Birds')

    def flight(self):
        print('There are many birds that can fly and some cannot')


class Sparrow(Bird):

    def intro(self):
        print('---Sparrow intro----')

    def flight(self):
        print('Sparrow can fly')


class Ostrich(Bird):

    def intro(self):
        print('---Ostrich Intro----')

    def flight(self):
        print('Ostrich cannot fly')


obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

for Birds_Fly in (obj_bird, obj_sparrow, obj_ostrich):
    Birds_Fly.intro()
    print()
    Birds_Fly.flight()
