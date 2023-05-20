N,M=gets.chomp.split(" ").map(&:to_i)
h_array=gets.chomp.split(" ").map(&:to_i).sort
w_array=gets.chomp.split(" ").map(&:to_i).sort
ret_base=0
ret_add=nil
w_now=0
(1..(N-1)).each do |i|
    if i%2==0
        if ret_add!=nil
            diff=h_array[i]-h_array[i-1]
            ret_add+=diff
        end
    else
        if w_now < M && w_array[w_now]<h_array[i]
            diff = (w_array[w_now]-h_array[i-1]).abs
            w_now+=1
            while w_now<M && w_array[w_now]<h_array[i] do
                d = (w_array[w_now]-h_array[i-1]).abs
                diff = d if diff > d
                w_now+=1
            end
            tmp=ret_base+diff
            if ret_add==nil
                ret_add=tmp
            else
                ret_add=(ret_add < tmp) ? ret_add : tmp
            end
        end
        diff=h_array[i]-h_array[i-1]
        ret_base+=diff
    end
end
if w_now<M
    diff = (w_array[w_now]-h_array[-1]).abs
    w_now+=1
    while w_now<M do
        d = (w_array[w_now]-h_array[-1]).abs
        diff = d if diff > d
        w_now+=1
    end
    tmp=ret_base+diff
    if ret_add==nil
        ret_add=tmp
    else
        ret_add=(ret_add < tmp) ? ret_add : tmp
    end
end
puts ret_add
