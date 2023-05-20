N=gets.to_i
array=[[true,true],[true,false],[false,true],[false,false]]
last=[]
s=gets.chomp
s.each_char.with_index do |ch, i|
  if ch=="o"
    4.times do |n|
      if array[n][-1]
        array[n].push(array[n][-2])
      else
        array[n].push(!array[n][-2])
      end
    end
  else
    4.times do |n|
      if array[n][-1]
        array[n].push(!array[n][-2])
      else
        array[n].push(array[n][-2])
      end
    end
  end
end
array.each do |arr|
  next if arr[1] != arr[-1] || arr[0] != arr[-2]
  arr.pop
  arr.shift
  arr.map{|v| print (v ? "S" : "W")}
  print "\n"
  exit
end

puts "-1"
