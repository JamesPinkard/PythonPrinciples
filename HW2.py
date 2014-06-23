"""
Simulator for resource generation with upgrades
"""

#import simpleplot
import math
import matplotlib.pyplot as plt

#import codeskulptor
#codeskulptor.set_timeout(20)

class ResourceScenario():
    def reset(self):
        self.current_time = 1
        self.total_resources_generated = 1
        self.upgrade_cost = 1
        
    def resources_vs_time(self, upgrade_cost_increment, num_upgrade):
        """
        Build function that performs unit upgrades with specified cost increments
        """
        time_and_resources= []
        self.reset()
        if num_upgrade !=0:
            
            for upgrade in range(num_upgrade):
                upgrade_time = self.current_time
                resources_generated = self.total_resources_generated
                time_and_resources.append([upgrade_time, resources_generated])
                
                self.upgrade_cost += upgrade_cost_increment
                self.calculate_time_till_upgrade(upgrade)
                self.calculate_resources_generated()
                
            return time_and_resources
        
        else:
            return time_and_resources
    
    def calculate_time_till_upgrade(self, upgrade):
        resource_rate = self.get_resource_rate(upgrade)
        added_time = self.upgrade_cost/resource_rate
        self.current_time += added_time

    
    
    def get_resource_rate(self,upgrade):
        rate = upgrade + 2
        return rate
    
    def calculate_resources_generated(self):
        self.total_resources_generated += self.upgrade_cost
        
        

        

#def test():
    #"""
    #Testing code for resources_vs_time
    #"""
    #data1 = resources_vs_time(0.5, 20)
    #data2 = resources_vs_time(1.5, 10)
    #print data1
    #print data2
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])

#test()

def my_test():
    data = ResourceScenario()
    resources1 = data.resources_vs_time(0.0,600)
    resources2 = data.resources_vs_time(0.5,10)
    resources3 = data.resources_vs_time(1.0,10)
    resources4 = data.resources_vs_time(2.0,10)
    x1 = [math.log(p[0]) for p in resources1]
    y1 = [math.log(p[1]) for p in resources1]
    x2 = [p[0] for p in resources2]
    y2 = [p[1] for p in resources2]
    x3 = [math.log(p[0]) for p in resources3]
    y3 = [math.log(p[1]) for p in resources3]
    x4 = [p[0] for p in resources4]
    y4 = [p[1] for p in resources4]    
    print(resources3)
    #plt.plot(x1,y1, 'r', x2, y2, 'g',x3,y3, 'b', x4,y4, 'm')
    plt.plot(x3,y3)
    plt.show()
    
    
my_test()
    
    
    

# Sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]

