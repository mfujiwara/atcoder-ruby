N=gets.to_i
ret=[]
N.times do
  a=gets.to_i
  index=ret.bsearch_index{|x| x<a }
  if index
    ret[index]=a
  else
    ret.push(a)
  end
end
puts ret.length
