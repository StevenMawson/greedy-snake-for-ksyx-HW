import tkinter as tk
import serial
import random

# 初始化Arduino串口
arduino = serial.Serial('COM3', 9600)

# 贪吃蛇逻辑
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=320, height=320)
        self.canvas.pack()
        self.snake = [(5, 5), (5, 6), (5, 7)]
        self.food = (10, 10)
        self.direction = (0, -1)
        self.game_over = False

        self.update_game()

    def update_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.draw_game()
            self.root.after(100, self.update_game)

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = (random.randint(0, 15), random.randint(0, 15))
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:] or head[0] < 0 or head[0] >= 16 or head[1] < 0 or head[1] >= 16:
            self.game_over = True

    def draw_game(self):
        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0]*20, segment[1]*20, segment[0]*20+20, segment[1]*20+20, fill="green")
        self.canvas.create_rectangle(self.food[0]*20, self.food[1]*20, self.food[0]*20+20, self.food[1]*20+20, fill="red")

    def set_direction(self, direction):
        self.direction = direction

# Tkinter主窗口
root = tk.Tk()
game = SnakeGame(root)

# 读取摇杆输入并更新方向
def read_joystick():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip().split(',')
        x = int(data[0])
        y = int(data[1])
        if x < 300:
            game.set_direction((0, -1))
        elif x > 700:
            game.set_direction((0, 1))
        elif y < 300:
            game.set_direction((-1, 0))
        elif y > 700:
            game.set_direction((1, 0))
    root.after(100, read_joystick)

read_joystick()
root.mainloop()