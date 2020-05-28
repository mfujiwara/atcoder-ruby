N = gets.to_i
histries = {}
my_turn = true
last_letter = nil
N.times do
    w = gets.chomp
    if histries[w] != nil
        puts my_turn ? "LOSE" : "WIN"
        exit
    elsif last_letter != nil && w[0] != last_letter
        puts my_turn ? "LOSE" : "WIN"
        exit
    end
    histries[w] = 0
    last_letter = w[-1]
    my_turn = !my_turn
end
puts "DRAW"
