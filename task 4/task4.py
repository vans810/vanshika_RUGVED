import math
import matplotlib.pyplot as plt

#initial position
x=0
y=0
theta=0

trajectory=[(x,y,theta)]
dt=0.01
while True:
    command=input("Enter command (velocity, angular velocity, time duration) or 'done' to finish: ").strip()
    if command.lower()=="done":
        break
    parts=command.split()
    if len(parts)!=3:
        print("Invalid command. Use: velocity <val>, angular velocity <val>, time duration <val>")
        continue
    try:

        v=float(parts[0])
        omega=float(parts[1])
        duration=float(parts[2])
    except ValueError:
        print("Invalid value. Please enter numbers.")
        continue
    initial_x=x
    initial_y=y
    initial_theta=theta
    count=int(duration/dt)
    for i in range(count):
        x+=v*math.cos(math.radians(theta))*dt
        y+=v*math.sin(math.radians(theta))*dt
        theta+=omega*dt
        theta%=360
        trajectory.append((x,y,theta))
    print(
        f"\nInitial State: "
        f"({initial_x:.2f}, {initial_y:.2f}, {initial_theta:.2f})"
    )

    print(
        f"Command: v={v:.2f}, omega={omega:.2f}, duration={duration:.2f}"
    )

    print(
        f"Final State: "
        f"({x:.2f}, {y:.2f}, {theta:.2f})\n"
    )


# Extract x, y coordinates
xs = [point[0] for point in trajectory]
ys = [point[1] for point in trajectory]

# Plot trajectory
plt.figure()

plt.plot(xs, ys, label="Robot Trajectory")

# Start point
plt.scatter(
    xs[0],
    ys[0],
    marker="s",
    s=100,
    label="Start"
)

# End point
plt.scatter(
    xs[-1],
    ys[-1],
    marker="X",
    s=100,
    label="End"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Continuous Robot Trajectory")

plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show()



    