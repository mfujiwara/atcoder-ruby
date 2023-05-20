S1=gets.chomp
MAP1={}
S1.each_char do |c|
    MAP1[c]||=0
    MAP1[c]+=1
end
S2=gets.chomp
MAP2={}
S2.each_char do |c|
    MAP2[c]||=0
    MAP2[c]+=1
end
S3=gets.chomp
MAP3={}
S3.each_char do |c|
    MAP3[c]||=0
    MAP3[c]+=1
end

rest1=S3.length/2
rest2=rest1
MAP3.each do |ch,count|
    c1=MAP1[ch]||0
    c2=MAP2[ch]||0
    if c1+c2<count
        puts "NO"
        exit
    elsif c1+c2==count
        rest1-=c1
        rest2-=c2
        if rest1<0 || rest2<0
            puts "NO"
            exit
        end
    else
        if c1<count
            rest2-=(count-c1)
            if rest2<0
                puts "NO"
                exit
            end
        end
        if c2<count
            rest1-=(count-c2)
            if rest1<0
                puts "NO"
                exit
            end
        end
    end
end
puts "YES"
