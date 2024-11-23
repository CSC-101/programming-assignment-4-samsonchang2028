import build_data
import data
from data import CountyDemographics
full_data = build_data.get_data()

'This function takes a list of values of type data.CountyDemographics and adds each element '
'of the county attribute into the result variable from 2014. It counts the population of the given list from 2014'
#part 1
def population_total(values:list[data.CountyDemographics])->int:
    total_population = 0
    for counties in range(len(values)): #iterates through the range of the length of values
        total_population = total_population + values[counties].population['2014 Population']
    return total_population
#part2
"returns a county's demographics into a list from matching it with it's states abbrev. It takes the list and iterates through it,"
" and if the state abbrevation is in the value of a key, it will return that whole county's demographics "
def filter_by_state(counties:list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:
    state_demographics = []
    for county in counties:
        if state in county.state:
            state_demographics.append(county)
    return state_demographics
#these functions take a list of data of type countydemographics and a string,and it checks if the specific key is in a county. if it is, it multiplies
# the percentage of the key value with the total 2014 population and returns the value after multiplied
#part3
def population_by_education(counties:list[data.CountyDemographics], degree:str) -> float:
    result = 0
    for county in counties:
        if degree in county.education:
            result =result + ((county.education[degree]/100)*county.population['2014 Population'])

    return round(result,3)
def population_by_ethnicity(counties:list[data.CountyDemographics], race:str) -> float:
    result = 0
    for county in counties:
        if race in county.ethnicities:
            result =result + ((county.ethnicities[race]/100) * county.population['2014 Population'])
    print(result)
    return result

def population_below_poverty_level(population:list[data.CountyDemographics]) -> float:
    result = 0
    for counties in population:
        result = result + ((counties.income['Persons Below Poverty Level']/100)*counties.population['2014 Population'])

    return round(result)

#These functions again take data types list and string. They take the number of people that have the specified key value and divides it to get it's decimal form then
# multiplies it by the total population to get its percentage. So the percentage represents how much of the total population has that specific key value.
#part4
def percent_by_education(counties:list[data.CountyDemographics],degree: str) -> float:
    result = population_by_education(counties,degree)
    return round((result/population_total(counties)*100),3)
def percent_by_ethnicity(counties:list[data.CountyDemographics], race:str) -> float:
    result = population_by_ethnicity(counties,race)
    return round((result / population_total(counties) * 100), 3)
def percent_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    result = population_below_poverty_level(counties)
    return round((result / population_total(counties) * 100), 3)
#These functions take a list of countydemographics, a string, and now a float. They filter counties wehre the percentage
#of people with a specified degree is greater than or equal to the given number
#part5
def education_greater_than(counties:list[data.CountyDemographics], degree:str, number:float) -> list[data.CountyDemographics]:
    education_percent_list= []
    for county in counties:
        percent = (((county.education[degree]/100)*county.population['2014 Population'])/county.population['2014 Population'])
        percent = percent * 100
        if percent >= number:
            education_percent_list.append(county)
    return education_percent_list
#Filters counties where the percentage of people with the specified degree is less than or equal to the given number.

def education_less_than(counties:list[data.CountyDemographics], degree:str, number:float) -> list[data.CountyDemographics]:
    education_percent_list= []
    for county in counties:
        percent = (((county.education[degree]/100)*county.population['2014 Population'])/county.population['2014 Population'])
        percent = percent * 100
        if percent <= number:
            education_percent_list.append(county)
    return education_percent_list
#THis function filters counties based on the percentage of a specific ethnicity in the population.
    # The function returns counties where the specified ethnicity makes up a percentage greater than or equal to the given threshold.
def ethnicity_greater_than(counties:list[data.CountyDemographics],race:str, number:float) -> list[data.CountyDemographics]:
    ethnicity_list= []
    for county in counties:
        percent = (((county.ethnicities[race]/100)*county.population['2014 Population'])/county.population['2014 Population'])
        percent = percent *100
        if percent >= number:
            ethnicity_list.append(county)
    return ethnicity_list
#This function filters counties based on the percentage of a specific ethnicity in the population.
    # The function returns counties where the specified ethnicity makes up a percentage less than or equal to the given threshold.

def ethnicity_less_than(counties:list[data.CountyDemographics],race:str, number:float) -> list[data.CountyDemographics]:
    ethnicity_list= []
    for county in counties:
        percent = (((county.ethnicities[race]/100)*county.population['2014 Population'])/county.population['2014 Population'])
        percent = percent *100
        if percent <= number:
            ethnicity_list.append(county)
    return ethnicity_list


#The functions below_poverty_level_greater_than and below_poverty_level_less_than filter a list of CountyDemographics objects
# based on the percentage of the population living below the poverty level. The greater_than function returns counties where this percentage is greater than or equal to a given threshold,
# while the less_than function returns counties where it is less than or equal to the num. The  percentage is calculated
# using the formula: (county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population'], and the result is compared to the number. if it is greater or less than, it will append it into poverty_list
def below_poverty_level_greater_than(counties:list[data.CountyDemographics], number:float) -> list[data.CountyDemographics]:
    poverty_list= []
    for county in counties:
        percent = (((county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']) / county.population[
            '2014 Population'])
        percent = percent * 100
        if percent >= number:
            poverty_list.append(county)
    return poverty_list
def below_poverty_level_less_than(counties:list[data.CountyDemographics], number:float) -> list[data.CountyDemographics]:
    poverty_list= []
    for county in counties:
        percent = (((county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']) / county.population[
            '2014 Population'])
        percent = percent * 100
        if percent <= number:
            poverty_list.append(county)
    return poverty_list
