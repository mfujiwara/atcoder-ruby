N,T=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret=0
diff_max=0
b_price=array[0]
b_price_count=1
s_price_count=0
(1..(N-1)).each do |i|
  if b_price == array[i]
    b_price_count+=1
  elsif b_price > array[i]
    ret+=[b_price_count,s_price_count].min
    b_price=array[i]
    b_price_count=1
    s_price_count=0
  else
    diff = array[i]-b_price
    if diff==diff_max
      s_price_count+=1
    elsif diff>diff_max
      ret=0
      diff_max=diff
      s_price_count=1
    end
  end
end
ret+=[b_price_count,s_price_count].min
puts ret
