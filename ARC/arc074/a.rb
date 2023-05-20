H,W=gets.chomp.split(" ").map(&:to_i)
if H%3==0 || W%3==0
    puts 0
    exit
end
h1=H/3
h2=H/3+1
w=W/2
w1=W/3
w2=W/3+1
h=H/2

r1 = [h1*W, (H-h1)*w, (H-h1)*(W-w)].sort
r2 = [h2*W, (H-h2)*w, (H-h2)*(W-w)].sort
r3 = [w1*H, (W-w1)*h, (W-w1)*(H-h)].sort
r4 = [w2*H, (W-w2)*h, (W-w2)*(H-h)].sort
r = [r1,r2,r3,r4].map {|r| r[2]-r[0] }.min
puts [r,H,W].min
