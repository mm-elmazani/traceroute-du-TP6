import argparse
import subprocess
import re
import os
import platform

def validate_target(target):
    """Validate if the target is a valid IP or domain."""
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    domain_pattern = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$")
    if ip_pattern.match(target) or domain_pattern.match(target):
        return True
    raise ValueError(f"Invalid target: {target}. Must be a valid IP or domain.")

def run_traceroute(target, progressive, output_file):
    """Run the traceroute command and handle output."""
    # Determine the correct command based on the operating system
    command = "tracert" if platform.system().lower() == "windows" else "traceroute"

    try:
        # Run traceroute using subprocess.Popen
        process = subprocess.Popen(
            [command, target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        results = []

        # Read output progressively
        for line in process.stdout:
            line = line.strip()
            if progressive:
                print(line)
            results.append(line)

        # Wait for the process to complete
        process.wait()

        # Handle errors
        if process.returncode != 0:
            error_output = process.stderr.read().strip()
            raise RuntimeError(f"Traceroute failed: {error_output}")

        # Write results to output file if specified
        if output_file:
            with open(output_file, "w") as f:
                f.write("\n".join(results))
            print(f"Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The '{command}' command is not available on your system.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argparse for command-line interface
    parser = argparse.ArgumentParser(description="Python Traceroute Script")
    parser.add_argument("target", type=str, help="Target URL or IP address for the traceroute.")
    parser.add_argument(
        "-p", "--progressive",
        action="store_true",
        help="Display traceroute results progressively."
    )
    parser.add_argument(
        "-o", "--output-file",
        type=str,
        help="File to save the traceroute results."
    )

    # Parse arguments
    args = parser.parse_args()

    # Validate target
    try:
        validate_target(args.target)
    except ValueError as e:
        print(e)
        return

    # Run traceroute
    run_traceroute(args.target, args.progressive, args.output_file)

if __name__ == "__main__":
    main()
