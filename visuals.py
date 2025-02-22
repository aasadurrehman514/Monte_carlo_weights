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
                                  repeat=False, interval=1, blit=False)  # Use blit=False for compatibility

    # ani.save('simulation_animation.html', writer='html', fps=30)
    # ani.save('Monte_carlo_practice.gif', writer='imagemagick', fps=1)
    plt.show()







    # # Use a style for a prettier plot
    # print(plt.style.available)
    # plt.style.use('dark_background')  # Choose from styles like 'ggplot', 'seaborn', etc.

    # # Plot the histogram with automatic bins and transparency
    # plt.hist(values, bins='auto', color='#1f77b4', edgecolor='black', alpha=0.7)

    # # Add labels and title with enhanced styling
    # plt.xlabel('Value', fontsize=14, fontweight='bold', color='darkblue')
    # plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='darkblue')
    # plt.title('Histogram of Dictionary Values', fontsize=16, fontweight='bold', color='darkblue')

    # # Add gridlines for easier readability
    # plt.grid(True, linestyle='--', alpha=0.5)

    # # Show the plot
    # plt.show()


    # # Show the plot
    # plt.show()
