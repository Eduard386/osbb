import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--calories", required=True, type=float, help="Total number of calories in this month")
ap.add_argument("-r", "--reduction", required=False, type=float, default=1, help="reduction coefficient")
args = vars(ap.parse_args())

cost_of_one_calorie = 1342.98
value_added_tax = 1.2


def kiev_teplo_energo_bill(calories, reduction):
    bill = calories * cost_of_one_calorie * value_added_tax * reduction
    return bill


bill = kiev_teplo_energo_bill(args["calories"], args["reduction"])

print('Bill from KievTeploEnergo should be {}'.format(bill))
