import time
import sys
from time import sleep


class User():
    def __init__(self, nickname1, password1, age1):
        self.nickname = nickname1
        self.password = hash(password1)
        self.age = age1


class Video():
    def __init__(self, title1, duration1, time_now=0, adult_mode=False):
        self.title = title1
        self.duration = duration1
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.vid = [self.title, self.duration, self.time_now, self.adult_mode]


class UrTube():
    def __init__(self, Users1=[], Videos1=[], current_user1=None):
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
        r = 0
        for i in self.Users:
            if i[0] == nick:
                print(f"The user {nick} already exists")
                r = 1
                break
        if r == 0:
            self.Users.append((nickname1, hash(password1), age1))
            self.current_user = nick  # вход автоматически

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        k = -1
        for i in args:
            k = k + 1
            for j in self.Videos:
                if i.title == j[0]:
                    break
            self.Videos.append(args[k].vid)

    def get_videos(self, ss1):
        ss = str(ss1).upper()
        spisok_name = []
        k = -1
        for i in self.Videos:
            k = k + 1
            if self.Videos[k][0].upper().find(ss) > -1:
                spisok_name.append(self.Videos[k][0])
        return spisok_name

    def watch_video(self, ss1):
        k = -1
        ss = ""
        for i in self.Videos:
            k = k + 1
            if self.Videos[k][0].find(ss1) > -1:
                if self.current_user == None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    break
                elif self.Videos[k][3] == False:
                    for j in range(self.Videos[k][1]):
                        sleep(1)
                        sys.stdout.write(str(j + 1) + " ")
                        break
                else:
                    for i in self.Users:
                        if i[0] == self.current_user:
                            if int(i[2]) < 18:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                                break
                            else:
                                for j in range(self.Videos[k][1]):
                                    sleep(1)
                                    sys.stdout.write(str(j + 1) + " ")
                                print("the end of the video".upper())
                                break


# def print_there(x, y, text):
#   sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
#  sys.stdout.flush()
# print_there(10, 20, "text")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print()

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
print()

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
print()

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
