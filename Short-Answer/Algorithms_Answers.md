#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

1.  I believe this code runs in `O(n^3)`. Even though `a` is increasing by `n * n` each iteration, the condition of the loop `while a < n * * n` should dominate as `n` increases.

2.  I believe this code runs in `O(n * log(n))`. The outer loop contributes a factor of `n`, because its counter increases by a constant `1` with each repetition. The inner loop contributes `log(n)` because, rather its counter is multiplied by `2` with each repetition: so it's `log_2(n)`.

3.  I believe this code runs in `O(n)`, where `n = bunnies`. The function `bunnyEars` only calls itself one or zero times per call, so it doesn't exponentially explode.

## Exercise II
