N,M=gets.chomp.split(" ").map(&:to_i)
NAME=gets.chomp
KIT=gets.chomp
name_grouped=NAME.split("").group_by {|s| s}
kit_grouped=KIT.split("").group_by {|s| s}
ret=0
name_grouped.each do |key, list|
    need=list.length
    provide=(kit_grouped[key]||[]).length
    if provide==0
        puts "-1"
        exit
    end
    r=(need+provide-1)/provide
    ret=r if ret < r
end
puts ret
