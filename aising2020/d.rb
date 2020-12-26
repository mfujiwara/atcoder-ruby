N=gets.to_i
X=gets.chomp

POPCOUNT_DP={}
def popcount(n)
  POPCOUNT_DP[n] ||= n.to_s(2).count("1")
end

FUNCTION_DP={}
FUNCTION_DP[0]=0
FUNCTION_DP[1]=1
def function(n)
  FUNCTION_DP[n] ||= function(n % popcount(n))+1
end

x=X.to_i(2)
base_pop = popcount(x)
if base_pop==0
  puts [1]*N
  exit
elsif base_pop==1
  if x==1
    X.each_char do |ch|
      if ch=="1"
        puts "0"
      else
        puts "2"
      end
    end
    exit
  else
    X.each_char.with_index do |ch, i|
      if ch=="1"
        puts "0"
      else
        if i==N-1
          puts "2"
        else
          puts "1"
        end
      end
    end
    exit
  end
end
base_r0 = x % (base_pop+1)
base_r1 = x % (base_pop-1)
rr0 = [1]
rr1 = [1]
(N-1).times do
  rr0.unshift(rr0[0] * 2 % (base_pop+1))
  rr1.unshift(rr1[0] * 2 % (base_pop-1))
end
X.each_char.with_index do |ch, i|
  if ch=="0"
    y = (base_r0+rr0[i]) % (base_pop+1)
  else
    y = (base_r1-rr1[i] + base_pop-1) % (base_pop-1)
  end
  puts function(y) + 1
end
