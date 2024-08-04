import tkinter as tk

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.reset = True
        self.time = 0

        self.label = tk.Label(self.root, text=self.format_time(self.time), font=("Arial", 50))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start, font=("Arial", 12))
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause, font=("Arial", 12))
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_time, font=("Arial", 12))
        self.reset_button.pack(side=tk.LEFT, padx=20)

        self.update_clock()

    def format_time(self, time):
        minutes = time // 6000
        seconds = (time // 100) % 60
        milliseconds = time % 100
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    def start(self):
        if not self.running:
            self.running = True
            self.reset = False
            self.update_clock()

    def pause(self):
        self.running = False

    def reset_time(self):
        self.running = False
        self.reset = True
        self.time = 0
        self.label.config(text=self.format_time(self.time))

    def update_clock(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time(self.time))
        if not self.reset:
            self.root.after(10, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
