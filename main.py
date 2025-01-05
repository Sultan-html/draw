#импорт ткинтер
import tkinter as tk
#функция для начала рисования
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x + 5, event.y + 5
#функция для рисования
def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2)
    last_x, last_y = event.x, event.y

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack()

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()
