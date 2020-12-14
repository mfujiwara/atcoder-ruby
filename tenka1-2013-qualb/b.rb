Q,L=gets.chomp.split(" ").map(&:to_i)
STACK=[]
size=0
Q.times do
    query=gets.chomp.split(" ")
    if query[0]=="Push"
        n,m=query[1].to_i,query[2]
        if L-n.to_i < size
            puts "FULL"
            exit
        end
        STACK.push([m,n])
        size+=n
    elsif query[0]=="Pop"
        n=query[1].to_i
        if n > size
            puts "EMPTY"
            exit
        end
        c=0
        while n>c do
            last_v,last_c=STACK.pop
            c+=last_c
        end
        if n<c
            STACK.push([last_v, c-n])
        end
        size-=n
    elsif query[0]=="Top"
        if size==0
            puts "EMPTY"
            exit
        end
        puts STACK[-1][0]
    else
        puts size
    end
end
puts "SAFE"
