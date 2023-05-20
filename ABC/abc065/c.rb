N,M=gets.chomp.split(" ").map(&:to_i).sort
diff = (N - M).abs
mod = 10**9 + 7
if diff > 1
    puts 0
    exit
end

ret = (1..N).inject(1){|i,j| i*j%mod }

if diff == 1
    puts ret*ret*M % mod
else
    puts ret*ret*2 % mod
end
