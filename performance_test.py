import timeit

# 计时列表创建（修正变量名笔误）
test1 = timeit.repeat('a=[1,2,3]', repeat=100)
# 计时元组创建
test2 = timeit.repeat('b=(1,2,3)', repeat=100)

# 计算列表创建的平均耗时（修复缩进）
a_sum = 0
for each in test1:
    a_sum = a_sum + each  # 这一行必须缩进，属于循环体
average = a_sum / len(test1)

# 输出结果
print(f"列表创建的平均耗时：{average:.8f} 秒")
print(f"元组创建的平均耗时：{sum(test2)/len(test2):.8f} 秒")