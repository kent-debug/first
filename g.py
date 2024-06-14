import math

# Given values
population_size = 151454 

z_value = 1.96
proportion = 0.5
margin_of_error = 0.05

# Sample size calculation without FPC
sample_size = (z_value**2 * proportion * (1 - proportion)) / (margin_of_error**2)

# Applying FPC
adjusted_sample_size = sample_size / (1 + ((sample_size - 1) / population_size))

# Round up to the nearest whole number
adjusted_sample_size = math.ceil(adjusted_sample_size)

adjusted_sample_size