P=gets.to_f
# f(x) = x + P/(2**(2x/3))
# f'(x) = 1 - 2/3 * log2*P / 2^(2x/3) = 0
# 2^(2x/3) = 2/3 * log2*P)
# 2x/3 = log_2(2/3 * log2*P)
# x = log_2(2/3 * log2*P) * (3/2)
tmp=(2.0/3.0*Math.log(2)*P)
x=[Math.log(tmp,2)*3/2,0].max
ret = x + P/(2**(2*x/3))
puts ret
