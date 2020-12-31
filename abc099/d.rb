N,C=gets.chomp.split(" ").map(&:to_i)
D_MTX=[]
C.times do
  d_row=gets.chomp.split(" ").map(&:to_i)
  D_MTX.push(d_row)
end
c_diffs=Array.new(3){Array.new(C){|i| [i, 0]}}
N.times do |i|
  c_row=gets.chomp.split(" ").map(&:to_i)
  N.times do |j|
    group=(i+j)%3
    from_c=c_row[j]-1
    C.times do |to_c|
      c_diffs[group][to_c][1]+=D_MTX[from_c][to_c]
    end
  end
end
3.times do |i|
  c_diffs[i] = c_diffs[i].sort_by {|i,v| v}
end
ret=10**10
3.times do |i| 3.times do |j| 3.times do |k|
  to_c0 = c_diffs[0][i][0]
  to_c1 = c_diffs[1][j][0]
  to_c2 = c_diffs[2][k][0]
  next if to_c0==to_c1 || to_c0==to_c2 || to_c1==to_c2
  r = c_diffs[0][i][1] + c_diffs[1][j][1] + c_diffs[2][k][1]
  ret=r if ret>r
end end end
puts ret
