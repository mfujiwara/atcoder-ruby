N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret=0
sum=0
i_start=0
i_end=0
array.each_with_index do |a,i|
    sum+=a
    i_end=i+1
    while sum >= K do
        sum-=array[i_start]
        i_start+=1
    end
    ret+=(i_end-i_start)
end
puts N*(N+1)/2-ret
