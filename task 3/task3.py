import math
import matplotlib.pyplot as plt

# Initial pose
x = 0
y = 0
theta = 0

# Store waypoints for plotting
trajectory = [(x, y, theta)]

print("Enter commands (forward <val>, left <val>, right <val>)")
print("Type 'done' to finish.\n")

while True:
    command = input("Command: ").strip()

    if command.lower() == "done":
        break

    parts = command.split()

    if len(parts) != 2:
        print("Invalid command. Use: forward <val>, left <val>, or right <val>")
        continue

    action = parts[0].lower()

    try:
        value = float(parts[1])
    except ValueError:
        print("Invalid value. Please enter a number.")
        continue

    # Save initial position before executing command
    initial_x = x
    initial_y = y
    initial_theta = theta

    # Execute command
    if action == "forward":
        # Move in the direction the robot is currently facing
        x += value * math.cos(math.radians(theta))
        y += value * math.sin(math.radians(theta))
        

    elif action == "left":
        # Rotate counter-clockwise
        theta += value
        trajectory.append((x, y, theta))

    elif action == "right":
        # Rotate clockwise
        theta -= value
        trajectory.append((x, y, theta))

    else:
        print("Invalid command.")
        continue

    # Keep theta between 0 and 360 degrees
    theta %= 360

    # Store new waypoint
   

    # Terminal output
    print(
        f"Initial Pos: ({initial_x:.2f}, {initial_y:.2f}, {initial_theta:.2f}) "
        f"| Executing: {command} "
        f"| Final Pos: ({x:.2f}, {y:.2f}, {theta:.2f})"
    )


# -----------------------------
# Plot the trajectory
# -----------------------------

xs = [point[0] for point in  trajectory]
ys = [point[1] for point in trajectory]
thetas = [point[2] for point in trajectory]

plt.figure()

# Plot path
plt.plot(xs, ys, marker='o', label="Robot Path")

# Start and end markers
plt.scatter(xs[0], ys[0], marker='s', s=100, label="Start")
plt.scatter(xs[-1], ys[-1], marker='X', s=100, label="End")

# Heading arrows at every waypoint
arrow_length = 1
xs.pop(-1)
ys.pop(-1)
thetas.pop(-1)

u = [
    arrow_length * math.cos(math.radians(theta))
    for theta in thetas
]

v = [
    arrow_length * math.sin(math.radians(theta))
    for theta in thetas
]

plt.quiver(
        xs,
        ys,
        u,
        v,
        angles='xy',
        scale_units='xy',
        scale=1,
        width=0.01
    )

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Robot Trajectory")
plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show()


