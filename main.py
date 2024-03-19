

def generate_bowl(starting_radius: float,
                  radius_step: float,
                  time_per_segment_s: float,
                  number_of_segments: int) -> list[tuple[tuple[float, float, float], float]]:
    """
    :param starting_radius: the topmost and largest radius of the bowl.
    :param radius_step: the amount the radius should decrease by between each segment.
    :param time_per_segment_s: the amount of time between each segment.
    :param number_of_segments: the number of segments in the bowl.
    :return: a list of circles, defined as a tuple containing a position in 3d space and a radius, which form the bowl.
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