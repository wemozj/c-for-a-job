#include <iostream>
// 统计输入中每个值连续出现的次数
int main()
{
    int currval = 0, val = 0;
    if(std::cin >> currval){
        int cnt = 1; //当前正在处理的值的个数
        while (std::cin >> val)
        {
            if (val == currval)
                ++cnt;
            else
            {
                std::cout << currval << " occurs "
                          << cnt << " times " << std::endl;
                currval = val;
                cnt = 1;
            }
            std::cout << currval << " occurs "
                          << cnt << " times " << std::endl;
        }
        std::cout << currval << " occurs "
                          << cnt << " times " << std::endl;
    }
    return 0;
}