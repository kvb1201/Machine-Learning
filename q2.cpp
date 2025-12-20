#include<iostream>

using namespace std;

int main()
{
    int t;
    cin >>t;
    while(t--)
    {
         long long int n;
        cin >>n;
        int k = log10(n) +1;
        int flag =0;
        while( k >0 )
        {
            int m = (pow(10,k) +1);
            if(n%m == 0)
            {
                flag =1;
                cout << n/m <<" ";
            }
            k--;
        }
        if(flag == 0)
        {
            cout <<0;
        }
        cout <<endl;
        


    }
}