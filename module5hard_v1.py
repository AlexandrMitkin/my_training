import time

class User():
    def __init__(self, nickname1, password1, age1):
        self.nickname = nickname1
        self.password = hash(password1)
        self.age = age1

class Video():
    def __init__(self,  title1, duration1, time_now=0, adult_mode=False):
        self. title =  title1
        self.duration = duration1
        self.time_now = time_now
        self.adult_mode = adult_mode
        
class UrTube():
    def __init__(self,  Users1=[], Videos1=[], current_user1=""):
        self.Users = Users1
        self.Videos = Videos1
        self.current_user = current_user1

    def log_in(self, nickname1, password1):
        nick = nickname1
        for i in self.Users:
            if i[0] == nick:
                self.current_user = "found"
                break
        print("You are not on the list")

    def register(self, nickname1, password1, age1):
        nick = nickname1
        for i in self.Users:
            if i[0] == nick:
                print(f"The user {nick} already exists")
                break
        self.Users.append((nickname1, hash(password1), age1))
        self.current_user = "found" #вход автоматически
    def log_out(self):
        self.current_user =None
    def __add__(self, v1,v2):
        if isinstance(v1, __main__.Video) and isinstance(v2, __main__.Video):
            return ["v1", "v2"]
        print("hghgh")
    def add(self,*args):
        k=-1
        for i in args:
            k=k+1
            for j in self.Videos:
                if i.title==j[0]:
                    break
            self.Videos.append(args[k])
        print(self.Videos)
    def get_videos(self, ss1):
        ss=str(ss1)
        for i in self.Videos:
            if i[0].upper().find(ss.upper())>-1:
                print(i[0])
    def watch_video(self):
        pass

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1,v2)