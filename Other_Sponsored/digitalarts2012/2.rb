ccc=gets.chomp
if ccc=="a" || ccc=="zzzzzzzzzzzzzzzzzzzz"
  puts "NO"
  exit
end
if ccc.length==1
  puts (ccc.ord-1).chr + "a"
  exit
end
ccc.each_char.with_index do |ch,index|
  if ccc[0]!=ch
    ccc[0],ccc[index]=ccc[index],ccc[0]
    puts ccc
    exit
  end
end
if ccc[0]=="a"
  puts "b" + "a"*(ccc.length-2)
  exit
end
puts (ccc[0].ord-1).chr + (ccc[0].ord+1).chr + ccc[0]*(ccc.length-2)
