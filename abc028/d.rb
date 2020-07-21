N,K=gets.chomp.split(" ").map(&:to_i)
cmb = 0
cmb+=(K-1)*(N-K)*6
cmb+=(N-1)*3
cmb+=1
puts cmb.to_f / (N**3).to_f
