N,Q=gets.chomp.split(" ").map(&:to_i)
CONES=[]
N.times do
    x,r,h=gets.chomp.split(" ").map(&:to_i)
    CONES.push([x,r,h])
end
Q.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    ret=0.0
    CONES.each do |x,r,h|
        next if b <= x || x+h <= a
        if a<=x && x+h<=b
            # a x x+h b
            ret+=Math::PI*r*r*h/3
        elsif x+h<=b
            # x a x+h b
            h2=x+h-a
            r2=r.to_f*h2/h
            ret+=Math::PI*r2*r2*h2/3
        elsif a<=x
            # a x b x+h
            h3=x+h-b
            r3=r.to_f*h3/h
            ret+=Math::PI*r*r*h/3
            ret-=Math::PI*r3*r3*h3/3
        else
            # x a b x+h
            h2=x+h-a
            r2=r.to_f*h2/h
            ret+=Math::PI*r2*r2*h2/3
            h3=x+h-b
            r3=r.to_f*h3/h
            ret-=Math::PI*r3*r3*h3/3
        end
    end
    puts ret
end
