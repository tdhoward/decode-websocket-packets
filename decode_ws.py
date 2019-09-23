
print("Enter string of hex bytes:")
payload = input()

websocket_payload = bytes.fromhex(payload.replace("\n", ""))

def DecodedCharArrayFromByteStreamIn(byteArray):
    datalength = byteArray[1] & 127
    indexFirstMask = 2 
    if datalength == 126:
        indexFirstMask = 4
    elif datalength == 127:
        indexFirstMask = 10
    masks = [m for m in byteArray[indexFirstMask : indexFirstMask+4]]
    indexFirstDataByte = indexFirstMask + 4
    decodedChars = []
    i = indexFirstDataByte
    j = 0
    while i < len(byteArray):
        decodedChars.append( chr(byteArray[i] ^ masks[j % 4]) )
        i += 1
        j += 1
    return "".join(decodedChars)

print(DecodedCharArrayFromByteStreamIn(websocket_payload))
