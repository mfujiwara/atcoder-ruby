A,B,Q=gets.chomp.split(" ").map(&:to_i)
ss=[]
A.times do
  s=gets.to_i
  ss.push(s)
end
tt=[]
B.times do
  t=gets.to_i
  tt.push(t)
end
Q.times do
  x=gets.to_i
  s_i=ss.bsearch_index{|s| s>x }
  t_i=tt.bsearch_index{|t| t>x }
  near_s = if s_i==0
    [ss[0]]
  elsif s_i==nil
    [ss[-1]]
  else
    [ss[s_i-1],ss[s_i]]
  end
  near_t = if t_i==0
    [tt[0]]
  elsif t_i==nil
    [tt[-1]]
  else
    [tt[t_i-1],tt[t_i]]
  end
  ret=10**11
  near_s.each do |s| near_t.each do |t|
    r1 = (x-s).abs + (s-t).abs
    r2 = (x-t).abs + (t-s).abs
    ret = r1 if ret>r1
    ret = r2 if ret>r2
  end end
  puts ret
end
