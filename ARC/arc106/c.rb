N,M=gets.chomp.split(" ").map(&:to_i)
if N==1
    if M==0
        puts "#{1} #{2}"
        exit
    else
        puts "-1"
        exit
    end
end
if M.abs+2 > N || M < 0
    puts "-1"
    exit
end

(N-M-2).times do |i|
    l=i*2 + 6*10**5
    puts "#{l} #{l+1}"
end

M.times do |i|
    l=10+i*2
    puts "#{l} #{l+1}"
end

if M > 0
    puts "1 #{5*10**5}"
    puts "#{5*10**5-1} #{5*10**5+1}"
else
    puts "1 3"
    puts "2 #{5*10**5}"
end
