with open('test.txt') as input_text:
    text = input_text.readlines()
    print(text)


def create_packets(lines: list):
    packets = []
    for line in lines:
        if line == '\n':
            continue
        packet = []
        buffer = []
        for i in range(len(line)):
            match line[i]:
                case '[':
                    return create_packets(line[i:])
                case ']':
                    packet.append(buffer)
                    buffer = []
                case '\n':
                    return packets.append(packet)
                case ',':
                    pass
                case x:
                    buffer.append(int(x))


ans = create_packets(text)
print(ans)