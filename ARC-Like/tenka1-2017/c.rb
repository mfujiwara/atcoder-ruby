N=gets.to_i
(1..3500).each do |h|
    (h..3500).each do |n|
        d = 4*h*n - n*N - h*N
        next if d <= 0
        if h*n*N % d == 0
            w = h*n*N / d
            puts "#{h} #{n} #{w}"
            exit
        end
    end
end
