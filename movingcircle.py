import matplotlib.pyplot as plt

x_limit = int(input("Enter X-axis limit (e.g., 10): "))
y_limit = int(input("Enter Y-axis limit (e.g., 10): "))
circle_radius = float(input("Enter circle radius (e.g., 0.5): "))

fig, ax = plt.subplots()

ax.set_xlim(0, x_limit)
ax.set_ylim(0, y_limit)

x, y = x_limit // 2, y_limit // 2

circle = plt.Circle((x, y), circle_radius)
ax.add_patch(circle)

step = 0.5

def on_key(event):
    global x, y

    if event.key == 'left':
        x -= step
    elif event.key == 'right':
        x += step
    elif event.key == 'up':
        y += step
    elif event.key == 'down':
        y -= step

    x = max(circle_radius, min(x, x_limit - circle_radius))
    y = max(circle_radius, min(y, y_limit - circle_radius))

    circle.center = (x, y)
    fig.canvas.draw()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Use Arrow Keys to Move Circle")

plt.show()