import Data.List
import qualified Math.NumberTheory.Primes.Sieve as PS

mod3or5 :: Integer -> Integer
mod3or5 x = if mod x 3 == 0 || mod x 5 == 0
            then x
            else 0

prob1 :: Integer
prob1 = sum (map mod3or5 [0..999])

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

evenFibsUnder :: Integer -> [Integer] -> [Integer]
evenFibsUnder x fibs = [y | y <- fibs, even y, y <= x]

prob2 :: Integer
prob2 = sum $ evenFibsUnder 4000000 $ take 1000 fibs

prob3' :: Integer -> Integer -> [Integer]
prob3' 1 _ = []
prob3' x n = if x `mod` n == 0
             then n : prob3' (x `div` n) n
             else prob3' x (n + 1)

prob3 :: Integer
prob3 = maximum $ prob3' 600851475143 2

isPalindrome :: Show a => a -> Bool
isPalindrome x = (show x) == (reverse $ show x)

prob4 :: Integer
prob4 = maximum [z | x <- [100..999], y <- [x..999], let z = x * y, isPalindrome z]

prob5 :: Integer
prob5 = foldl1 lcm [1..20]

square :: Integer -> Integer
square = (^ 2)

prob6 :: Integer
prob6 = (square $ sum [1..100]) - (sum $ map square [1..100])

some_remainder :: Integer -> Integer -> Bool
some_remainder x y = (y `mod` x) /= 0

primes :: [Integer] -> [Integer]
primes (x:xs) = x : primes (filter (some_remainder x) xs)

prob7 :: Integer
prob7 = primes [2..] !! 10000

hypot a b = sqrt $ a * a + b * b

tripletSum a b = a + b + hypot a b

prob9 = head [a * b * hypot a b | a <- [1..1000], b <- [1..a], tripletSum a b == 1000]

prob10 = sum $ takeWhile (< 2 * 10 ^ 6) PS.primes
