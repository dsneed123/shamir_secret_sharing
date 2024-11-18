# Shamir Secret Sharing Scheme Implementation

This is a basic implementation of a Shamir Secret Sharing scheme.

## Author

Davis Sneed

## Class

Cyber Security

## Description

This script implements a basic Shamir Secret Sharing scheme, which allows a secret to be divided into multiple "shares". A threshold number of shares is required to reconstruct the original secret. This is a widely used cryptographic method for securely sharing secrets among multiple parties.

## Date

- Created: 19 February 2024
- Last Modified: 18 November 2024

## Usage

To use this script, you need to have Python installed. You can then run the script with the following command:

```bash
python script_name.py num_shares threshold
```

### Parameters:
- `num_shares`: The total number of shares to generate.
- `threshold`: The minimum number of shares required to reconstruct the secret.

For example, if you want to create 5 shares, with a threshold of 3 (meaning any 3 shares can be used to reconstruct the secret), you would run:

```bash
python script_name.py 5 3
```

## Requirements

- Python 3.x or higher
- Required Python libraries (if any) are listed below:

  ```bash
  pip install <library_name>
  ```

## How It Works

The script uses the Shamir Secret Sharing algorithm to divide a secret into multiple shares. Each share is represented as a point in a polynomial, and the threshold defines the minimum number of shares required to solve for the original secret.

1. The secret is turned into a polynomial with random coefficients.
2. The polynomial is evaluated at different points to generate shares.
3. A subset of shares, equal to or greater than the threshold, can be used to reconstruct the original secret.

## Example

1. You can create shares by running the script with a desired number of shares and a threshold.
2. You can later combine the shares using Lagrange interpolation to recover the original secret.


## Acknowledgments

- Shamir's Secret Sharing is a cryptographic algorithm developed by Adi Shamir in 1979.
