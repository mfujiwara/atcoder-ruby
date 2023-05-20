S=gets.chomp
count=0
(0..(S.length/2-1)).each do |i|
    count+=1 if S[i]!=S[-1-i]
end
if count==0
    if S.length.odd?
        puts (S.length-1)*25
    else
        puts S.length*25
    end
elsif count==1
    puts (S.length*25)-2
else
    puts S.length*25
end
