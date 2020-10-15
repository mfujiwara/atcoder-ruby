N,M=gets.chomp.split(" ").map(&:to_i)
MEMO=Array.new(N){[]}
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    MEMO[a-1].push(b-1)
    MEMO[b-1].push(a-1)
end
N.times do |i|
    friends = MEMO[i]
    friends_of_firends = friends.map{|f| MEMO[f] }.flatten.uniq
    friends_of_firends.delete(i)
    friends.each {|f| friends_of_firends.delete(f) }
    puts friends_of_firends.length
end