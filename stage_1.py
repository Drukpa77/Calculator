units = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}

# This funciton converts the value into SI Unit of meters.


def convert_to_meter(val, unit):
    if(unit == "m"):
        return val

    unit_val = [value for key, value in units.items() if key == unit][0]

    return float(unit_val) * val

# This function calculates the value in the unit specified by the user and returns the output as result


def calculate_value(final_unit, num1):

    result = 0

    if (final_unit == "m"):
        return math.floor(num1)

    for key, value in units.items():
        if(key == final_unit):
            result = float(num1) / float(value)

    if(result < 1):
        return format(result, "f")
    return round(result)


def convert(get_value, initial_unit, final_unit):
    value = convert_to_meter(get_value, initial_unit)
    return calculate_value(final_unit, value)


def main():

    num1 = int(input('Enter the value: '))
    print("list of units:cm, m, km, mm")
    unit1 = input('Which unit do you want it converted from:  ')
    unit2 = input('Which unit do you want it converted to: ')

    result = convert(num1, unit1, unit2)

    print(result)


if(__name__ == "__main__"):
    main()
