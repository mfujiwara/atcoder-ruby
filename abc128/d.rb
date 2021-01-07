N,K=gets.chomp.split(" ").map(&:to_i)
v_array=gets.chomp.split(" ").map(&:to_i)
ret=0
(0..K).each do |i|
  next if i > N
  (0..(K-i)).each do |j|
    next if i+j > N
    left= i>0 ? v_array[0..(i-1)] : []
    right= j>0 ? v_array[(N-j)..(N-1)] : []
    all = (left+right).sort
    (K-i-j).times do
      break if all.empty? || all[0]>0
      all.shift
    end
    all.push(0)
    r = all.inject(&:+)
    ret=r if ret<r
  end
end
puts ret
