N=gets.to_i
if N<=2
    puts 1
    exit
end
m = (1..N).bsearch do |n|
    (1+n)*n/2 > N+1
end
m-=1
puts N-m+1
