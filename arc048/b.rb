N=gets.to_i
inputs=[]
MEMO={}
RETS={}
N.times do |i|
    r,h=gets.chomp.split(" ").map(&:to_i)
    MEMO[r]||=Array.new(3,0)
    MEMO[r][h-1]+=1
    RETS[r]||=Array.new(3,nil)
    inputs.push([r,h-1])
end
count=0
MEMO.keys.sort.each do |r|
    gh,ch,ph=MEMO[r]
    sum=gh+ch+ph
    lose=N-count-sum
    RETS[r][0]="#{count+ch} #{lose+ph} #{gh-1}"
    RETS[r][1]="#{count+ph} #{lose+gh} #{ch-1}"
    RETS[r][2]="#{count+gh} #{lose+ch} #{ph-1}"
    count+=sum
end
inputs.each {|r,h| puts RETS[r][h] }
