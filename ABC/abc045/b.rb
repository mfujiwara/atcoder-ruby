a = gets.chomp.split("")
b = gets.chomp.split("")
c = gets.chomp.split("")

turn = "a"
loop do
    next_turn = nil
    case turn
    when "a" then
        next_turn = a.shift
    when "b" then
        next_turn = b.shift
    when "c" then
        next_turn = c.shift
    end
    if next_turn == nil
        puts turn.upcase
        exit
    else
        turn = next_turn
    end
end
