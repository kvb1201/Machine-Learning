#include <iostream>
using namespace std;
#include <string>


int main()
{
    int t;
    cin >>t;
    while(t--)
    {   
        int n;
        cin >>n;
        string a;
        cin >>a;
        int m;
        cin>>m;
        string b,c;
        cin>>b;
        cin >>c;

        string d,v;
        for(int i =0; i <m; i++)
        {
            if(c[i] == 'v')
            {
                v += b[i];
            }
            else
            {
                d += b[i];
            }
        }
        a = v +a +d;
        cout <<a <<endl;

    }
}