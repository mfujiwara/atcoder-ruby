N=gets.to_i
DIC={
    "a" => "",
    "b" => "1",
    "c" => "1",
    "d" => "2",
    "e" => "",
    "f" => "4",
    "g" => "9",
    "h" => "8",
    "i" => "",
    "j" => "3",
    "k" => "8",
    "l" => "5",
    "m" => "7",
    "n" => "9",
    "o" => "",
    "p" => "7",
    "q" => "4",
    "r" => "0",
    "s" => "6",
    "t" => "3",
    "u" => "",
    "v" => "5",
    "w" => "2",
    "x" => "6",
    "y" => "",
    "z" => "0",
    "," => "",
    "." => "",
    " " => " "
}
W=gets.chomp.downcase + " "
rets = []
ret = ""
(0..(W.length-1)).each do |i|
    r = DIC[W[i]]
    next if r.empty?
    if r == " "
        if !ret.empty?
            rets.push(ret) 
            ret = ""
        end
    else
        ret = "#{ret}#{r}"
    end
end
puts rets.join(" ")
