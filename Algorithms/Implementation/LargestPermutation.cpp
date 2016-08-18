#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    ios_base::sync_with_stdio(false);
    unsigned long long N, K, temp;
    int8_t *array;
    array = new int8_t[N];
    unsigned long long largestSoFar;

    cin >>  N >> K;
    largestSoFar N;
    for(unsigned long long i = 0;i<N;i++)
        cin >> array[i];

    for(unsigned long long i = 0;i<N;i++){
        if (array[i] < largestSoFar){
          //find largest number above the array
          for(unsigned long long j = i;j<N;j++){
            if (array[j] > largestSoFar){
              temp = array[i];
              array[i] = array[j];
              array[j] = temp;
              if (--K){
                largestSoFar = -1;
              }
            }
          }
        }

        cout << array[i] << " ";
    }
    cout << "\b"
    return 0;
}
