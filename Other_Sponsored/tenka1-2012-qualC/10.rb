S=gets.chomp
c=0
progress_d=["",0]
progress_c=["",0]
progress_h=["",0]
progress_s=["",0]
while c<S.length do
    m=S[c]
    n=S[c+1]
    n = "10" if n=="1"
    progress_d[0]+=(m+n) if m!="D" || !["10","J","Q","K","A"].include?(n)
    progress_c[0]+=(m+n) if m!="C" || !["10","J","Q","K","A"].include?(n)
    progress_h[0]+=(m+n) if m!="H" || !["10","J","Q","K","A"].include?(n)
    progress_s[0]+=(m+n) if m!="S" || !["10","J","Q","K","A"].include?(n)

    if ["10","J","Q","K","A"].include?(n)
        progress = if m=="D"
            progress_d
        elsif m=="C"
            progress_c
        elsif m=="H"
            progress_h
        else
            progress_s
        end
        progress[1]+=1
        if progress[1]==5
            if progress[0]==""
                puts "0"
            else
                puts progress[0]
            end
            exit
        end
    end

    c+= (n=="10" ? 3 : 2)
end