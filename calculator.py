#!/usr/bin/env python3
"""简单计算器：支持加法。"""


def add(a: float, b: float) -> float:
    """返回两个数字之和。"""
    return a + b


if __name__ == "__main__":
    print("简单加法计算器")
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    result = add(num1, num2)
    # 整数结果时输出整数形式，其他情况保留小数
    if result.is_integer():
        print(f"结果: {int(result)}")
    else:
        print(f"结果: {result}")
