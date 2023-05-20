S=gets.chomp
if S=="{}"
    puts "dict"
    exit
end
depth = 0
(1..(S.length-1)).each do |i|
    if S[i] == "{"
        depth+=1
    elsif S[i] == "}"
        depth-=1
    elsif depth == 0
        if S[i] == ","
            puts "set"
            exit
        elsif S[i] == ":"
            puts "dict"
            exit
        end
    end
    i+=1
end
puts "set"
