#include<iostream>
using namespace std;

int main()
{
 int t;
    cin >>t;
    while (t--)
    {   long long int k;
        cin >>k;
        int sum =0;
        for(int i =1; i <=k; i++)
        {
            long long int num =i;
            while(num != 0)
            {
                int dig = num%10;
                sum += dig;
                num /=10;
            }
        }
        cout << sum<<endl;

    }
    
}