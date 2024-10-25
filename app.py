import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Interactive Histogram App")

with ui.sidebar():
    ui.input_slider("selected_number_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram showing random data distribution")
def histogram():
    count_of_points: int = 437
    np.random.seed(3)
    x = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(x, input.selected_number_bins(), density=True)
    plt.title("My Example")  

