        cout << " \n" << c;
    }
    cout << endl;
    return 0;




#include <iostream>
using namespace std;


//create fibo function with recursive call and return the value of the fibo number at the given position


int fibo(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibo(n - 1) + fibo(n - 2);
    }
}


//print fibo with loop and range 0..10 and print the result with println! macro


int main()
{
    for (int i = 0; i <= 10; i++)
    {
        //println!("{}", fibo(i)); cout << " \n" << fibo(i);
        cout << " \n" << fibo(i);

    }

    return 0;

}


