import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_dist(results):
    values = list(results.values())  
    labels = list(results.keys())    
    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots()
    bins = np.histogram_bin_edges(values, bins='auto')

    ax.set_xlim(0,max(values))
    ax.set_ylim(0, 700) 
    ax.set_xlabel('simulated PDs')

    n, bins, patches = ax.hist([], bins=bins, color='#b51307', edgecolor='white', alpha=0.7)
    title = ax.set_title(f"Running Simulation No. : {labels[0]}")

    def update(frame):
        current_data = values[:frame]
        n, _ = np.histogram(current_data, bins)

        for rect, height in zip(patches, n):
            rect.set_height(height)

        title.set_text(f"Running Simulation No. : {labels[frame - 1]}")

        return list(patches) + [title] 

    ani = animation.FuncAnimation(fig, update, frames=np.arange(1, len(values) + 1),
                                  repeat=False, interval=1, blit=False) 

    # ani.save('simulation_animation.html', writer='html', fps=30)
    # ani.save('Monte_carlo_practice.gif', writer='imagemagick', fps=1)
    plt.show()




