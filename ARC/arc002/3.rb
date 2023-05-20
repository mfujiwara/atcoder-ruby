N = gets.to_i
cmd = gets.chomp

MEMO = {}
def eval(cmd, lr)
    key = "#{cmd}_#{lr[0]}_#{lr[1]}"
    return MEMO[key] if MEMO[key]

    return 1 if cmd.length == 1 || cmd == lr[0] || cmd == lr[1]
    return 1 if cmd.length == 2 && (cmd==lr[0]||cmd==lr[1])

    next_cmd = cmd[2 .. -1]

    rets = []
    # Lを使う
    if (lr[0] == cmd[0 .. 1])
        rets.push(eval(cmd[2 .. -1], lr) + 1)
    end

    # Rを使う
    if (lr[1] == cmd[0 .. 1])
        rets.push(eval(cmd[2 .. -1], lr) + 1)
    end

    # そのまま
    rets.push(eval(cmd[1 .. -1], lr) + 1)

    # 最小値
    ret = rets.min
    MEMO[key] = ret
    return ret
end

ret = N
["A","B","X","Y"].repeated_permutation(2).map {|a, b| "#{a}#{b}"}.combination(2) do |l,r|
    ret = [eval(cmd, [l,r]), ret].min
    MEMO = {}
end
puts ret
