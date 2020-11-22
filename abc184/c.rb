R1,C1=gets.chomp.split(" ").map(&:to_i)
R2,C2=gets.chomp.split(" ").map(&:to_i)
if R1==R2 && C1==C2
    puts 0
elsif R1+C1==R2+C2 || R1-C1==R2-C2 || (R1-R2).abs+(C1-C2).abs<=3
    puts 1
elsif (R1+C1)%2 == (R2+C2)%2 || (R1+C1-R2-C2).abs<=3 || (R1-C1-R2+C2).abs<=3
    puts 2
else
    puts 3
end
