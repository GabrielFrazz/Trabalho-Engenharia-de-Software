import gspread 
from app.engine.forms import Feedback
from oauth2client.service_account import ServiceAccountCredentials

def update_forms():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\luanm\\Documents\\A_TES\\Trabalho-Engenharia-de-Software\\app\\engine\\fomulario-satisfacao.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Avaliação de Desempenho do Vendedor (respostas)").sheet1
    data = sheet.get_all_records()
    V = []
    i = 1
    temp = Feedback()
    for record in data:
        temp.create_feedback(i,record.get('Nome:'),record.get('Carimbo de data/hora'),record.get('Feedback:'))
        V.append(temp)
        i = i+1
    return V
        


