N,M=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
combos=[]
M.times do
    combo=gets.chomp.split(" ").map(&:to_i)
    b=combo[0]
    c=combo[1]
    combos.push([b,combo[2..(c+1)]])
end
ret=0
(1..N).to_a.combination(9) do |idles|
    r=0
    idles_hash={}
    idles.each do |idle|
        r+=array[idle-1]
        idles_hash[idle]="1"
    end
    combos.each do |b,combo|
        c=0
        combo.each do |comb|
            c+=1 if idles_hash[comb]
            if c==3
                r+=b
                break
            end
        end
    end
    ret=r if ret<r
end
puts ret
