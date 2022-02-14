
//create a function that returns the nth fibonacci number (the sum of the two previous numbers)



func fibonacci(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return fibonacci(n-1) + fibonacci(n-2)
    }
}











