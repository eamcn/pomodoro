import time
import tkinter as tk

WORK_TIME = 25 * 60  # 25 minutes
SHORT_BREAK_TIME = 5 * 60  # 5 minutes
LONG_BREAK_TIME = 15 * 60  # 15 minutes


class Pomodoro:
    def __init__(self, root):
        self.root = root

        self.root.title("Pomodoro Timer")
        self.root.geometry("300x300")

        # Timer variables
        self.timer_running = False
        self.time_left = WORK_TIME
        self.work_sessions_completed = 0

        # Label to display the timer
        self.label = tk.Label(root, text=self.format_time(self.time_left), font=("Arial", 30))
        self.label.pack(pady=30)

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
        return

    def pause_timer(self):
        return

    def reset_timer(self):
        return

    def count_down(self):
        return


# Run app
root = tk.Tk()
app = Pomodoro(root)
root.mainloop()
