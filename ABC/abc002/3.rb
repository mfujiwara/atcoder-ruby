xa,ya,xb,yb,xc,yc=gets.chomp.split(" ").map(&:to_i)
puts 0.5*((xa-xc)*(yb-yc)-(xb-xc)*(ya-yc)).abs
