N = gets.to_i
array = []
N.times {
    array.push(gets.to_i)
}

Maximum = array.inject(:+)
puts Maximum

max = array.max

diff = max*2 - Maximum 
puts [diff, 0].max
