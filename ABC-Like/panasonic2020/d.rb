N=gets.chomp.to_i
def calc(str, used)
    if str.length==N
        puts str
        return
    end
    used.each do |a|
        calc(str+a, used)
    end
    s=("a".ord+used.length).chr
    calc(str+s, (0..(used.length)).to_a.map{|i| ("a".ord+i).chr})
end
calc("a",["a"])
