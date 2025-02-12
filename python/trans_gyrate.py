import argparse
import matplotlib.pyplot as plt
import numpy as np

def plot_radius_of_gyration(input_file, output_file):
    """
    Plots Radius of Gyration (Rg) vs. Time from GROMACS gyrate output.
    """
    # Load Rg data (ignoring comments starting with '#' or '@')
    data = np.loadtxt(input_file, comments=["#", "@"])

    # Extract time and Rg values
    time_values = data[:, 0]
    rg_values = data[:, 1]

    # Create figure
    fig, ax0 = plt.subplots(1, 1)

    # Plot Rg vs. Time
    ax0.plot(time_values, rg_values, linewidth=1.5, color="orange", label="Radius of Gyration (Rg)")

    # Set axis labels
    ax0.set_xlabel("Time (ps)")
    ax0.set_ylabel("Radius of Gyration (nm)")

    # Add legend
    ax0.legend(loc="upper right")

    # Optimize layout
    fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

    # Save figure with high resolution
    plt.savefig(output_file, format="png", bbox_inches="tight", dpi=800)

    print(f"Plot saved as {output_file}")

if __name__ == '__main__':
    # Argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="Use this tool to generate Radius of Gyration (Rg) vs. Time plots.")
    parser.add_argument('-f', '--input', type=str, required=True, help='Input filename (Rg .xvg file).')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output filename (PNG file).')

    # Parse arguments
    args = parser.parse_args()

    # Run the Rg plot function with parsed arguments
    plot_radius_of_gyration(args.input, args.output)