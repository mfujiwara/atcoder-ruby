N=gets.to_i
MEMO={}
array=gets.chomp.split(" ").map(&:to_i)
duplicate=0
array.each do |a|
    if MEMO[a] != nil
        duplicate+=1
    end
    MEMO[a]=a
end
duplicate+=1 if duplicate.odd?
puts N-duplicate
