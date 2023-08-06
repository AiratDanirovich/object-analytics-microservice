import matplotlib.pyplot as plt
import mpld3
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px


# создание matplot графика + сохранение в html и jpg
def matplot_graph(table_list):
    # много параметров по оси x - лучше выставить размер побольше
    fig = plt.figure(figsize=(50, 10))
    ax = fig.add_subplot()
    ax.bar(table_list[1::3], table_list[2::3])
    plt.xticks(rotation=90)
    plt.title("Дебиты для объектов")
    plt.xlabel("Объект")
    plt.ylabel("Дебит объекта")

    plt.savefig('../output_data/debit_object_graph.jpg')
    mpld3.save_html(fig, '../output_data/debit_object_graph.html')


# график plotly
def plotly_graph(table_list):
    pio.renderers.default = "browser"

    # столбчатая даиграмма
    # fig = go.Figure(
    #    data=[go.Bar(x=table_list[1::3], y=table_list[2::3])],
    #    layout_title_text="Object and debit diagram"
    # )

    # точечный график
    fig = px.scatter(x=table_list[1::3], y=table_list[2::3])

    # подписи для осей
    fig.update_layout(
        xaxis_title=dict(text='Object name', font=dict(size=16, color='#000000')),
        yaxis_title=dict(text='Debit size', font=dict(size=16, color='#000000')),
    )

    fig.show()
