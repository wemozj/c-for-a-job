#include <iostream>
#include <queue>
#include <string>
#include <fstream>
using namespace std;

void push(deque<double>& values)
{
    values.push_front(1.1);
    values.push_front(2.1);
    values.push_back(3.1);
    values.push_back(4.1);
}

int main()
{
    deque<double> values;
    // ostream_iterator<double> output(std::cout, " ");
    push(values);
    values.pop_front();
    values[1] = 5.4;
    for(auto it = values.begin(); it != values.end(); it++)
    cout<<(*it)<<endl;
    //copy(values.begin(), values.end(), output);
    //std::cout << std::endl;
    return 0;
}