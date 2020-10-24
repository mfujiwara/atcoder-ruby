N=gets.to_i
b=1
a=1
while 5**b < N do
    aa = N - 5**b
    a=1
    while 3**a < aa do
        a+=1
    end
    if 3**a + 5**b == N 
        puts "#{a} #{b}"
        exit
    end
    b+=1
end
puts "-1"
