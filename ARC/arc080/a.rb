N = gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
grouped = array.group_by {|i| i%4}
n4=grouped[0].length
n2=grouped[2].length
n1=N-n4-n2
puts n4*2>=n1 ? 'Yes' : 'No'
