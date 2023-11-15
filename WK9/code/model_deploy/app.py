import pandas as pd 
import pickle
from flask import Flask, render_template, request

## load in values for ordinal encoding
mapping_area = pd.read_csv('data/mapping_area.csv')
mapping_crm = pd.read_csv('data/mapping_crm.csv')
mapping_date = pd.read_csv('data/mapping_date.csv')
maping_descent = pd.read_csv('data/mapping_descent.csv')
mapping_premis = pd.read_csv('data/mapping_premis.csv')
mapping_sex = pd.read_csv('data/mapping_sex.csv')
mapping_weapon = pd.read_csv('data/mapping_weapon.csv')

mapping_area_list = mapping_area['area_name'].tolist()
mapping_crm_list = mapping_crm['crm_cd_desc'].tolist()
mapping_date_list = mapping_date['date_occ'].tolist()
mapping_descent_list = maping_descent['vict_descent_desc'].tolist()
mapping_premis_list = mapping_premis['premis_desc'].tolist()
mapping_sex_list = mapping_sex['vict_sex'].tolist()
mapping_weapon_list = mapping_weapon['weapon_desc'].tolist()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
        area_list=mapping_area_list,
        crm_list=mapping_crm_list,
        date_list=mapping_date_list,
        descent_list=mapping_descent_list,
        premis_list=mapping_premis_list,
        sex_list=mapping_sex_list,
        weapon_list=mapping_weapon_list,
    )
        

if __name__ == '__main__':
    app.run(
        debug=True, 
        port=5000)