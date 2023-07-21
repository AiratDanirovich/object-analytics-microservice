import matplotlib.pyplot as plt
import mpld3

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