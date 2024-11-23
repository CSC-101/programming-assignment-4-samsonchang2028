from typing import Optional
import hw3
import build_data
from data import CountyDemographics

full_data = build_data.get_data()
def is_float(num:int)->Optional[float]:
    try:
        num = float(num)
        print(num)
        return True
    except ValueError:
        return False
def is_function(list_value):
    if list_value[2] == 'Percent 65 Percent or Older':
        return True
    elif list_value[2] == 'Percent Under 18 Years':
        return True
    elif list_value[2] == 'Percent Under 5 Years':
        return True
    elif list_value[2] == "Bachelor's Degree or Higher":
        return True
    elif list_value[2] == 'High School or Higher':
        return True
    elif list_value[2] == 'American Indian and Alaska Native Alone':
        return True
    elif list_value[2] == 'Asian Alone':
        return True
    elif list_value[2] == 'Black Alone':
        return True
    elif list_value[2] == 'Hispanic or Latino':
        return True
    elif list_value[2] == 'Native Hawaiian and Other Pacific Islander Alone':
        return True
    elif list_value[2] == 'Two or More Races':
        return True
    elif list_value[2] == 'White Alone':
        return True
    elif list_value[2] == 'White Alone, not Hispanic or Latino':
        return True
    elif list_value[2] == 'Per Capita Income':
        return True
    elif list_value[2] == 'Persons Below Poverty Level':
        return True
    elif list_value[2] == 'Median Household Income':
        return True
    elif list_value[2] == '2010 Population':
        return True
    elif list_value[2] == '2014 Population':
        return True
    elif list_value[2] == 'Population Percent Change':
        return True
    elif list_value[2] == 'Population per Square Mile':
        return True
    else:
        return False
def operations_seconds_element(line_list):
    if line_list[0] == 'filter-gt':
        if line_list[1] == 'Education':
            if not is_float(line_list[3]):
                print('Value is not a float')
            elif is_function(line_list):
                if len(line_list) >=5:
                    print('Argument is too long, it is an invalid argument')
                else:
                    return hw3.education_greater_than(full_data,line_list[2],float(line_list[3]))
            else:
                print('Invalid argument')
        elif line_list[1] == 'Ethnicities':
            if not is_float(line_list[3]):
                print('Value is not a float')
            elif is_function(line_list):
                if len(line_list) >=5:
                    print('Argument is too long, it is an invalid argument')
                else:
                    return hw3.ethnicity_greater_than(full_data,line_list[2],line_list[3])
            else:
                print('Invalid argument')
        elif line_list[1] == 'Income':
            return hw3.below_poverty_level_greater_than(full_data,line_list[2])
        else:
            print('System Error,cannot find comparison for filter-gt')
    elif line_list[0] == 'filter-lt':
        if line_list[1] == 'Education':
            if not is_float(line_list[3]):
                print('Value is not a float')
            elif is_function(line_list):
                if len(line_list) >=5:
                    print('Argument is too long, it is an invalid argument')
                else:
                    return hw3.education_less_than(full_data,line_list[2],float(line_list[3]))
        elif line_list[1] == 'Ethnicities':
            if not is_float(line_list[3]):
                print('Value is not a float')
            elif is_function(line_list):
                if len(line_list) >=5:
                    print('Argument is too long, it is an invalid argument')
                else:
                    return hw3.ethnicity_less_than(full_data, line_list[2], float(line_list[3]))
        elif line_list[1] == 'Income':
            return hw3.below_poverty_level_less_than(full_data, line_list[2])
        else:
            print('System Error,cannot find comparison for filter-lt')
    elif line_list[0] == 'population':
        if line_list[1] == 'Education':
            if is_function(line_list):
                return hw3.population_by_education(full_data,line_list[2])
            else:
                print('Invalid argument')
        elif line_list[1] == 'Ethnicities':
            if is_function(line_list):
                return hw3.population_by_ethnicity(full_data, line_list[2])
            else:
                print('Invalid argument')
        elif line_list[1] == 'Income':
            if is_function(line_list):
                return hw3.population_below_poverty_level(full_data)
            else:
                print('Invalid argument')
    elif line_list[0] == 'percent':
        if line_list[1] == 'Education':
            return hw3.percent_by_education(full_data,line_list[2])
        elif line_list[1] == 'Ethnicities':
            return hw3.percent_by_ethnicity(full_data, line_list[2])
        elif line_list[1] == 'Income':
            return hw3.percent_below_poverty_level(full_data)
        else:
            print('System Error, cannot find comparison for percent')
def print_demo(demo_list:list[CountyDemographics]):
    for attributes in demo_list:
        print(attributes.county,',',attributes.state)
        print('Population',attributes.population['2014 Population'])
        print('Age Data')
        print('\t Percent Under 5 Years Old',attributes.age['Percent Under 5 Years'],'%')
        print('\t Percent Under 18 Years Old',attributes.age['Percent Under 18 Years'],'%')
        print('\t Percent 65 and Over',attributes.age['Percent 65 and Older'],'%')
        print('Education Data')
        print('\t Bachelor or Higher',attributes.education["Bachelor's Degree or Higher"],'%')
        print('\t High School or Higher',attributes.education['High School or Higher'],'%')
        print('Ethnicities Data')
        print('\t American Indian and Alaska Native Alone',attributes.ethnicities['American Indian and Alaska Native Alone'],'%')
        print('\t Asian Alone',attributes.ethnicities['Asian Alone'],'%')
        print('\t Black Alone',attributes.ethnicities['Black Alone'],'%')
        print('\t Hispanic or Latino',attributes.ethnicities['Hispanic or Latino'],'%')
        print('\t Native Hawaiian and Other Pacific Islander Alone',attributes.ethnicities['Native Hawaiian and Other Pacific Islander Alone'],'%')
        print('\t Two or More Races',attributes.ethnicities['Two or More Races'],'%')
        print('\t White Alone',attributes.ethnicities['White Alone'],'%')
        print('\t White Alone, not Hispanic or Latino',attributes.ethnicities['White Alone, not Hispanic or Latino'],'%')
        print('Income Data')
        print('\t Per Capita Income',attributes.income['Per Capita Income'],'%')
        print('\t Persons Below Poverty Level',attributes.income['Persons Below Poverty Level'],'%')
        print('\t Median Household Income',attributes.income['Median Household Income'],'%')

def operation_lines(commandline):
    global full_data
    try:
        with open(commandline) as file:
            for line in file:
                line = line.translate(str.maketrans({':':'|','.':'|'}))
                line_list = line.split('|')
                line_list = [item.strip() for item in line_list]
                print(line_list)
                if line_list[0] == 'filter-state':
                    line_list[1].upper()
                    state_filtered_list = hw3.filter_by_state(full_data,line_list[1])
                    full_data = state_filtered_list
                elif line_list[0] == 'display':
                    print_demo(full_data)
                elif line_list[0] == 'filter-gt':
                    full_data = operations_seconds_element(line_list)
                elif line_list[0] == 'filter-lt':
                    full_data = operations_seconds_element(line_list)
                elif line_list[0] == 'population-total':
                    print('2014 Population:',hw3.population_total(full_data))
                elif line_list[0] == 'population':
                    print('2014',line_list[1],line_list[2],":",operations_seconds_element(line_list))
                elif line_list[0] == 'percent':
                    full_data = operations_seconds_element(line_list)
                else:
                    print('Line ',line,'in',commandline,'has no valid argument')
                    continue
    except FileNotFoundError:
        print('Error, file not found!')
operation_lines('inputs/bachelors_gt_60.ops')

