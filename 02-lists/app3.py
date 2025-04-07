import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser App")
        
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        
        self.create_grid()
        self.eraser = None
        self.canvas.bind('<Button-1>', self.create_eraser)
        self.canvas.bind('<B1-Motion>', self.move_eraser)
        
    def create_grid(self):
        num_rows = CANVAS_HEIGHT // CELL_SIZE
        num_cols = CANVAS_WIDTH // CELL_SIZE
        
        for row in range(num_rows):
            for col in range(num_cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                
    def create_eraser(self, event):
        if self.eraser is None:
            x1 = event.x
            y1 = event.y
            x2 = x1 + ERASER_SIZE
            y2 = y1 + ERASER_SIZE
            self.eraser = self.canvas.create_rectangle(x1, y1, x2, y2, fill='pink')
            
    def move_eraser(self, event):
        if self.eraser is not None:
            x1 = event.x
            y1 = event.y
            x2 = x1 + ERASER_SIZE
            y2 = y1 + ERASER_SIZE
            
            # Move the eraser
            self.canvas.coords(self.eraser, x1, y1, x2, y2)
            
            # Find and erase overlapping rectangles
            overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
            for item in overlapping:
                if item != self.eraser:
                    self.canvas.itemconfig(item, fill='white')

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()