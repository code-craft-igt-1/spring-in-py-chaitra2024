import unittest
import statistics_calculate
import math
 
class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics_calculate.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)
 
  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics_calculate.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
 
if __name__ == "__main__":
  unittest.main()