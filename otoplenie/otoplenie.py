import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sum", required=True, type=float, help="Total sum from KievTeploEnergo")
ap.add_argument("-c", "--cubes", required=True, type=float, help="Total number of hot water cubes")
args = vars(ap.parse_args())

total_living_space = 7980.40
cost_of_hot_water_cube = 98.89


def one_meter_heating_cost(sum, cubes):
    total_cost_of_hot_water = cubes * cost_of_hot_water_cube
    total_cost_of_heating = sum - total_cost_of_hot_water
    one_meter_heating_cost = total_cost_of_heating / total_living_space
    return one_meter_heating_cost


cost = one_meter_heating_cost(args["sum"], args["cubes"])

print('One meter heating costs {} this month'.format(cost))
