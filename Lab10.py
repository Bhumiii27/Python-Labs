import matplotlib.pyplot as plt

# Create subplots: 1 row, 3 columns
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# ---------------- (a) Line plot ----------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

axs[0].plot(x, y, color="blue")
axs[0].set_xlabel("X Axis")
axs[0].set_ylabel("Y Axis")
axs[0].set_title("Simple Line Plot")

# ---------------- (b) Multiple lines ----------------
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]
y3 = [2, 3, 5, 7, 11]

axs[1].plot(x, y1, label="y=2x")
axs[1].plot(x, y2, label="y=x²")
axs[1].plot(x, y3, label="Prime numbers")
axs[1].set_xlabel("X Axis")
axs[1].set_ylabel("Y Axis")
axs[1].set_title("Multiple Lines")
axs[1].legend()

# ---------------- (c) Bar chart ----------------
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

axs[2].bar(languages, popularity, color="skyblue", edgecolor="black")
axs[2].set_xlabel("Languages")
axs[2].set_ylabel("Popularity (%)")
axs[2].set_title("Popularity of Programming Languages")

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
