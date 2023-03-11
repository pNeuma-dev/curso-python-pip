import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], keys, values)

  keys, values = utils.population_by_world(data)
  charts.generate_pie_chart(keys, values)


if __name__ == '__main__':
  run()
