N=gets.to_i
array=[]
N.times do
    t=gets.to_i
    index = array.bsearch_index {|x| x >= t } || array.length
    array.insert(index, t)
end
MOD = 10**9+7
sum = 0
time = 0
cmb = 1
pre = [0, 1]
array.each do |t|
    sum += time + t
    time += t
    if pre[0] == t
        pre[1] += 1
    else
        pre = [t, 1]
    end
    cmb *= pre[1]
    cmb %= MOD
end
puts sum
puts cmb
