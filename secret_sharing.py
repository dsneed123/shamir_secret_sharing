"""
Author: Davis Sneed
Class: Cyber Security
Description: This is a basic implmentation of a shmair secret sharing scheme
Date: 19 Feburary 2024
Last Modified: 18 November 2024
------------------------------------------------
Note: this only seems to work with small amounts of shares and a small threshold.
I am having trouble expanding this to work for larger variables.
"""
import random
import argparse

FIELD_SIZE = 10**5

# Generate a random secret and return it
def generate_secret():
    return random.randrange(1, FIELD_SIZE)

# Reconstruct the secret with the shares and return it
def reconstruct_secret(shares, threshold):
    secret = 0 #create a accumulator variable. Secret = 0
    for i in range(threshold):
        term = shares[i][1] #create a term varable set to i in the list and the first element in the tuple
        #use the lagrange interpolation formula
        for j in range(threshold):
            if i != j: #prevent division by 0
                term *= -shares[j][0] / (shares[i][0] - shares[j][0]) 
        secret += term #add each term to the secret
        
    reconstructed_secret = int(secret) % FIELD_SIZE #Turn the secret into a int and mod by the field size
    return reconstructed_secret 

# Create coefficients and return them
def create_coefficients(num_shares, secret):
    coefficients = [secret]  # Set coefficient[0] = secret

    # Create coefficients and append to an array
    for _ in range(1, num_shares):
        coefficients.append(random.randrange(1, FIELD_SIZE)) #append random coefficients to array

   #print("Coefficients: ", coefficients)  # Print for test purposes
    return coefficients  # Return the coefficient array

# Split the secret into N shares and return the shares
def generate_shares(num_shares, threshold, secret):
		#generate the random coefficeints for the line
    coefficients = create_coefficients(threshold, secret)  # Use threshold as the degree of the polynomial
    shares = [] #empty list of shares
		
		#iterate through the list of coefficeints
    for i in range(1, num_shares + 1):
        share = sum(c * (i ** j) % FIELD_SIZE for j, c in enumerate(coefficients)) % FIELD_SIZE #calculate a point
        shares.append((i, share)) #append the tuple to the list of shares

    return shares

def main():
    parser = argparse.ArgumentParser(description="Secret Sharing Script")
    parser.add_argument("num_shares", type=int, help="Number of shares to generate")
    parser.add_argument("threshold", type=int, help="Threshold number of shares needed to reconstruct the secret")
    args = parser.parse_args()

    num_shares = args.num_shares
    threshold = args.threshold
    secret = generate_secret()  # Generate a random secret
    print("Original secret: ", secret)

    shares = generate_shares(num_shares, threshold, secret)
    print("Generated shares:", shares)

    # Uncomment the following lines when the reconstruct_secret function is implemented
    # reconstructed_secret = reconstruct_secret(shares, threshold)
    # print("Reconstructed secret:", reconstructed_secret)


if __name__ == "__main__":
    main() 
