mod3or5 x = if mod x 3 == 0 || mod x 5 == 0
            then x
            else 0

prob1 = sum (map mod3or5 [0..999])
