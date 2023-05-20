N=gets.to_i
A,B=gets.chomp.split(" ").map(&:to_i)
if A==B
    if N % (A+1)==0
        puts "Aoki"
    else
        puts "Takahashi"
    end
elsif A>B
    puts "Takahashi"
else
    if N<=A
        puts "Takahashi"
    else
        puts "Aoki"
    end
end
