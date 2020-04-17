#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

1.  I believe this code runs in `O(n^3)`. Even though `a` is increasing by `n * n` each iteration, the condition of the loop `while a < n * * n` should dominate as `n` increases.

2.  I believe this code runs in `O(n * log(n))`. The outer loop contributes a factor of `n`, because its counter increases by a constant `1` with each repetition. The inner loop contributes `log(n)` because, rather its counter is multiplied by `2` with each repetition: so it's `log_2(n)`.

3.  I believe this code runs in `O(n)`, where `n = bunnies`. The function `bunnyEars` only calls itself one or zero times per call, so it doesn't exponentially explode.

## Exercise II

I would perform a binary search of the floors. Starting with floor `f(0) = n`, I'd drop the egg. If it doesn't break, then the highest floor where the egg doesn't break is `n`, because nothing higher is possible. If the eggs does break, then I'd check floor `f(1) = round(n/2)`. If it doesn't break, then I'd check upward `f(2) = round(f(1) + (f(0) - f(1))/2)`. If it does break, then I'd check downward `f(2) = round(f(1) - (f(0) - f(1))/2)`. And so on, with the relation `f(n) = round(f(n-1) + (f(n-2) - f(n-1))/2)` when the egg doesn't break and `f(n) = round(f(n-1) - (f(n-2) - f(n-1))/2)` when the egg does break.

I believe this should have the same runtime complexity as a normal binary search: `O(log(n))`.
