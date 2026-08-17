example='01001011111010101101111110'

def stuffer(bit_stream):
    stuffed_list=['0','1','1','1','1','1','1','0']
    one_count=0
    for bit in bit_stream:
        stuffed_list.append(bit)
        if bit=='1':
            one_count+=1
            if one_count==5:
                stuffed_list.append('0')
        if bit=='0':
            one_count=0
    stuffed_list.extend(['0','1','1','1','1','1','1','0'])
    stuffed=''.join(stuffed_list)
    return stuffed

def destuffer(bit_stream):
    destuffed_list=[]
    one_count=0
    for bit in bit_stream[8:-8]:
            if bit=='0':
                if one_count==5:
                    one_count=0
                    continue
                else:
                    destuffed_list.append(bit)
                one_count=0
            if bit=='1':
                one_count+=1
                destuffed_list.append(bit)
    destuffed=''.join(destuffed_list)
    return destuffed