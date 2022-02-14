
//create fibo function with recursive call and return the value of the fibo number at the given position

fn fibo(n: i32) -> i32 {
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
}


fn main() {
    //print fibo with loop and range 0..10 and print the result with println! macro
    for i in 0..300 {
        println!("fibo({}) = {}", i, fibo(i));
    }



}





