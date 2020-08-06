N,M=gets.chomp.split(" ").map(&:to_i)
A=[]
N.times do
    a=gets.chomp
    A.push(a)
end
B=[]
M.times do
    b=gets.chomp
    B.push(b)
end
(0..(N-M)).each do |x|
    (0..(N-M)).each do |y|
        judge=true
        (0..(M-1)).each do |m|
            a=A[m+x][y,M]
            b=B[m]
            if a!=b
                judge=false
                break
            end
        end
        if judge
            puts "Yes"
            exit
        end
    end
end
puts "No"
