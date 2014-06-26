"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        '''
        Constructor
        '''
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._cookies_per_second = 1.0
        self._history_list = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return 'Total Cookies: ' + str(self._total_cookies) + '\n' + \
        'Current Cookies: ' + str(self._current_cookies) + '\n' + \
        'Current Time: ' +  str(self._current_time) + '\n' + \
        'Cookies Per Second: ' + str(self._cookies_per_second)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cookies_per_second
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time_until_cookies = (cookies - self._current_cookies) / self._cookies_per_second
        time_remainder = time_until_cookies - int(time_until_cookies)
        if time_remainder > 0.0:
            time_until_cookies = int(time_until_cookies) +  1.0
        return float(time_until_cookies)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        self._total_cookies += time * self._cookies_per_second
        self._current_cookies += time * self._cookies_per_second
        self._current_time += time 
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._cookies_per_second += additional_cps
            
            current_time = self.get_time()
            total_cookies = self._total_cookies
            current_status = (current_time, item_name, cost, total_cookies)
            self._history_list.append(current_status)
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    simulator_build_info = build_info.clone()
    simulator_state = ClickerState()
    current_time = simulator_state.get_time()
    time_left = duration - current_time    
    
    while time_left >= 0.0:
        
        cookies = simulator_state.get_cookies()
        cookie_rate = simulator_state.get_cps()
        current_time = simulator_state.get_time()
        time_left = duration - current_time
        
        if time_left <= 0:
            break
        
        recommended_item = strategy(cookies, cookie_rate, time_left, simulator_build_info)
        if recommended_item == None:
            break
        
        recommended_item_cost = simulator_build_info.get_cost(recommended_item)
        time_until_recommended_item = simulator_state.time_until(recommended_item_cost)
        if time_until_recommended_item > time_left:
            break
        
        simulator_state.wait(time_until_recommended_item)
        recommended_item_cps = simulator_build_info.get_cps(recommended_item)
        simulator_state.buy_item(recommended_item, recommended_item_cost, recommended_item_cps)
        simulator_build_info.update_item(recommended_item)
        
    if current_time < duration:
        simulator_state.wait(duration - current_time)
            
    
    return simulator_state


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Always buys the cheapest item
    """
    
    available_items = build_info.build_items()
    costs_of_items = [build_info.get_cost(item) for item in available_items]
    cookies_left = cookies + (cps * time_left)
    available_costs = []
    for item_cost in costs_of_items:
        if item_cost <= cookies_left:
            available_costs.append(item_cost)
    
    if available_costs == []:
        return None
    
    min_cost = min(available_costs)
    for item in available_items:
        if build_info.get_cost(item) == min_cost:
            recommended_item = item
    return recommended_item

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Always buys the most expensive item
    """
    available_items = build_info.build_items()
    costs_of_items = [build_info.get_cost(item) for item in available_items]
    cookies_left = cookies + (cps * time_left)
    available_costs = []
    for item_cost in costs_of_items:
        if item_cost <= cookies_left:
            available_costs.append(item_cost)
    
    if available_costs == []:
        return None
    
    max_cost = max(available_costs)
    for item in available_items:
        if build_info.get_cost(item) == max_cost:
            recommended_item = item
    return recommended_item

def strategy_best(cookies, cps, time_left, build_info):
    """
    Always buys the item with the highest rate per cost
    """
    available_items = build_info.build_items()
    costs_of_items = [build_info.get_cost(item) for item in available_items]
    cookies_left = cookies + (cps * time_left)
    available_costs = get_available_costs(costs_of_items, cookies_left)
    
    
    if available_costs == []:
        return None
          
    rate_per_cost_dict = get_rate_per_cost_dict(available_items, available_costs, build_info)
    rpc = get_rpc(rate_per_cost_dict)
    max_rate_per_cost = max(rpc)
    recommended_item = rate_per_cost_dict[max_rate_per_cost]
            
    return recommended_item

def get_available_costs(costs_of_items, cookies_left):
    """
    returns costs for items that can be bought within the time limit
    """
    available_costs = []
    for item_cost in costs_of_items:
        if item_cost <= cookies_left:
            available_costs.append(item_cost)
            
    return available_costs

def get_rate_per_cost_dict(available_items, available_costs, build_info):
    """
    returns dictionary of items and the rate per cost
    """
    rate_per_cost_dict = {}
    for item in available_items:
        if build_info.get_cost(item) in available_costs:
            available_item_cost = build_info.get_cost(item)
            available_item_rate = build_info.get_cps(item)
            rate_per_cost = available_item_rate/available_item_cost
            
            rate_per_cost_dict[rate_per_cost] = item
    return rate_per_cost_dict

def get_rpc(rate_per_cost_dict):
    """
    returns list of rates per costs
    """
            
    rpc = []
    for rate in rate_per_cost_dict.keys():
        rpc.append(rate)
        
    return rpc
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
    

