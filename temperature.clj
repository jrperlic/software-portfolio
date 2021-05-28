; Here's my project. It's a program that converts the temperature
; from Fahrenheit to Celsius and vice versa. Going into this, I did
; not know how to do rounding in Clojure, so I spent a good chunk of
; time learning that.

; This week, I focused on learning how to perform tests in Clojure.
; So I Googled how to do it, and after some initial frustration, this
; is what I had at the end of 3 hours:

(ns testing)

(defn celsius-to-fahrenheit [C]
  (display (+ (* C 9/5) 32)))

(defn fahrenheit-to-celsius [F]
  (display (* (- F 32) 5/9)))

(defn display [n]
  (int (Math/round (float n))))

(deftest test-celsius-to-fahrenheit
  (is (= 32 (celsius-to-fahrenheit 0)))
  (is (= 212 (celsius-to-fahrenheit 100))))

(deftest test-fahrenheit-to-celsius
  (is (= 0 (fahrenheit-to-celsius 32)))
  (is (= 100 (fahrenheit-to-celsius 212))))

(run-tests)