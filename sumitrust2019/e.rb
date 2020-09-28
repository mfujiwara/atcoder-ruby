N=gets.to_i
MOD=10**9+7
array=gets.chomp.split(" ").map(&:to_i)
M={}
M[0]=3
ret=1
array.each do |a|
    M[a]||=0
    ret*=M[a]
    ret%=MOD
    M[a]-=1
    M[a+1]||=0
    M[a+1]+=1
end
puts ret
