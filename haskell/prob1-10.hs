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

prob5 = foldl1 lcm [1..20]
