from datetime import datetime
from tkinter import *
# from icon import img
import base64
import os


def cal_week():
    week = -1
    times = datetime.now().timetuple()
    month = times[1]
    day = times[2]
    week_end = -1
    month_end = -1
    if month == 7:
        month_end = 7
        if 3 <= day <= 9:
            week = 4
            week_end = 10
        elif 10 <= day <= 16:
            week = 5
            week_end = 17
        elif 17 <= day <= 23:
            week = 6
            week_end = 24
        elif 24 <= day <= 30:
            week = 7
            week_end = 31
        elif day == 31:
            week = 8
            month_end = 8
            week_end = 7
    elif month == 8:
        month_end = 8
        if 1 <= day <= 6:
            week = 8
            week_end = 7
        elif 7 <= day <= 13:
            week = 9
            week_end = 14
        elif 14 <= day <= 20:
            week = 10
            week_end = 21
        elif 21 <= day <= 27:
            week = 11
            week_end = 28
        elif 28 <= day <= 31:
            week = 12
            month_end = 9
            week_end = 4
    elif month == 9:
        month_end = 9
        if 1 <= day <= 3:
            week = 12
            week_end = 4
        else:
            week = week_end = month_end = "END"

    return week, week_end, month_end


class Countdown:

    window = Tk()
    window.title("MSc Project Timer")
    window.geometry("350x139")

    # tmp = open("tmp.ico", "wb+")
    # tmp.write(base64.b64decode(img))
    # tmp.close()
    # window.iconbitmap('tmp.ico')  # add icon
    # os.remove("tmp.ico")

    week, week_end, month_end = cal_week()

    zero_label = Label(text=f"Week {week}", font=('思源黑体 CN Bold', 15), anchor='w')
    first_label = Label(text="%-21s" % "Week ends in", font=('思源黑体 CN Regular', 15), anchor='w')
    first_label_time = Label(font=('思源黑体 CN Regular', 15), anchor='e')
    second_label = Label(text="%-17s" % "Project ends in", font=('思源黑体 CN Regular', 15), anchor='w')
    second_label_time = Label(font=('思源黑体 CN Regular', 15), anchor='e')
    time_label = Label(font=('思源黑体 CN Regular', 15), anchor='e')

    def __init__(self):
        self.zero_label.place(x=25, y=25, width=150, height=25)
        self.first_label.place(x=25, y=55, width=293, height=30)
        self.first_label_time.place(x=170, y=55, width=160, height=30)
        self.second_label.place(x=25, y=85, width=293, height=30)
        self.second_label_time.place(x=170, y=85, width=160, height=30)
        self.time_label.place(x=120, y=23, width=210, height=30)

        self.refresh_week()
        self.refresh_week_ends()
        self.refresh_proj_ends()
        self.refresh_time()
        self.window.resizable(False, False)
        self.window.mainloop()

    def refresh_week(self):
        self.week, self.week_end, self.month_end = cal_week()
        self.zero_label = Label(text=f"Week {self.week}")
        self.zero_label.update()
        self.window.after(1000, self.refresh_week)

    def refresh_week_ends(self):
        week_end = str(datetime(year=2023, month=self.month_end, day=self.week_end) - datetime.now())[:-7].split(", ")
        if len(week_end) > 1:
            week_end_d = week_end[0]
            week_end_t = week_end[1]
        else:
            week_end_d = ""
            week_end_t = week_end[0]
        self.first_label_time.config(text="%-8s%s" % (week_end_d, week_end_t))
        self.first_label_time.update()
        self.window.after(1000, self.refresh_week_ends)

    def refresh_proj_ends(self):
        proj_end = str(datetime(year=2023, month=9, day=2) - datetime.now())[:-7].split(", ")
        self.second_label_time.config(text="%-9s%s" % (proj_end[0], proj_end[1]))
        self.second_label_time.update()
        self.window.after(1000, self.refresh_proj_ends)

    def refresh_time(self):
        self.time_label.config(text="%s" % str(datetime.now())[:-7])
        self.time_label.update()
        self.window.after(1000, self.refresh_time)


if __name__ == "__main__":
    tasks = Countdown()
