N,Q=gets.chomp.split(" ").map(&:to_i)
board=Array.new(N,0)
Q.times do
    l,r=gets.chomp.split(" ").map(&:to_i)
    board[l-1]+=1
    board[r]-=1 if r < N
end
c=0
board.each do |b|
    c+=b
    print c%2==1 ? "1" : "0"
end
puts