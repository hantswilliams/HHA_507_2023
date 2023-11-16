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

## load in the model
loaded_model = pickle.load(open('model/xgboost_100k.sav', 'rb'))
## load in the scaler
loaded_scaler = pickle.load(open('model/scaler_100k.sav', 'rb'))

print('mapping_area_list:', mapping_area_list)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ## if request is post, then get the values from the form
    if request.method == 'POST':
        print('request.form:', request.form)

        date_occ = request.form['date_occ']
        time_occ = request.form['time_occ']
        area_name = request.form['area_name']
        rpt_dist_no = request.form['rpt_dist_no']
        crm_cd_desc = request.form['crm_cd_desc']
        vict_age = request.form['vict_age']
        vict_descent = request.form['vict_descent']
        premis_desc = request.form['premis_desc']
        weapon_desc = request.form['weapon_desc']

        print('date_occ:', date_occ)
        print('time_occ:', time_occ)
        print('area_name:', area_name)
        print('rpt_dist_no:', rpt_dist_no)
        print('crm_cd_desc:', crm_cd_desc)
        print('vict_age:', vict_age)
        print('vict_descent:', vict_descent)
        print('premis_desc:', premis_desc)
        print('weapon_desc:', weapon_desc)

        ## based on the values, get the ordinal encoding
        date_occ = mapping_date[mapping_date['date_occ'] == date_occ]['date_occ_ordinal'].values[0]
        print('date_occ:', date_occ)

        area_name = mapping_area[mapping_area['area_name'] == area_name]['area_name_ordinal'].values[0]
        print('area_name:', area_name)

        crm_cd_desc = mapping_crm[mapping_crm['crm_cd_desc'] == crm_cd_desc]['crm_cd_desc_ordinal'].values[0]
        print('crm_cd_desc:', crm_cd_desc)

        vict_descent = maping_descent[maping_descent['vict_descent_desc'] == vict_descent]['vict_descent_ordinal'].values[0]
        print('vict_descent:', vict_descent)

        premis_desc = mapping_premis[mapping_premis['premis_desc'] == premis_desc]['premis_desc_ordinal'].values[0]
        print('premis_desc:', premis_desc)

        weapon_desc = mapping_weapon[mapping_weapon['weapon_desc'] == weapon_desc]['weapon_desc_ordinal'].values[0]
        print('weapon_desc:', weapon_desc)

        ## create a dataframe with the values
        df = pd.DataFrame({
            'date_occ': [date_occ],
            'time_occ': [time_occ],
            'area_name': [area_name],
            'rpt_dist_no': [rpt_dist_no],
            'crm_cd_desc': [crm_cd_desc],
            'vict_age': [vict_age],
            'vict_descent': [vict_descent],
            'premis_desc': [premis_desc],
            'weapon_desc': [weapon_desc],
        })

        print('df:', df)

        ## scale the values
        df_scaled = loaded_scaler.transform(df)
        print('df_scaled:', df_scaled)

        ## make the prediction
        prediction = loaded_model.predict(df_scaled)
        print('ML PREDICTION: ', prediction[0])

        ## map the prediction to a string
        if prediction[0] == 0:
            prediction = 'Female'
        else:
            prediction = 'Male'

        ## return the prediction
        return render_template(
            'index.html',
            prediction=prediction,
            area_list=mapping_area_list,
            crm_list=mapping_crm_list,
            date_list=mapping_date_list,
            descent_list=mapping_descent_list,
            premis_list=mapping_premis_list,
            sex_list=mapping_sex_list,
            weapon_list=mapping_weapon_list,
        )

    else:
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