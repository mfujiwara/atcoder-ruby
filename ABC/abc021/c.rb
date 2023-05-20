MOD=10**9+7
N=gets.to_i
a,b=gets.chomp.split(" ").map(&:to_i)
if a==b
  puts 1
  exit
end
M=gets.to_i
EDGES={}
M.times do
  x,y=gets.chomp.split(" ").map(&:to_i)
  EDGES[x]||={}
  EDGES[x][y]="1"
  EDGES[y]||={}
  EDGES[y][x]="1"
end
D={}
D[a]=[0,1]
nows=[a]
loop do
  break if D[b]!=nil
  nexts=[]
  nows.each do |x|
    EDGES[x].keys.each do |y|
      D[y]||=[200,0]
      next if D[y][0] <= D[x][0]
      nexts.push(y) if D[y][0] ==200
      D[y][0]=D[x][0]+1
      D[y][1]+=D[x][1]
      D[y][1]%=MOD
    end
  end
  nows=nexts
end
puts D[b][1]
