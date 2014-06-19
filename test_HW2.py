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
        
        actual = self.scenario.resources_vs_time(self.upgrade_cost_increment,self.num)
        
        self.assertItemsEqual(expected, actual)
        
    def setIncrementAndUpgrades(self, upgrade_cost_increment, num_upgrade):
        self.upgrade_cost_increment = upgrade_cost_increment
        self.num_upgrade = num_upgrade
        
        