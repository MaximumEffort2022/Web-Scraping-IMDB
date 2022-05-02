import seaborn as sns
import matplotlib.pyplot as plt
import base64 
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,5))
    plt.title('movie year with ratings')
    # plt.plot(x,y)
    fig, ax = plt.subplots(1, 1, figsize=(11, 3))
    _ = ax.plot(x,y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_2(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,5))
    plt.title('movie year with ratings')
    # plt.plot(x,y)
    fig, ax = plt.subplots(1, 1, figsize=(11, 6))
    _ = ax.scatter(x,y)
    plt.xticks()
    plt.tight_layout()
    graph2 = get_graph()
    return graph2