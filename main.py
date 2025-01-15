import time
import tkinter as tk

WORK_TIME = 0.2 * 60  # 25 minutes
SHORT_BREAK_TIME = 0.05 * 60  # 5 minutes
LONG_BREAK_TIME = 0.1 * 60  # 15 minutes


class Pomodoro:
    def __init__(self, root):
        self.root = root

        self.root.title("Pomodoro Timer")
        self.root.geometry("300x300")

        # Timer variables
        self.timer_running = False
        self.time_left = int(WORK_TIME)
        self.work_sessions_completed = 0
        self.current_task = "work"

        # Label to display the timer
        self.label = tk.Label(root, text=self.format_time(self.time_left), font=("Arial", 30))
        self.label.pack(pady=30)

        # Label to display messages
        self.message_label = tk.Label(root, text="Start when ready!", font=("Arial", 15))
        self.message_label.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=30)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side="left", padx=30)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=30)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        if not self.timer_running:
            if self.current_task == "work":
                self.message_label.config(text="Time to work!")

            self.timer_running = True
            self.count_down()

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_left = int(WORK_TIME)
        self.work_sessions_completed = 0
        self.label.config(text=self.format_time(self.time_left))
        self.message_label.config(text="Start when ready!")

    def count_down(self):
        if self.timer_running and self.time_left > 0:
            self.label.config(text=self.format_time(self.time_left))
            self.time_left -= 1
            self.root.after(1000, self.count_down)  # calls itself again after 1 second
        elif self.time_left == 0:
            self.timer_end()

    def timer_end(self):
        if self.current_task == "work":
            self.current_task = "break"
            self.start_break()
        else:
            self.current_task = "work"
            self.start_work()

    def start_break(self):
        if self.work_sessions_completed < 3:
            break_time = SHORT_BREAK_TIME
        else:
            break_time = LONG_BREAK_TIME
            self.work_sessions_completed = 0

        self.time_left = int(break_time)
        self.label.config(text=self.format_time(self.time_left))
        self.timer_running = False

        if break_time == SHORT_BREAK_TIME:
            self.message_label.config(text="Take a short break!")
        else:
            self.message_label.config(text="Take a long break!")

    def start_work(self):
        self.work_sessions_completed += 1
        self.time_left = int(WORK_TIME)
        self.label.config(text=self.format_time(self.time_left))
        self.message_label.config(text="Time to work!")
        self.timer_running = False


# Run app

root = tk.Tk()
app = Pomodoro(root)
root.mainloop()
