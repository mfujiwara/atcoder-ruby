sx,sy,tx,ty=gets.chomp.split(" ").map(&:to_i)
ret=""
ret += ("U"*(ty-sy))
ret += ("R"*(tx-sx))
ret += ("D"*(ty-sy))
ret += ("L"*(tx-sx))
ret += "L"
ret += ("U"*(ty-sy+1))
ret += ("R"*(tx-sx+1))
ret += "D"
ret += "R"
ret += ("D"*(ty-sy+1))
ret += ("L"*(tx-sx+1))
ret += "U"
puts ret
