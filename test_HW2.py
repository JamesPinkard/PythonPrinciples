import unittest
import random
from HW2 import ResourceScenario


class ResourceScenarioTests(unittest.TestCase):
    
    def setUp(self):
        self.resource_and_time = []
        self.scenario = ResourceScenario()
        
        
    def test_resourcesVsTime_NoCostIncrementsOrUpgrades_ReturnEmptyList(self):
        self.setIncrementAndUpgrades(0, 0)
        expected = []
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment,self.num_upgrade)
        
        self.assertItemsEqual(expected, actual)

        
    def test_resourcesVsTime_OneIncrementOneUpgrade_ReturnListOfOnes(self):
        self.setIncrementAndUpgrades(1, 1)
        expected = [[1,1]]
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment, self.num_upgrade)
        
        self.assertItemsEqual(expected, actual)
        
    def test_resourcesVsTime_OneIncrementTwoUpgrades_ReturnListOfTwoResourceStatus(self):
        self.setIncrementAndUpgrades(1, 2)
        expected = [[1,1], [2, 3]]
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment,self.num_upgrade)
        
        self.assertListEqual(expected, actual)
        
    def test_resourcesVsTime_TwentyHalfIncrementUpgrades_ReturnLisOfTwentyStatusResources(self):
        self.setIncrementAndUpgrades(0.5, 20)
        expected = [[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment,self.num_upgrade)
        
        self.assertEqual(len(expected), len(actual))
        self.assertAlmostEqual(expected[10][0],actual[10][0])
        
    def test_resourcesVsTime_TenOneAndHalfIncrementUpgrades_ReturnLisOfTenStatusResources(self):
        self.setIncrementAndUpgrades(1.5, 10)
        expected = [[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment,self.num_upgrade)
        
        self.assertEqual(len(expected), len(actual))
        self.assertAlmostEqual(expected[5][0],actual[5][0])    


        
    def setIncrementAndUpgrades(self, upgrade_cost_increment, num_upgrade):
        self.upgrade_cost_increment = upgrade_cost_increment
        self.num_upgrade = num_upgrade
        
        
        
        