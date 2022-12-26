import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
    def study(self):
        print("Час навчатись")
        self.progress+=0.12
        self.gladness-=3
    def sleep(self):
        print("Час спати")
        self.gladness+=3
    def chill(self):
        print("Час відпочинку")
        self.progress+=0.1
        self.gladness+=5
    def is_alive(self):
        if self.progress<-0.5:
            print("Відрахували...")
            self.alive=False
        elif self.gladness<=0:
            print("Дипресія")
            self.alive=False
        elif self.progress>5:
            print("Закінчив екстерном")
            self.alive=False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        cube=random.randint(1,3)
        if cube==1:
            self.study()
        elif cube==2:
            self.sleep()
        elif cube==3:
            self.chill()
        self.end_of_day()
        self.is_alive()

nick=Student(name="Maks")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
