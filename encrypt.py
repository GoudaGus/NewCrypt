# pylint: disable-msg=invalid-name

"""Create crypto object and encrypt plain encoded text."""


from random import randint
from sys import exit


class Crypto_item:
    """Create random keys if no arguments are provided."""

    def __init__(self, p=0, q=0):
        """Initiate creation of keys."""
        def open_file_read(filename):
            """Read file."""
            try:
                with open(str(filename), "r") as open_file:
                    return open_file.read()
                open_file.close()
            except FileNotFoundError:
                return False

        # Assign to self
        self.p = p
        self.q = q

        # Import prime list.
        if open_file_read("mynewprimes.txt"):
            raw_file = str(self.open_file_read("mynewprimes.txt"))
            self.primes = [i.strip() for i in raw_file.split(",")]
        else:
            print("Error: mynewprimes.txt not found.")
            exit()

        # If primes are not assigned, assign using pre-complied list.
        if self.p == 0:
            self.p = self.get_prime()
            while self.p == self.q:
                self.p = self.get_prime()
        if self.q == 0:
            self.q = self.get_prime()
            while self.q == self.p:
                self.q = self.get_prime()

        self.keys = self.create_keys()

    # File opening manager

    def open_file_read(self, filename):
        """Read file."""
        try:
            with open(str(filename), "r") as open_file:
                return open_file.read()
            open_file.close()
        except FileNotFoundError:
            return False

    # Select random prime from list

    def get_prime(self):
        """Get list of primes from file made using sage."""
        return int(self.primes[randint(0, len(self.primes) - 1)])

    # Create crypto objects (keys)

    def create_keys(self):
        """Create key math."""
        def coprime(phi):
            while True:
                r = self.get_prime()
                if r != phi:
                    if 2 < r < phi:
                        break
            return r

        def mod_inv(a, m):
            """Get modInv."""
            def egcd(a, b):
                """Get GCD."""
                if a == 0:
                    return (b, 0, 1)
                g, y, x = egcd(b % a, a)
                return (g, x - (b//a) * y, y)

            __, x, _ = egcd(a, m)
            return x % m

        # Calculate internal variables
        p = self.p
        q = self.q

        n = p * q
        phi = (p - 1) * (q - 1)
        e = coprime(phi)
        d = mod_inv(e, phi)

        return e, n, d


def encrypt(m):
    """Encrypt encoded plaintext."""
    # Get keys
    primary_crypto = Crypto_item()
    e, n, d = primary_crypto.keys

    # Encrypt with public key
    cipher = pow(m, e, n)

    return f"{cipher},{d},{n}"


def decrypt(ck):
    """Decrypt ciphertext into encoded plaintext."""
    # Separate tuples
    cipher, priv_k = ck
    d, n = priv_k

    # Decrypt ciphertext
    plain = pow(cipher, d, n)

    return plain


if __name__ == "__main__":
    print("Please use via UI.py")
