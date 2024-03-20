from math import pi, exp
import matplotlib.pyplot as plt


def saturation_vapor_pressure(temperature):
    return 0.61121 * exp((17.27 * temperature) / (temperature + 237.3))


def relative_to_absolute_humidity(relative_humidity, temperature):
    relative_humidity /= 100
    grams_per_m3 = relative_humidity * (saturation_vapor_pressure(temperature) / 0.378)
    kg_per_m3 = grams_per_m3 / 1000
    kg_per_kg = kg_per_m3 / 1.2041
    return kg_per_kg


def generate_bowl(starting_radius: float,
                  radius_step: float,
                  time_per_segment_s: float,
                  number_of_segments: int) -> list[tuple[float, float]]:
    """
    :param starting_radius: the topmost and largest radius of the bowl.
    :param radius_step: the amount the radius should decrease by between each segment.
    :param time_per_segment_s: the amount of time between each segment.
    :param number_of_segments: the number of segments in the bowl.
    :return: a list of circles, defined as a depth and a radius, which form the bowl.
    """

    """
    for each time segment,
        calculate the new radius by subtracting the radius_step from the previous radius.
        use the evaporation formula to calculate the volume of water that would evaporate in time time_per_segment.
        find height of cone segment (connecting currant to previous circle) needed to achieve the necessary volume.
        use this information to position the new circle.
        append the new circle to the circle list.
    return the circle list   
    """
    circles = [(0, starting_radius)]
    currant_radius = starting_radius
    segment_count = 1

    while segment_count < number_of_segments:
        segment_count += 1
        currant_radius -= radius_step

        # evaporation formula
        air_velocity = 0.2
        temperature = 30
        relative_humidity = 30

        surface_area = ((pi * currant_radius ** 2) + (pi * circles[-1][0] ** 2)) / 2
        absolute_humidity = relative_to_absolute_humidity(relative_humidity, temperature)
        max_humidity = relative_to_absolute_humidity(100, temperature)

        kg_per_hour = (25 + 19 * air_velocity) * surface_area * (max_humidity - absolute_humidity)
        kg_per_second = kg_per_hour / 3600
        volume_per_second = kg_per_second / 998  # divide by density of water
        volume_per_segment = volume_per_second * time_per_segment_s

        # using volume of truncated cone
        last_radius = circles[-1][1]
        depth = volume_per_segment / (
                (pi / 3) * (last_radius ** 2 + currant_radius ** 2 + last_radius * currant_radius))
        circles.append((depth + circles[-1][0], currant_radius))

    return circles


start_radius = 2
radius_step = 2 / 1000
time_per_segment = 3600*2 / 1000
number_of_segments = 1000

bowl = generate_bowl(start_radius, radius_step, time_per_segment, number_of_segments)

print(f"radius reduces by {radius_step * 100}cm every {time_per_segment / 3600}hrs")
for i, b in enumerate(bowl):
    print(f"layer: {i + 1}, radius: {b[1]}m, depth: {b[0] * 100}cm")


data = [[1, 2], [2, 4], [3, 1], [4, 5], [5, 3]]

# Extract x and y values from the data
x = [row[0] for row in bowl]
y = [row[1] for row in bowl]

# Plot the data
plt.plot(x, y, marker='o')  # You can use a different marker if needed
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot from a 2D array')
plt.grid(True)
plt.show()