import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# Number of radars
NUM_RADARS = 3
MAX_DISTANCE = 100

# Create radar figure
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.set_title("Multi-Radar Detection System", fontsize=14)
ax.set_ylim(0, MAX_DISTANCE)
ax.set_facecolor("black")
ax.grid(color="lime", linestyle="dotted")

# Radar sweep line
sweep_line, = ax.plot([], [], color="lime", linewidth=2)

# Target points
targets, = ax.plot([], [], 'ro')

def generate_targets():
    """Generate random targets for each radar."""
    angles = []
    distances = []
    for _ in range(NUM_RADARS):
        angles.append(random.uniform(0, 2 * np.pi))
        distances.append(random.uniform(10, MAX_DISTANCE))
    return angles, distances

def update(frame):
    """Update radar animation."""
    angle = np.deg2rad(frame)

    # Update sweep line
    sweep_line.set_data([angle, angle], [0, MAX_DISTANCE])

    # Generate targets
    angles, distances = generate_targets()
    targets.set_data(angles, distances)

    return sweep_line, targets

# Animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 360, 2),
    interval=50,
    blit=True
)

plt.show()