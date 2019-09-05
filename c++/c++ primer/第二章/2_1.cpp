#include <iostream>
// 无符号类型仅能表示大于等于0的值
// 赋给无符号类型一个超出它表示范围的值时，结果是初始值对无符号类型
// 表示数值总数取模后的余数
// 当一个算术表达式中既有 无符号数 又有 int值时，那个int值就会转换成无符号数。
int main()
{
    unsigned u = 10, u2 = 42;
    std::cout << u2 - u << std::endl; // 32
    std::cout << u - u2 << std::endl; // 4294967264

    int i = 10, i2 = 42;
    std::cout << i2 - i << std::endl; // 32
    std::cout << i - i2 << std::endl; // -32
    std::cout << i - u  << std::endl; // 0
    std::cout << u - i  << std::endl; // 0
    std::cout << u - i2  << std::endl; // 4294967264

    return 0;
}