import tkinter as tk
import functions

class StopWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="Time: 0.0s", font=("Helvetica", 20))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.continue_button = tk.Button(root, text="Continue", command=self.continue_timer, state=tk.DISABLED)
        self.continue_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Annul", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        functions.start_timer(self)

    def stop_timer(self):
        functions.stop_timer(self)

    def continue_timer(self):
        functions.continue_timer(self)

    def reset_timer(self):
        functions.reset_timer(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopWatch(root)
    root.mainloop()
