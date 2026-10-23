
1. Primes, Divisors, & Factorization

Finding factors and determining primality efficiently form the baseline of mathematical algorithms.
• Primality Testing: Checking if a number N is prime can be done naively in O(N), but optimizing it to iterate only up to \(\sqrt{N}\) achieves an \(O(\sqrt{N})\) time complexity.
• Sieve of Eratosthenes: Used to find all prime numbers up to a given limit N. By crossing out multiples of primes, it operates in \(O(N \log \log N)\) time, which is vastly superior to checking every number individually.
• Prime Factorization: Decomposing a number into a product of primes. A Sieve can be modified to store the Smallest Prime Factor (SPF) or Lowest Prime Factor (LPF) for each index. This precomputation reduces the time to factorize any number down to \(O(\log N)\).

2. GCD, LCM, & The Euclidean Algorithm

Greatest Common Divisors (GCD) are fundamental when solving problems regarding fractions, distributions, or periodic alignments.
• Euclidean Algorithm: Rather than searching for all common factors, the Euclidean algorithm utilizes the property \(\gcd(a, b) = \gcd(b, a \pmod b)\). It computes the GCD recursively in logarithmic time \(O(\log(\min(a, b)))\).
• Extended Euclidean Algorithm: Extends the standard algorithm to solve equations of the form \(ax + by = \gcd(a, b)\), extracting the integer coefficients x and y.
• Linear Diophantine Equations: Integer equations written as ax + by = c. They are solvable if and only if \(\gcd(a, b)\) perfectly divides c. The Extended Euclidean Algorithm is used to derive these solutions.

3. Modular Arithmetic & Fast Exponentiation

When answers to coding challenges grow exceptionally large, platforms require calculating results modulo a prime (typically 10⁹ + 7).
• Basic Rules:
	• \((a + b) \pmod m = ((a \pmod m) + (b \pmod m)) \pmod m\)
	• \((a \times b) \pmod m = ((a \pmod m) \times (b \pmod m)) \pmod m\)
• Binary Exponentiation (Fast Power): Computes \((a^b) \pmod m\) in \(O(\log b)\) instead of a linear loop. It breaks the power down using binary representation (e.g., a¹³ = a⁸ × a⁴ × a¹).
• Modular Multiplicative Inverse: Division is not directly defined in modular arithmetic. To calculate \((a / b) \pmod m\), you compute \((a \times b^{-1}) \pmod m\).
	• Fermat's Little Theorem: If m is prime, \(b^{-1} \equiv b^{m-2} \pmod m\). It is easily calculated via binary exponentiation.
	• Extended Euclidean Method: If m is composite but \(\gcd(b, m) = 1\), the inverse can be extracted via bx + my = 1.  