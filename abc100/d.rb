N,M=gets.chomp.split(" ").map(&:to_i)
if M==0
  puts 0
  exit
end
XYZ=[]
N.times do
  x,y,z=gets.chomp.split(" ").map(&:to_i)
  XYZ.push([x,y,z])
end
xxx=XYZ.sort_by{|x,y,z| x+y+z}
yyy=XYZ.sort_by{|x,y,z| x-y+z}
zzz=XYZ.sort_by{|x,y,z| x+y-z}
ttt=XYZ.sort_by{|x,y,z| x-y-z}
def calc(xyzs)
  xx,yy,zz=0,0,0
  xyzs.each do |x,y,z|
    xx+=x
    yy+=y
    zz+=z
  end
  return xx.abs + yy.abs + zz.abs
end
r1=calc(xxx[0..(M-1)])
r2=calc(xxx[(N-M)..(N-1)])
r3=calc(yyy[0..(M-1)])
r4=calc(yyy[(N-M)..(N-1)])
r5=calc(zzz[0..(M-1)])
r6=calc(zzz[(N-M)..(N-1)])
r7=calc(ttt[0..(M-1)])
r8=calc(ttt[(N-M)..(N-1)])

puts [r1,r2,r3,r4,r5,r6,r7,r8].max
