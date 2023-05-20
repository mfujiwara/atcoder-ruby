N=gets.to_i
T=gets.chomp
if N==1
    if T=="1"
        puts 2*10**10
    else
        puts 10**10
    end
    exit
end
if N==2
    if T=="11"
        puts 10**10
    elsif T=="10"
        puts 10**10
    elsif T=="01"
        puts 10**10-1
    else
        puts 0
    end
    exit
end
110110
if T[0..2]=="110"
    (3..(N-1)).each do |i|
        if (i%3==0 && T[i]!="1") || (i%3==1 && T[i]!="1") || (i%3==2 && T[i]!="0")
            puts 0
            exit
        end
    end
    r=(N+2)/3
    puts 10**10-r+1
elsif T[0..2]=="101"
    (3..(N-1)).each do |i|
        if (i%3==0 && T[i]!="1") || (i%3==1 && T[i]!="0") || (i%3==2 && T[i]!="1")
            puts 0
            exit
        end
    end
    r=N/3+1
    puts 10**10-r+1
elsif T[0..2]=="011"
    (3..(N-1)).each do |i|
        if (i%3==0 && T[i]!="0") || (i%3==1 && T[i]!="1") || (i%3==2 && T[i]!="1")
            puts 0
            exit
        end
    end
    r=(N+1)/3+1
    puts 10**10-r+1
else
    puts 0
end
