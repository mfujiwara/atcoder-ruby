N,A,B,C=gets.chomp.split(" ").map(&:to_i)
ls=[]
N.times do
  l=gets.to_i
  ls.push(l)
end

ret=10**10
n1=N/3
(1..n1).each do |i|
  n2=(N-i)/2
  (i..n2).each do |j|
    n3=N-i-j
    (j..n3).each do |k|
      ls.permutation do |perm|
        a=perm[0..(i-1)].inject(&:+)
        b=perm[i..(i+j-1)].inject(&:+)
        c=perm[(i+j)..(i+j+k-1)].inject(&:+)
        abc=[a,b,c].sort.reverse
        r= (A-abc[0]).abs + (B-abc[1]).abs + (C-abc[2]).abs + (i+j+k-3)*10
        ret=r if ret>r
      end
    end
  end
end
puts ret
