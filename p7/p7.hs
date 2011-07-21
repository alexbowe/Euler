sieve :: [Integer] -> [Integer]
sieve xs = head xs : sieve [x | x <- xs, rem x (head xs) /= 0]

primes = sieve [2..]

--take 10 primes
