N=gets.to_i
MOD=10**9+7
array=gets.chomp.split("").group_by{|i|i}.map{|k,v|v.length}
puts array.inject(1) {|i,j| (i*(j+1))%MOD }-1
