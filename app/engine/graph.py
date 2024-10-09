import plotly.graph_objects as go
from app import app, db
from app.models import Sale
from sqlalchemy import extract  # Import necessário para filtrar por mês

# Criar um bloco de contexto da aplicação
def cria_grafico():
    with app.app_context():
        # Filtrando as vendas de cada mês
        jan = db.session.query(Sale).filter(extract('month', Sale.date) == 1).count()
        fev = db.session.query(Sale).filter(extract('month', Sale.date) == 2).count()
        mar = db.session.query(Sale).filter(extract('month', Sale.date) == 3).count()
        abr = db.session.query(Sale).filter(extract('month', Sale.date) == 4).count()
        mai = db.session.query(Sale).filter(extract('month', Sale.date) == 5).count()
        jun = db.session.query(Sale).filter(extract('month', Sale.date) == 6).count()
        jul = db.session.query(Sale).filter(extract('month', Sale.date) == 7).count()
        ago = db.session.query(Sale).filter(extract('month', Sale.date) == 8).count()
        setm = db.session.query(Sale).filter(extract('month', Sale.date) == 9).count()
        out = db.session.query(Sale).filter(extract('month', Sale.date) == 10).count()
        nov = db.session.query(Sale).filter(extract('month', Sale.date) == 11).count()
        dez = db.session.query(Sale).filter(extract('month', Sale.date) == 12).count()

        # Definindo os nomes dos meses e as vendas
        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        sales = [jan, fev, mar, abr, mai, jun, jul, ago, setm, out, nov, dez]

        # Criando o gráfico com Plotly
        grafLin = go.Figure()
        grafLin.add_trace(go.Scatter(x=meses, y=sales, mode='lines+markers', name='Grupo 1', line=dict(color='blue', width=2)))

        # Configurando o layout do gráfico
        grafLin.update_layout(
            title='Gráfico de Linhas - Vendas por Mês',
            xaxis_title='Meses',
            yaxis_title='Vendas',
        )

        # Exibindo o gráfico
        grafLin.show()
