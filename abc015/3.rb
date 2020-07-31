N,K=gets.chomp.split(" ").map(&:to_i)
ans=[0]
N.times do
    ts = gets.chomp.split(" ").map(&:to_i)
    nexts = []
    ts.each do |t|
        ans.each do |a|
            nexts.push(t^a)
        end
    end
    ans = nexts
end
puts ans.include?(0) ? "Found" : "Nothing"
