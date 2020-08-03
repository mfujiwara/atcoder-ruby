N=gets.to_i
if N == 1
    puts 1
    exit
end
xys=[]
diffs={}
N.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    xys.each do |w,t|
        if x>w || x==w && y>t
            diffs["#{x-w}_#{y-t}"] ||= 0
            diffs["#{x-w}_#{y-t}"] += 1
        else
            diffs["#{w-x}_#{t-y}"] ||= 0
            diffs["#{w-x}_#{t-y}"] += 1
        end
    end
    xys.push([x,y])
end
n=diffs.values.sort[-1]
puts N-n
