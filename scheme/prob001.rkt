#lang racket

; 
; If we list all the natural numbers below 10 that are multiples 
; of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
; 
; Find the sum of all the multiples of 3 or 5 below 1000.
; 

(define prob1
  (lambda (limit)
    (cond ((< limit 1) 0)
          (else
           (+ 
            (cond ((or (= (modulo limit 3) 0) (= (modulo limit 5) 0)) 
                   limit)
                  (else 0))
            (prob1 (- limit 1)))))))