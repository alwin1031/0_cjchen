import argparse
import matplotlib.pyplot as plt
import numpy as np

def plot_temperature(input_file, output_file):
    """
    Plots Temperature vs. Time from GROMACS energy file.
    """
    # Load temperature data (ignoring comments starting with '#' or '@')
    data = np.loadtxt(input_file, comments=["#", "@"])

    # Extract time and temperature values
    time_values = data[:, 0]
    temp_values = data[:, 1]

    # Create figure
    fig, ax0 = plt.subplots(1, 1)

    # Plot Temperature vs. Time
    ax0.plot(time_values, temp_values, linewidth=1.5, color="r", label="Temperature")

    # Set axis labels
    ax0.set_xlabel("Time (ps)")
    ax0.set_ylabel("Temperature (K)")

    # Add legend
    ax0.legend(loc="upper right")

    # Optimize layout
    fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

    # Save figure with high resolution
    plt.savefig(output_file, format="png", bbox_inches="tight", dpi=800)

    print(f"Plot saved as {output_file}")

if __name__ == '__main__':
    # Argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="Use this tool to generate Temperature vs. Time plots.")
    parser.add_argument('-f', '--input', type=str, required=True, help='Input filename (Temperature .xvg file).')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output filename (PNG file).')

    # Parse arguments
    args = parser.parse_args()

    # Run the temperature plot function with parsed arguments
    plot_temperature(args.input, args.output)