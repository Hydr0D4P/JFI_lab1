## Task 1
def jains(throughput1, throughput2):
    """Write a function named jains that takes two throughput values (int and/or float) as arguments and
    returns a JFI."""

    # Calculate the numerator of the Jain's fairness index
    numerator = (throughput1 + throughput2) ** 2

    # Calculate the denominator of the Jain's fairness index
    denominator = 2 * (throughput1 ** 2 + throughput2 ** 2)

    # Check for divide-by-zero errors and return the result
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

## Task 2

def jainsall(throughputs):
    """Write a new function jainsall function that takes a list of throughput values (integers and/or float)
    and returns a JFI."""
    # Calculate the numerator of the Jain's fairness index
    numerator = sum(throughputs) ** 2

    # Calculate the denominator of the Jain's fairness index
    denominator = len(throughputs) * sum(x ** 2 for x in throughputs)

    # Check for divide-by-zero errors and return the result
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

throughputs = [10, 20]
jfi = jainsall(throughputs)
print(jfi) # Output: 0.9

# Task 3
def jainsallfromtxt(textfile):
    """Read the throughput values from a file and then use your jainsall function to calculate a JFI."""

    with open(textfile, 'r') as file:
        # Read lines from file and extract numeric values
        throughputs = [float(line.split()[0]) for line in file]

    # Calculate Jain's fairness index for the throughput values
    jfi = jainsall(throughputs)
    return jfi

jfi = jainsallfromtxt('JFI.txt')
print(f"3: JFI: {jfi}") # Output: 0.7552

# Task 4
def openandparse(textfile):
    """Read the throughput values from a file and then use your jainsall function to calculate a JFI. Note:
    you must use the same units."""

    # Opens the file
    with open(textfile, 'r') as f:
        # Reads the content
        content = f.readlines()

    # Parses the values and converts them to Mbps
    throughputs = []
    for line in content:
        value, unit = line.split()
        value = int(value)
        if unit == "Mbps":
            throughput_mbps = value
        elif unit == "Kbps":
            throughput_mbps = value / 1000
        else:
            print("value error, unknown unit")
            continue
        #add corrected value to throughputs
        throughputs.append(throughput_mbps)
    return throughputs # [7, 1.2, 15, 32]

throughputs = openandparse('JFI2.txt')
jfi_mbps = jainsall(throughputs)
print(f"4: JFI: {jfi_mbps}") # Output: 0.5862