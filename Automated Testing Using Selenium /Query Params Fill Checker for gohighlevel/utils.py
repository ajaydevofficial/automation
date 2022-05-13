import pandas as pd
import json

def read_csv_to_json(filepath):

    #Function reads csv file and returns corresponding json value
    csv = pd.read_csv(filepath)
    data = csv.to_json(orient='records')
    return json.loads(data)