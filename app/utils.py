from functools import reduce


def get_population(country_dic):
  #Esto se puede solucionar con expresiones regulares
  population_dic = {
    '2022': int(country_dic['2022 Population']),
    '2020': int(country_dic['2020 Population']),
    '2015': int(country_dic['2015 Population']),
    '2010': int(country_dic['2010 Population']),
    '2000': int(country_dic['2000 Population']),
    '1990': int(country_dic['1990 Population']),
    '1980': int(country_dic['1980 Population'])
  }
  labels = population_dic.keys()
  values = population_dic.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result


def population_by_world(data):
  country = []
  population_percentaje = []
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  for row in data:
    country.append(row['Country/Territory'])
    population_percentaje.append(float(row['World Population Percentage']))
  return country, population_percentaje
