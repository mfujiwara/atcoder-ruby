N,K=gets.chomp.split(" ").map(&:to_i)
arrays=[]
needs_new=true
pre = 1
N.times do
    s=gets.to_i
    if s==0
        puts N
        exit
    end
    if s<=K
        arrays.push([]) if needs_new || pre*s > K
        needs_new=false
        arrays[-1].push(s)
        pre=s
    else
        needs_new=true
        pre=1
    end
end
ret=0
arrays.each do |array|
    ret=1 if ret==0
    start_index=0
    end_index=0
    diff_index=1
    val=array[0]
    while end_index < array.length-1 do
        tmp=val*array[end_index+1]
        if tmp <= K
            val=tmp
            end_index+=1
            diff_index+=1
            ret=diff_index if ret<diff_index
        else
            val=val/array[start_index]
            start_index+=1
            diff_index-=1
        end
    end    
end
puts ret
