import pandas as pd

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

dist_planets = pd.Series(data = distance_from_sun, index = planets)

time_light = dist_planets / 18

close_planets = time_light[time_light < 40]