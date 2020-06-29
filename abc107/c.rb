N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret = 10**9
(0..(N-K)).each do |ind_s|
    ind_e = ind_s + K - 1
    r = 0
    if array[ind_s] < 0 && array[ind_e] < 0
        r = -1 * array[ind_s]
    elsif array[ind_s] < 0 && array[ind_e] >= 0
        if array[ind_s] * -1 > array[ind_e]
            r = array[ind_e] * 2 - array[ind_s]
        else
            r = array[ind_s] * -2 + array[ind_e]
        end
    else
        r = array[ind_e]
    end

    if r < ret
        ret = r
    end
end
puts ret
