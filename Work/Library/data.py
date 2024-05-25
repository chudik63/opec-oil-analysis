import pandas as pd
import numpy as np

countries = dates = daily_production = pd.DataFrame()

def read_data(databases_paths):
    global countries, dates, daily_production
    countries = pd.read_excel(databases_paths['countries'])
    dates = pd.read_excel(databases_paths['dates'])
    daily_production = pd.read_excel(databases_paths['daily_production'])

def collect_to_main(path):
    main = pd.merge(daily_production, dates, on='date_id')
    main = pd.merge(main, countries, on='country_id')
    main.to_excel(path, index=False)



