"""
Author: Davis Sneed
Class: Cyber Security
Description: This is a basic implementation of a Shamir secret sharing scheme
Date: 19 February 2024
Last Modified: 18 November 2024
------------------------------------------------
"""
import random
import argparse
import matplotlib.pyplot as plt
import numpy as np

FIELD_SIZE = 10**5

# Generate a random secret and return it
def generate_secret():
    return random.randrange(1, FIELD_SIZE)

# Reconstruct the secret with the shares and return it
def reconstruct_secret(shares, threshold):
    secret = 0  # Create an accumulator variable. Secret = 0
    for i in range(threshold):
        term = shares[i][1]  # Create a term variable set to i in the list and the first element in the tuple
        # Use the Lagrange interpolation formula
        for j in range(threshold):
            if i != j:  # Prevent division by 0
                term *= (0 - shares[j][0]) * pow(shares[i][0] - shares[j][0], -1, FIELD_SIZE)
                term %= FIELD_SIZE
        secret += term
        secret %= FIELD_SIZE
    return secret

# Create coefficients and return them
def create_coefficients(threshold, secret):
    coefficients = [secret]  # Set coefficient[0] = secret

    # Create coefficients and append to an array
    for _ in range(1, threshold):
        coefficients.append(random.randrange(1, FIELD_SIZE))  # Append random coefficients to array

    return coefficients  # Return the coefficient array

# Split the secret into N shares and return the shares
def generate_shares(num_shares, coefficients):
    shares = []  # Empty list of shares

    # Iterate through the list of coefficients
    for i in range(1, num_shares + 1):
        share = sum(c * (i ** j) % FIELD_SIZE for j, c in enumerate(coefficients)) % FIELD_SIZE  # Calculate a point
        shares.append((i, share))  # Append the tuple to the list of shares

    return shares

def plot_shares(shares, coefficients):
    x, y = zip(*shares)
    plt.scatter(x, y, label='Shares', color='red')

    # Generate points for the polynomial curve
    x_curve = np.linspace(1, max(x), 100)
    y_curve = [sum(c * (xi ** j) % FIELD_SIZE for j, c in enumerate(coefficients)) % FIELD_SIZE for xi in x_curve]

    plt.plot(x_curve, y_curve, label='Polynomial Curve', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Secret Shares and Polynomial Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Secret Sharing Script")
    parser.add_argument("num_shares", type=int, help="Number of shares to generate")
    parser.add_argument("threshold", type=int, help="Threshold number of shares needed to reconstruct the secret")
    parser.add_argument("-g", "--graph", action="store_true", help="Output a graph of the shares")
    args = parser.parse_args()

    num_shares = args.num_shares
    threshold = args.threshold
    secret = generate_secret()  # Generate a random secret
    print("Original secret: ", secret)

    coefficients = create_coefficients(threshold, secret)
    shares = generate_shares(num_shares, coefficients)
    print("Generated shares:", shares)

    if args.graph:
        plot_shares(shares, coefficients)

    # Uncomment the following lines when the reconstruct_secret function is implemented
    # reconstructed_secret = reconstruct_secret(shares, threshold)
    # print("Reconstructed secret:", reconstructed_secret)

if __name__ == "__main__":
    main()

# Example usage:
# python secret_sharing.py 5 3 -g
# This will generate 5 shares with a threshold of 3 to reconstruct the secret and output a graph of the shares and polynomial curve.