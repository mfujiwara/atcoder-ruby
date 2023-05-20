MOD=10**9+7
N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
all_lcm=array.inject(:lcm)
puts array.inject(0) {|sum,a|
  b=all_lcm/a%MOD
  (sum+b)%MOD
}
