N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
MEMO={}
MEMO[N-1]=0
MEMO[N-2]=(array[-1]-array[-2]).abs
(N-3).downto(0) do |n|
    a = (array[n]-array[n+1]).abs + MEMO[n+1]
    b = (array[n]-array[n+2]).abs + MEMO[n+2]
    MEMO[n] = a < b ? a : b
end
puts MEMO[0]
