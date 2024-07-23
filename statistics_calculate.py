import statistics
import math
def calculateStats(numbers):
    stats={}
    if numbers:
        average = statistics.mean(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
    else:
        average = maximum = minimum = math.nan
    stats.update({"avg":average, "max":maximum, "min":minimum})
    return stats
  
