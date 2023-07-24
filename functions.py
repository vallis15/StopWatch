import time
import tkinter as tk

def start_timer(app):
    if not app.is_running:
        app.is_running = True
        if app.elapsed_time == 0:
            app.start_time = time.time()
        else:
            app.start_time = time.time() - app.elapsed_time
        update_timer(app)

        app.start_button.config(state=tk.DISABLED)
        app.stop_button.config(state=tk.NORMAL)
        app.continue_button.config(state=tk.DISABLED)
        app.reset_button.config(state=tk.DISABLED)

def stop_timer(app):
    if app.is_running:
        app.is_running = False
        app.elapsed_time = time.time() - app.start_time

        app.start_button.config(state=tk.NORMAL)
        app.stop_button.config(state=tk.DISABLED)
        app.continue_button.config(state=tk.NORMAL)
        app.reset_button.config(state=tk.NORMAL)

def continue_timer(app):
    if not app.is_running:
        app.is_running = True
        app.start_time = time.time() - app.elapsed_time
        update_timer(app)

        app.start_button.config(state=tk.DISABLED)
        app.stop_button.config(state=tk.NORMAL)
        app.continue_button.config(state=tk.DISABLED)
        app.reset_button.config(state=tk.DISABLED)

def reset_timer(app):
    app.is_running = False
    app.start_time = 0
    app.elapsed_time = 0
    app.time_label.config(text="Time: 0.0s")

    app.start_button.config(state=tk.NORMAL)
    app.stop_button.config(state=tk.DISABLED)
    app.continue_button.config(state=tk.DISABLED)
    app.reset_button.config(state=tk.DISABLED)

def update_timer(app):
    if app.is_running:
        app.elapsed_time = time.time() - app.start_time
        app.time_label.config(text="Time: {:.1f}s".format(app.elapsed_time))
        app.root.after(100, update_timer, app)
