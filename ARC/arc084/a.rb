N=gets.chomp.to_i
a_array=gets.chomp.split(" ").map(&:to_i).sort
b_array=gets.chomp.split(" ").map(&:to_i).sort
c_array=gets.chomp.split(" ").map(&:to_i).sort
ret=0
a=0
c=0
b_array.each do |b|
    while a != N && a_array[a] < b do
        a+=1
    end
    while c != N && c_array[c] <= b do
        c+=1
    end
    ret+=a*(N-c)
end
puts ret
