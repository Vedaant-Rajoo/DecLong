#include<iostream>
#include<string>
using namespace std;
int main(){
    int n,r;
    cin>>n>>r;
    for (int i=0;i<n;i++){
        int f;
        string arr[n+2];
        cin>>f;
        if (f<r){
            arr[i]="Bad boi";
        }
        else
        arr[i]="Good boi";
    }
    for (int j=0;j<n;j++)[
        cout<<arr[j]<<endl;
    ]
}