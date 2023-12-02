input = open("2023\\day1\\input.txt", "r")
map = readlines(input)
close(input)
println(typeof(map))

for m in map
    global results
    first_match = match(r"\d", m)
    last_match = match(r"\d(?=\D*$)", m)
    
    # Check if both matches are not empty
    if first_match !== nothing && last_match !== nothing
        num = string(first_match.match, last_match.match)
        results += parse(Int, num)
    else
        println("Skipping line: $m")
    end
end

print(results)