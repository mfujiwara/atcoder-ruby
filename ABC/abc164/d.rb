S=gets.chomp
ret=0
BASE_MODS=[1]
(1..(S.length-1)).each do |i|
    BASE_MODS.push(BASE_MODS[-1]*10%2019)
end
MODS=Array.new(2019,0)
MODS[0]=1
s=0
(0..(S.length-1)).each do |i|
    s+=S[S.length-1-i].to_i * BASE_MODS[i]
    s%=2019
    ret+=MODS[s]
    MODS[s]+=1
end 
puts ret
